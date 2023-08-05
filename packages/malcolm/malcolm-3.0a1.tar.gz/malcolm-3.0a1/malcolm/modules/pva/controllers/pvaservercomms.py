import pvaccess
from annotypes import add_call_types

from malcolm.core import Loggable, Queue, Get, Put, Post, Subscribe, \
    Error, ProcessPublishHook, APublished, serialize_object, \
    serialize_hook
from malcolm.modules import builtin
from .pvautil import dict_to_pv_object, value_for_pva_set, strip_tuples


class PvaServerComms(builtin.controllers.ServerComms):
    """A class for communication between pva client and server"""

    def __init__(self, mri):
        # type: (builtin.controllers.AMri) -> None
        super(PvaServerComms, self).__init__(mri, use_cothread=False)
        self._pva_server = None
        self._spawned = None
        self._published = ()
        self._endpoints = None
        # Hooks
        self.register_hooked(ProcessPublishHook, self.publish)

    def do_init(self):
        self._start_pva_server()

    @add_call_types
    def publish(self, published):
        # type: (APublished) -> None
        # Administer endpoints
        self._published = published
        if self._pva_server:
            with self._lock:
                # Delete blocks we no longer have
                for mri in self._endpoints:
                    if mri not in published:
                        # TODO: delete endpoint here when we can
                        pass
                # Add new blocks
                for mri in published:
                    if mri not in self._endpoints:
                        self._add_new_pva_channels(mri)

    def _add_new_pva_channels(self, mri):
        controller = self.process.get_controller(mri)
        self._add_new_pva_channel(mri, controller)
        b = controller.make_view()
        for field in b:
            self._add_new_pva_channel(mri, controller, field)

    def _add_new_pva_channel(self, mri, controller, field=None):
        """Create a new PVA endpoint for the block name

        Args:
            mri (str): The name of the block to create the PVA endpoint
        """

        def _get(pv_request):
            try:
                return PvaGetImplementation(mri, controller, field, pv_request)
            except Exception:
                self.log.exception("Error doing Get")

        def _put(pv_request):
            try:
                return PvaPutImplementation(mri, controller, field, pv_request)
            except Exception:
                self.log.exception("Error doing Put")

        def _rpc(pv_request):
            try:
                rpc = PvaRpcImplementation(mri, controller, field, pv_request)
                return rpc.execute
            except Exception:
                self.log.exception("Error doing Rpc")

        def _monitor(pv_request):
            try:
                return PvaMonitorImplementation(
                    mri, controller, field, pv_request)
            except Exception:
                self.log.exception("Error doing Monitor")

        endpoint = pvaccess.Endpoint()
        endpoint.registerEndpointGet(_get)
        endpoint.registerEndpointPut(_put)
        # TODO: There is no way to eliminate dead RPC connections
        endpoint.registerEndpointRPC(_rpc)
        # TODO: There is no way to eliminate dead monitors
        # TODO: Monitors do not support deltas
        endpoint.registerEndpointMonitor(_monitor)
        self._endpoints.setdefault(mri, []).append(endpoint)
        if field:
            mri += ".%s" % field
        self._pva_server.registerEndpoint(mri, endpoint)

    def _start_pva_server(self):
        if self._pva_server is None:
            self._pva_server = pvaccess.PvaServer()
            # {mri: Endpoint}
            self._endpoints = {}
            for mri in self._published:
                self._add_new_pva_channels(mri)
            self._spawned = self.spawn(self._pva_server.startListener)

    def _stop_pva_server(self):
        if self._pva_server is not None:
            self._pva_server.shutdown()
            self._pva_server = None
            self._spawned.wait(10)


