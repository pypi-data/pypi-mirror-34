"""Initialization and finalization of dataClay client API.

The `init` and `finish` functions are availble through the
dataclay.api package.
"""

import importlib
import logging
import random
import uuid
import time
from logging import TRACE

from grpc import RpcError
from dataclay.commonruntime.ExecutionGateway import ExecutionGateway
from dataclay.commonruntime.Settings import settings
from dataclay.communication.grpc.clients.ExecutionEnvGrpcClient import EEClient
from dataclay.communication.grpc.clients.LogicModuleGrpcClient import LMClient
from dataclay.communication.grpc.messages.common.common_messages_pb2 import LANG_PYTHON
from dataclay.exceptions.exceptions import DataClayException
from dataclay.serialization.lib.DeserializationLibUtils import deserialize_return
from dataclay.serialization.lib.SerializationLibUtils import serialize_params_or_return, serialize_dcobj_with_data
from dataclay.commonruntime.DataClayRuntime import DataClayRuntime
from dataclay.commonruntime.RuntimeType import RuntimeType
from dataclay.heap.ClientHeapManager import ClientHeapManager
from dataclay.loader.ClientObjectLoader import ClientObjectLoader

# Sentinel-like object to catch some typical mistakes
UNDEFINED_LOCAL = object()


class ClientRuntime(DataClayRuntime):
    
    current_type = RuntimeType.client

    def __init__(self):
        
        DataClayRuntime.__init__(self)
        
    def initialize_runtime_aux(self):
        self.dataclay_heap_manager = ClientHeapManager(self)
        self.dataclay_object_loader = ClientObjectLoader(self)
        
    def is_exec_env(self):
        return False

    def federate_object(self, object_id, ext_dataclay_id, recursive):
        self.logger.debug("[==FederateObject==] Starting federation of object %s with dataClay %s", object_id, ext_dataclay_id)
        session_id = settings.current_session_id
        self.ready_clients["@LM"].federate_object(session_id, object_id, ext_dataclay_id, recursive)

    def get_object_by_id(self, object_id, class_id=None, hint=None):
        # Note that this method requires several calls to the LogicModule
        # (getObjectInfo). If the class_id is available, like the typical response
        # or parameter serialization, it is better to use the new_instance method.
        o = self.get_from_heap(object_id)
        if o is not None:
            return o

        if not class_id:
            full_name, namespace = self.ready_clients["@LM"].get_object_info(
                settings.current_session_id, object_id)
            self.logger.debug("Trying to import full_name: %s from namespace %s",
                         full_name, namespace)
    
            # Rearrange the division, full_name may include dots (and be nested)
            prefix, class_name = ("%s.%s" % (namespace, full_name)).rsplit('.', 1)
            m = importlib.import_module(prefix)
            klass = getattr(m, class_name)
            class_id = klass.get_class_extradata().class_id

        o = self.get_or_new_persistent_instance(object_id, class_id, hint)
        return o
    
    def get_or_new_persistent_instance(self, object_id, metaclass_id, hint):
        """
        @postcondition: Check if object with ID provided exists in dataClay heap. If so, return it. Otherwise, create it.
        @param object_id: ID of object to get or create 
        @param metaclass_id: ID of class of the object (needed for creating it) 
        @param hint: Hint of the object, can be None. 
        """ 
        if metaclass_id is None:
            metadata = self.ready_clients["@LM"].get_metadata_by_oid(
                settings.current_session_id, object_id)
            metaclass_id = metadata.metaclassID

        return self.dataclay_object_loader.get_or_new_persistent_instance(metaclass_id, object_id, hint)
    
    def new_replica(self, object_id, backend_id, recursive):
        self.logger.debug("Starting new replica")
        session_id = settings.current_session_id
        return self.ready_clients["@LM"].new_replica(session_id, object_id, backend_id, recursive)
    
    def new_version(self, object_id, backend_id):
        self.logger.debug("Starting new version")
        session_id = settings.current_session_id
        return self.ready_clients["@LM"].new_version(session_id, object_id, backend_id)
    
    def consolidate_version(self, version_info):
        self.logger.debug("Starting consolidate version")
        session_id = settings.current_session_id
        return self.ready_clients["@LM"].consolidate_version(session_id, version_info)
    
    def get_execution_environment_by_oid(self, object_id):
        try:
            obj = self.get_from_heap(object_id)
            if obj is not None:
                hint = obj.get_hint()
                if hint is not None:
                    self.logger.debug("Returning hint from heap object")
                    return hint
                else:
                    raise DataClayException("The object %s is not initialized well, hint missing or not exist", object_id)
            else:
                raise DataClayException("The object %s is not initialized", object_id)
        except DataClayException as e:
            # If the object is not initialized well trying to obtain location from metadata
            metadata = self.ready_clients["@LM"].get_metadata_by_oid(
                settings.current_session_id, object_id)
        
            self.logger.debug("Received the following MetaDataInfo for object %s: %s",
                        object_id, metadata)
            return iter(metadata.locations).next()

    def get_all_execution_environments_by_oid(self, object_id):
        try:
            metadata = self.ready_clients["@LM"].get_metadata_by_oid(
                settings.current_session_id, object_id)
        
            self.logger.debug("Received the following MetaDataInfo for object %s: %s",
                        object_id, metadata)
            return metadata.locations
        except Exception as e:
            self.logger.debug("Object %s has not metadata", object_id)
            obj = self.get_from_heap(object_id)
            if obj is not None:
                hint = obj.get_hint()
                if hint is not None:
                    self.logger.debug("Returning list with hint from heap object")
                    return [hint]
                else:
                    raise DataClayException("The object %s is not initialized well, hint missing or not exist", object_id)
            else:
                raise DataClayException("The object %s is not initialized", object_id)

    def get_execution_environments_info(self):
        ee_info_map = self.ready_clients["@LM"].get_execution_environments_info(
            settings.current_session_id, LANG_PYTHON)

        if self.logger.isEnabledFor(TRACE):
            n = len(ee_info_map)
            self.logger.trace("Response of ExecutionEnvironmentsInfo returned #%d ExecutionEnvironmentsInfo", n)
            for i, (ee_id, ee_info) in enumerate(ee_info_map.iteritems(), 1):
                self.logger.trace("ExecutionEnvironments info (#%d/%d): %s\n%s", i, n, ee_id, ee_info)

        return ee_info_map
    
    def get_by_alias(self, dclay_cls, alias):
        class_id = dclay_cls.get_class_extradata().class_id
    
        oid, hint = self.ready_clients["@LM"].get_object_from_alias(
            settings.current_session_id, class_id, alias)

        return self.get_object_by_id(oid, class_id)
    
    def delete_alias(self, dclay_cls, alias):
        class_id = dclay_cls.get_class_extradata().class_id
        instance = self.get_by_alias(dclay_cls, alias)
        instance.set_has_alias(False)

        self.ready_clients["@LM"].delete_alias(settings.current_session_id, class_id, alias)
        self.logger.debug("Removing from cache alias %s of class %s", alias, dclay_cls)        
        del self.alias_cache[(alias, class_id)]

    def store_object(self, instance):
        raise RuntimeError("StoreObject can only be used from the ExecutionEnvironment")
    
    def move_object(self, instance, source_backend_id, dest_backend_id, recursive):
        self.logger.debug("Moving object %r from %s to %s",
                     instance, source_backend_id, dest_backend_id)
    
        object_id = instance.get_object_id()
    
        self.ready_clients["@LM"].move_object(settings.current_session_id, object_id,
                            source_backend_id, dest_backend_id, recursive)
    
    def make_persistent(self, instance, alias, backend_id, recursive):
        client = self.ready_clients["@LM"]
        self.logger.debug("Starting make persistent object for instance %s with id %s", instance,
                     instance.get_object_id())
    
        reg_infos = list()
        update_alias = False
        object_id_to_have_alias = None

        if instance.is_persistent():
            if self.current_type == RuntimeType.exe_env:
                only_register = True
                self.logger.debug("Object need to be only registered")
            else:
                # TODO: Before was return.. now?
                self.logger.verbose("Trying to make persistent %r, which already is persistent. Ignoring", self)
                
        if backend_id is UNDEFINED_LOCAL:
            # This is a commonruntime end user pitfall,
            # @abarcelo thinks that it is nice
            # (and exceptionally detailed) error
            raise RuntimeError("""
    You are trying to use dataclay.api.LOCAL but either:
      - dataClay has not been initialized properly
      - LOCAL has been wrongly imported.
    
    Be sure to use LOCAL with:
    
    from dataclay import api
    
    and reference it with `api.LOCAL`
    
    Refusing the temptation to guess.""")
    
        if backend_id is None:
            # If no execution environment specified select it randomly
            backend_id = random.choice(self.get_execution_environments_info().keys())
        
        instance._set_has_alias_internal(alias is not None)
        if alias is not None:
            update_alias = True
            object_id_to_have_alias = instance.get_object_id()

        self.logger.verbose("ExecutionEnvironment chosen for MakePersistent is: %s", backend_id)
    
        hint = backend_id
    
        ignore_user_types = not recursive
        serialized_objs = list()
        persisted_object = list()
        pending_objs = list()
        datasets_specified = dict()
    
        # OidsCreated: OIDS created while serializing metadata or the objects found
        # objs_already_persistent: All objects that are already persistent
        objs_already_persistent = list()
    
        pending_objs.append(instance)
    
        while pending_objs:
            current_obj = pending_objs.pop()
    
            object_id = current_obj.get_object_id()
            dataset_id = current_obj.get_dataset_id()
    
            dcc_extradata = current_obj.get_class_extradata()
            class_id = dcc_extradata.class_id
    
            if class_id is None:
                raise RuntimeError("ClassID is None. Stubs are not used properly.")
    
            # Ignore already persistent objects
            if current_obj.is_persistent() or object_id in objs_already_persistent:
                continue
    
            # First store since others OIDs are recursively created while creating MetaData
            if not object_id:
                object_id = uuid.uuid4()
                current_obj.set_object_id(object_id)
    
            # Store dataset id in the datasets dict
            if dataset_id is not None:
                datasets_specified[object_id] = dataset_id
            else:
                # And assume that it will be put to the dataset_for_store accordingly to the session
                dataset_id = client.get_dataset_id(settings.current_id,
                                                   settings.current_credential,
                                                   settings.dataset_for_store)
                datasets_specified[object_id] = dataset_id
                
            objs_already_persistent.append(object_id)
    
            # During serialization, ObjectIDs of found objects can be set since it is
            # necessary for serializing MetaData of each object!
            # Serialize the objects to make persistent
            self.logger.verbose("Adding object to make persistent call: instance %s", current_obj)
    
            serialized_objs.append(
                serialize_dcobj_with_data(current_obj, pending_objs,
                                          ignore_user_types, hint, self, False)
            )
            persisted_object.append(object_id)
    
            infos = [object_id, class_id,
                     settings.current_session_id, dataset_id]
    
            if infos not in reg_infos:
                reg_infos.append(infos)
                
            # ToDo: Check it
            # This object will soon be persistent
            current_obj.set_persistent(True)
            current_obj.set_loaded(False)

        objs_to_register = list()
        for reg_info in serialized_objs:
            objs_to_register.append(reg_info[0])

        for reg_obj in reg_infos:
            if reg_obj[0] == instance.get_object_id():
                self.logger.debug(
                    "[==MakePersistent==] Setting flag persistent from registerObjects: %s", reg_obj)
                # ToDo: Check it
                instance.set_persistent(True)

        if alias is not None:
            self.logger.debug("Making persistent object %s with alias %s and associated objects: %s",
                            instance.get_object_id(),
                            alias, objs_to_register)

        else:
            self.logger.debug("Making persistent object %s and associated objects: %s",
                            instance.get_object_id(),
                            objs_to_register)

        client.make_persistent(session_id=settings.current_session_id,
                                dest_backend_id=backend_id,
                                serialized_objects=serialized_objs,
                                ds_specified=datasets_specified,
                                object_to_have_alias=object_id_to_have_alias,
                                alias=alias)
        
        if update_alias:
            
            client.add_alias(session_id=settings.current_session_id,
                                metaclass_id=instance.get_class_extradata().class_id,
                                object_id_to_have_alias=instance.get_object_id(),
                                dest_backend_id=backend_id,
                                alias=alias)
            
            self.logger.debug("Adding to cache object with alias %s and oid %s",
                        alias, instance.get_object_id())
            self.alias_cache[(alias, instance.get_class_extradata().class_id)] = (instance.get_object_id(), backend_id)

        self.logger.verbose("[==MakePersistent==] Make Persistent finished of object = %s", instance)
        return backend_id

    def execute_implementation_aux(self, operation_name, instance, parameters, exeenv_id=None):
        stub_info = instance.get_class_extradata().stub_info
        implementation_stub_infos = stub_info.implementations
        object_id = instance.get_object_id()
        
        self.logger.verbose("Calling operation '%s' in object with ID %s", operation_name, object_id)
        self.logger.debug("Call is being done into %r with #%d parameters",
                          instance, len(parameters))
        
        # # Check if object is being deserialized (params/returns)
        # ToDo: volatiles under deserialization, needed in Python? (dgasull)
        
        # // === HINT === //
        self.logger.trace("Provided hint = %s", exeenv_id)
        exeenv_id = exeenv_id or instance.get_hint()
        self.logger.verbose("Using hint = %s", exeenv_id)

        # // === DEFAULT EXECUTION LOCATION === // CURRENTLY NOT SUPPORTED 
        # ToDo: remove in java (dgasull)
        
        # // === HASHCODE EXECUTION LOCATION === //
        # ToDo: modify make persistent to use hashcode instead of random
        if exeenv_id is None:
            exeenv_id = self.get_execution_environment_by_oid(object_id)
            self.logger.verbose("ExecutionEnvironmentID obtained for execution = %s", exeenv_id)
    
        # // === SERIALIZE PARAMETERS === //
        serialized_params = serialize_params_or_return(
            params=parameters,
            iface_bitmaps=None,
            params_spec=implementation_stub_infos[operation_name].parameters,
            params_order=implementation_stub_infos[operation_name].paramsOrder,
            hint_volatiles=exeenv_id,
            runtime=self)
        
        remote_impl = [implementation_stub_infos[operation_name].remoteImplID,
                       implementation_stub_infos[operation_name].contractID,
                       implementation_stub_infos[operation_name].interfaceID]
    
        # // === EXECUTE === //
        max_retry = 3
        last_exception = None
        for k in range(max_retry):
            try:
                self.logger.verbose("Obtaining API for remote execution in %s ", exeenv_id)
                execution_client = self.ready_clients[exeenv_id]
            except KeyError:
                exeenv = self.get_execution_environments_info()[exeenv_id] 
                self.logger.debug("Not found in cache ExecutionEnvironment {%s}! Starting it at %s:%d",
                               exeenv_id, exeenv.hostname, exeenv.port)
                execution_client = EEClient(exeenv.hostname, exeenv.port)
                self.ready_clients[exeenv_id] = execution_client
    
            try:
                self.logger.verbose("Calling remote EE %s ", exeenv_id)
                ret = execution_client.ds_execute_implementation(
                    object_id,
                    remote_impl[0],
                    settings.current_session_id,
                    serialized_params)
                break
            
            except (DataClayException, RpcError) as dce:
                last_exception = dce
                self.logger.debug("Exception dataclay during execution. Retrying...")
                self.logger.debug(str(dce))
                metadata = self.ready_clients["@LM"].get_metadata_by_oid(
                    settings.current_session_id, object_id)
                new_location = False
                for loc in metadata.locations:
                    self.logger.debug("Found location %s" % str(loc))
                    if loc != exeenv_id:
                        exeenv_id = loc
                        self.logger.debug("Found different location %s" % str(loc))
                        new_location = True
                        break
                    
                if not new_location: 
                    exeenv_id = iter(metadata.locations).next()
                
                self.logger.debug("Retry in location %s" % str(exeenv_id))
     
                if self.logger.isEnabledFor(logging.DEBUG):
                    self.logger.debug("MetaDataInfo received for object: %s", object_id)
        else:
            raise last_exception
    
        self.logger.verbose("Result of operation named '%s' received", operation_name)
    
        if ret is None:
            return None
        else:
            return deserialize_return(
                ret, None, implementation_stub_infos[operation_name].returnType, self)

    def run_remote(self, object_id, backend_id, operation_name, value):
        try:
            execution_client = self.ready_clients[backend_id]
        except KeyError:
            exeenv = self.get_execution_environments_info()[backend_id]
            execution_client = EEClient(exeenv.hostname, exeenv.port)
            self.ready_clients[backend_id] = execution_client
        dcc_extradata = self.get_object_by_id(object_id).get_class_extradata()
        stub_info = dcc_extradata.stub_info
        implementation_stub_infos = stub_info.implementations
        operation = implementation_stub_infos[operation_name]

        value = serialize_params_or_return(
            params=(value,),
            iface_bitmaps=None,
            params_spec=operation.parameters,
            params_order=operation.paramsOrder,
            hint_volatiles=None,
            runtime=self
        )

        ret = execution_client.ds_execute_implementation(object_id, operation.remoteImplID, settings.current_session_id, value)

        if ret is not None:
            return deserialize_return(ret, None, operation.returnType, self)

    def call_execute_to_external_DC(self, instance, params, operation_name, dc_info):
        
        volatile_parameters_being_send = set()
        executed = False
        num_misses = 0
        stub_info = instance.get_class_extradata().stub_info
        implementation_stub_infos = stub_info.implementations
        operation = implementation_stub_infos[operation_name]
        dataclay_id = dc_info.dcID
        # === SERIALIZE PARAMETERS === 
        # Between DC - DC , ifaceBitMaps = null
        serialized_params = serialize_params_or_return(
            params=params,
            iface_bitmaps=None,
            params_spec=implementation_stub_infos[operation_name].parameters,
            params_order=implementation_stub_infos[operation_name].paramsOrder,
            hint_volatiles=instance.get_hint(),
            runtime=self)

        if serialized_params is not None and serialized_params[3] is not None:
            for param in serialized_params[3]:
                volatile_parameters_being_send.add(param[0])
        
        # TODO: DEBUG LOGS

        # TODO: Populate impl_info
        impl_info = list()

        while not executed and num_misses < 5:  # TODO: num_misses < Configuration.flags....
            try:
                self.logger.debug("[==JUMP==] Request execution to external dataClay named %s for object %s"
                , dc_info.name, instance.get_object_id())
                lm_client = self.ready_clients[dataclay_id]   
                
            except KeyError:
                lm_client = LMClient(dc_info.host, dc_info.port)
                
                self.ready_clients[dataclay_id] = lm_client

            try:
                ser_result = lm_client.execute_on_federated_object(dataclay_id, instance.get_object_id(), impl_info, serialized_params)
                executed = True
            except Exception:
                is_race_condition = False
                if serialized_params is not None and serialized_params[4] is not None:
                    for param in serialized_params[4]:
                        if param[0] in volatile_parameters_being_send:
                            is_race_condition = True
                            time.sleep(3)
                        break
            if not is_race_condition:
                num_misses += 1
        
        if num_misses > 0 and serialized_params is not None:
            for volatil in serialized_params[3]:
                volatile_parameters_being_send.remove(volatil[0])
        if not executed:
            self.logger.error("Trying to execute remotely object %s of class %s but something went wrong. Maybe the object is still not stored  (in case of asynchronous makepersistent) and waiting time is not enough. Maybe the object does not exist anymore due to a remove. Or Maybe an exception happened in the server and the call failed.",
            instance.get_object_id(),
            instance.get_class_extradata().name)

            raise RuntimeError("[dataClay] ERROR: Trying to execute remotely object  but something went wrong. Maybe the object is still not stored (in case of asynchronous makepersistent) and waiting time is not enough. Maybe the object does not exist anymore due to a remove. Or Maybe an exception happened in the server and the call failed.")
        
        return deserialize_return(serialized_params, None, operation.returnType, self)
    
    def close_session(self):
         self.ready_clients["@LM"].close_session(settings.current_session_id)