class PvaImplementation(Loggable):
    def __init__(self, mri, controller, field, pv_request):
        self.set_logger(mri=mri)
        self._mri = mri
        self._controller = controller
        self._field = field
        self._request = pv_request
        self.log.debug(
            "Mri %r field %r got request %s", mri, field, pv_request.toDict())

    def _dict_to_path_value(self, pv_request):
        value = pv_request.toDict()
        if "field" in value:
            value = value["field"]
        path = []
        if self._field:
            path.append(self._field)
        while isinstance(value, dict) and len(value) == 1:
            endpoint = list(value)[0]
            value = value[endpoint]
            path.append(endpoint)
        return path, value

    def _request_response(self, request_cls, path, **kwargs):
        queue = Queue()
        request = request_cls(path=[self._mri] + path, **kwargs)
        request.set_callback(queue.put)
        self._controller.handle_request(request)
        response = queue.get()
        if isinstance(response, Error):
            raise response.message
        else:
            return response

    def _get_pv_structure(self, pv_request):
        # TODO: do we need to take this or should we use self._request?
        path, _ = self._dict_to_path_value(pv_request)
        response = self._request_response(Get, path)
        # We are expected to provide all the levels in the dict. E.g. if
        # asked to get ["block", "attr", "value"], we should provide
        # {"attr": {"value": 32}}
        response_dict = response.value
        if self._field:
            # One level down
            path = path[1:]
        for endpoint in reversed(path):
            response_dict = {endpoint: response_dict}
        pv_structure = dict_to_pv_object(response_dict)
        return pv_structure

    def _pv_error_structure(self, exception):
        """Make an error structure in lieu of actually being able to raise"""
        error = Error(message=serialize_hook(exception)).to_dict()
        error.pop("id")
        return dict_to_pv_object(error)


class PvaGetImplementation(PvaImplementation):
    _pv_structure = None

    def getPVStructure(self):
        if self._pv_structure is None:
            try:
                self._pv_structure = self._get_pv_structure(self._request)
            except Exception as e:
                # TODO: pvaPy should really allow us to raise here
                self.log.exception("Bad get %s", self._request.toDict())
                # Can't raise an error, so send a bad structure as next best
                # thing
                self._pv_structure = self._pv_error_structure(e)
        return self._pv_structure

    def get(self):
        # No-op as getPvStructure gets values too
        pass


class PvaPutImplementation(PvaGetImplementation):
    def put(self, put_request):
        self.log.error("Put to %r value:\n%s", self._mri, put_request.toDict())
        self.getPVStructure()
        try:
            path, value = self._dict_to_path_value(put_request)
            self._request_response(Put, path, value=value)
        except Exception:
            self.log.exception(
                "Exception while putting to %r value:\n%s",
                self._mri, put_request.toDict())


class PvaRpcImplementation(PvaImplementation):

    def execute(self, args):
        try:
            if self._field:
                method_name = self._field
            else:
                method_name = self._request["method"]
            self.log.debug("Execute method %r of %r with args:\n%s",
                           self._mri, method_name, args.toDict())
            path = [method_name]
            parameters = strip_tuples(args.toDict(True))
            parameters.pop("typeid", None)
            response = self._request_response(Post, path, parameters=parameters)
            response_value = serialize_object(response.value)
            if isinstance(response_value, dict):
                pv_object = dict_to_pv_object(response_value)
            elif response_value is not None:
                # TODO: it might be better to just send the value without
                # the intermediate dictionary...
                pv_object = dict_to_pv_object({"return": response_value})
            else:
                # We need to return something, otherwise we get an error on the
                # client side:
                # Callable python service object must return instance of
                # PvObject.
                pv_object = pvaccess.PvObject({})
            self.log.debug("Return from method %r of %r:\n%s",
                           self._mri, method_name, pv_object.toDict())
            return pv_object
        except Exception as e:
            self.log.exception(
                "Exception while executing method of %r with args:\n%s",
                self._mri, args.toDict())
            error = self._pv_error_structure(e)
            return error


class PvaMonitorImplementation(PvaGetImplementation):
    def __init__(self, mri, controller, field, request):
        super(PvaMonitorImplementation, self).__init__(
            mri, controller, field, request)
        self._mu = pvaccess.MonitorServiceUpdater()
        self.getPVStructure()
        self._do_update = False
        path, _ = self._dict_to_path_value(self._request)
        request = Subscribe(path=[self._mri] + path, delta=True)
        request.set_callback(self._on_response)
        self._controller.handle_request(request)

    def getUpdater(self):
        return self._mu

    def _on_response(self, delta):
        """Handle Delta response to Subscribe

        Args:
            delta (Delta): The response
        """
        for change in delta.changes:
            path, _ = self._dict_to_path_value(self._request)
            if self._field:
                path = path[1:]
            field_path = ".".join(path + change[0])
            if field_path and self._pv_structure.hasField(field_path):
                new_value = value_for_pva_set(change[1])
                # Don't update on the first change if all is the same
                if not self._do_update:
                    if self._pv_structure[field_path] == new_value:
                        continue
                    else:
                        self._do_update = True
                self._pv_structure[field_path] = new_value
        if self._do_update is False:
            # First update gave us not changes, but unconditionally update from
            # now on
            self._do_update = True
        else:
            self._mu.update()
