import importlib
import logging
import time
import uuid
import datetime
from dataclay.communication.grpc.clients.ExecutionEnvGrpcClient import EEClient
from dataclay.communication.grpc.messages.common.common_messages_pb2 import LANG_PYTHON
from dataclay.exceptions.exceptions import DataClayException
from dataclay.paraver import trace_function
from dataclay.commonruntime.DataClayRuntime import DataClayRuntime
from dataclay.commonruntime.RuntimeType import RuntimeType
from dataclay.commonruntime.Settings import settings
from dataclay.serialization.lib.DeserializationLibUtils import deserialize_return  # Import after DataClayRuntime to avoid circular imports
from dataclay.serialization.lib.SerializationLibUtils import serialize_dcobj_with_data, serialize_params_or_return  # Import after DataClayRuntime to avoid circular imports
from dataclay.commonruntime.ExecutionGateway import ExecutionGateway
from dataclay.heap.ExecutionEnvironmentHeapManager import ExecutionEnvironmentHeapManager
from dataclay.loader.ExecutionObjectLoader import ExecutionObjectLoader
from dataclay.commonruntime.Runtime import threadLocal
from dataclay.communication.grpc.messages.logicmodule.logicmodule_messages_pb2 import GetMetadataByOIDRequest
from dataclay.util import Configuration
__author__ = 'Alex Barcelo <alex.barcelo@bsc.es>'
__copyright__ = '2015 Barcelona Supercomputing Center (BSC-CNS)'

logger = logging.getLogger(__name__)

current_milli_time = lambda: int(round(time.time() * 1000))


class ExecutionEnvironmentRuntime(DataClayRuntime):
    
    def __init__(self, theexec_env):
        DataClayRuntime.__init__(self)
            
        self.current_type = RuntimeType.exe_env
    
        """ Execution Environment using this runtime. """
        self.execution_environment = theexec_env
        
        """
        References hold by sessions. Resource note: Maximum size of this map is maximum number of objects allowed in EE x sessions.
        Also, important to think what happens if one single session is associated to two client threads? use case? 
        should we allow that?
        Must be thread-safe.
        """
        self.references_hold_by_sessions = dict() 
    
        """
        Sessions in quarantine. note: maximum size of this map is max number of sessions per EE: This map is needed to solve a race
        condition in Global Garbage collection (@see getReferenceCounting). 
        """
        self.quarantine_sessions = set()
        
        """
        Per each session, it's expiration date. This is used to control 'retained' objects from sessions in Garbage collection.
        Must be thread-safe.
        """
        self.session_expires_dates = dict()
    
        """
        Alias references found. TODO: this set is not cleaned. Important: modify this when design of removeAlias: we need to add
        'alias' as DataClayObject field since alias can be added dynamically to a volatile. Or check updateAliases function. Also,
        ensure removeAlias in LM notifies EE and avoid race condition remove alias but continue using object and GlobalGC clean it.
        Should be thread-safe.
        """
        self.alias_references = set()

    def initialize_runtime_aux(self):
        self.dataclay_heap_manager = ExecutionEnvironmentHeapManager(self)
        self.dataclay_object_loader = ExecutionObjectLoader(self)
        
    def is_exec_env(self):
        return True

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

    def get_or_new_instance_from_db(self, object_id, retry):
        """
        @postcondition: Get object from memory or database and WAIT in case we are still waiting for it to be persisted.
        @param object_id: ID of object to get or create 
        @param retry: indicates if we should retry and wait 
        """ 
        return self.dataclay_object_loader.get_or_new_instance_from_db(object_id, retry)

    def get_or_new_volatile_instance_and_load(self, object_id, metaclass_id, hint,
                                              obj_with_data, ifacebitmaps):
        """
        @postcondition: Get from Heap or create a new volatile in EE and load data on it.
        @param object_id: ID of object to get or create 
        @param metaclass_id: ID of class of the object (needed for creating it) 
        @param hint: Hint of the object, can be None. 
        @param obj_with_data: data of the volatile instance 
        @param ifacebitmaps: interface bitmaps
        """ 
        return self.dataclay_object_loader.get_or_new_volatile_instance_and_load(metaclass_id, object_id, hint, obj_with_data, ifacebitmaps)

    def add_volatiles_under_deserialization(self, volatiles):
        """
        @postcondition: Add volatiles provided to be 'under deserialization' in case any execution in a volatile is thrown 
        before it is completely deserialized. This is needed in case any deserialization depends on another (not for race conditions)
        like hashcodes or other similar cases.
        @param volatiles: volatiles under deserialization
        """
        pass
   
    def remove_volatiles_under_deserialization(self):
        """
        @postcondition: Remove volatiles under deserialization
        """
        pass 
    
    def load_object_from_db(self, instance, retry):
        """
        @postcondition: Load DataClayObject from Database
        @param instance: DataClayObject instance to fill
        @param retry: Indicates retry loading in case it is not in db.
        """
        return self.dataclay_object_loader.load_object_from_db(instance, retry)
    
    def get_hint(self):
        """
        @postcondition: Get hint of the current EE 
        @return Hint of current EE
        """
        return settings.environment_id
    
    def retain_in_heap(self, dc_object):
        """
        @postcondition: Retain in heap
        @param dc_object: Object to retain.
        """
        self.dataclay_heap_manager.retain_in_heap(dc_object)
        
    def flush_all(self):
        """
        @postcondition: Flush all objects in memory to disk.
        """
        self.dataclay_heap_manager.flush_all()
    
    def get_session_id(self):
        """
        @postcondition: Get Session ID associated to current thread 
        @return: Session ID associated to current thread 
        """
        return threadLocal.session_id
    
    def get_execution_environment(self):
        """
        @return: Return execution environment using this runtime 
        """ 
        return self.execution_environment

    def federate_object(self, object_id, ext_dataclay_id, recursive):
        logger.debug("[==FederateObject==] Starting federation of object %s with dataClay %s", object_id, ext_dataclay_id)
        session_id = self.execution_environment.thread_local_info.session_id
        self.ready_clients["@LM"].federate_object(session_id, object_id, ext_dataclay_id, recursive)

    @trace_function
    def store_object(self, instance):
        if not instance.is_persistent():
            raise RuntimeError("StoreObject should only be called on Persistent Objects. "
                               "Ensure to call make_persistent first")
    
        self.internal_store(instance, make_persistent=False)
    
    @trace_function
    def make_persistent(self, instance, alias, backend_id, recursive):
        if instance.is_persistent():
            logger.verbose("Trying to make persistent %r, which already is persistent. Ignoring", self)
            return
    
        # TODO: add support for that:
        if alias is not None:
            logger.warning("Server-side make_persistent with alias is not supported. Ignoring.")
    
        # TODO: add support for that:
        if backend_id is not None:
            logger.warning("Server-side EE pinning on make_persistent is not supported. Ignoring.")
    
        self.internal_store(instance, make_persistent=True)
    
    @trace_function
    def get_object_by_id(self, object_id):
        """Obtain a (thin) PersistentObject from the ObjectID
        :param object_id: The UUID of the Object
        :return: An Execution Class instance, typically with
        ExecuteRemoteImplementation as True
        """
            
        o = self.get_from_heap(object_id)
        if o is not None:
            return o
    
        full_name, namespace = self.ready_clients["@LM"].get_object_info(
            self.execution_environment.thread_local_info.session_id, object_id)
        logger.debug("Trying to import full_name: %s from namespace %s",
                     full_name, namespace)
    
        # Rearrange the division, full_name may include dots (and be nested)
        prefix, class_name = ("%s.%s" % (namespace, full_name)).rsplit('.', 1)
        m = importlib.import_module(prefix)
        klass = getattr(m, class_name)
    
        dataset_id = self.ready_clients["@LM"].get_object_dataset_id(
            self.execution_environment.thread_local_info.session_id, object_id)

        o = self.get_or_new_persistent_instance(object_id, klass.get_class_extradata().class_id, None)
        o.set_dataset_id(dataset_id)
        return o
    
    def new_replica(self, object_id, backend_id, recursive):
        logger.debug("Starting new replica from EE")
        session_id = self.execution_environment.thread_local_info.session_id
        return self.ready_clients["@LM"].new_replica(session_id, object_id, backend_id, recursive)

    def get_execution_environment_by_oid(self, object_id):
        try:
            obj = self.get_from_heap(object_id)
            if obj is not None:
                hint = obj.get_hint()
                if hint is not None:
                    logger.debug("Returning hint from heap object")
                    return hint
                else:
                    raise DataClayException("The object %s is not initialized well, hint missing or not exist", object_id)
            else:
                raise DataClayException("The object %s is not initialized", object_id)
        except DataClayException as e:
            # If the object is not initialized well trying to obtain location from metadata
            metadata = self.ready_clients["@LM"].get_metadata_by_oid(
                self.execution_environment.thread_local_info.session_id, object_id)
        
            logger.debug("Received the following MetaDataInfo for object %s: %s",
                        object_id, metadata)
            return iter(metadata.locations).next()

    def get_all_execution_environments_by_oid(self, object_id):
        try:
            metadata = self.ready_clients["@LM"].get_metadata_by_oid(
                self.execution_environment.thread_local_info.session_id, object_id)
        
            logger.debug("Received the following MetaDataInfo for object %s: %s",
                        object_id, metadata)
            return metadata.locations
        except Exception as e:
            logger.debug("Object %s has not metadata", object_id)
            obj = self.get_from_heap(object_id)
            if obj is not None:
                hint = obj.get_hint()
                if hint is not None:
                    logger.debug("Returning list with hint from heap object")
                    return [hint]
                else:
                    raise DataClayException("The object %s is not initialized well, hint missing or not exist", object_id)
            else:
                raise DataClayException("The object %s is not initialized", object_id)

    def get_execution_environments_info(self):
        
        return self.ready_clients["@LM"].get_execution_environments_info(self.execution_environment.thread_local_info.session_id,
                                                                         LANG_PYTHON)
    
    def get_by_alias(self, dclay_cls, alias):
        class_id = dclay_cls.get_class_extradata().class_id
    
        oid, hint = self.ready_clients["@LM"].get_object_from_alias(
            self.execution_environment.thread_local_info.session_id, class_id, alias)
        
        return self.get_object_by_id(oid)
    
    def move_object(self, instance, source_backend_id, dest_backend_id):
        client = self.ready_clients["@LM"]
        logger.debug("Moving object %r from %s to %s",
                     instance, source_backend_id, dest_backend_id)
    
        object_id = instance.get_object_id()
    
        client.move_objects(self.execution_environment.thread_local_info.session_id,
                            object_id, source_backend_id, dest_backend_id)
    
    def execute_implementation_aux(self, operation_name, instance, parameters, exeenv_id=None):

        if instance.is_loaded():
            # Client
            raise RuntimeError("Execute Implementation Aux commonruntime helper should only be called for non-loaded")
    
        object_id = instance.get_object_id()
        
        logger.debug("Calling execute_implementation inside EE for operation %s and object id %s", operation_name, object_id)
    
        # # ============================== PARAMS/RETURNS ========================== //
        # # Check if object is being deserialized (params/returns)
        # ToDo: volatiles under deserialization, needed in Python? (dgasull)
        
        # // === HINT === //
        thisExecEnv = settings.environment_id
        if exeenv_id is None:
            if instance.get_hint() is not None:
                exeenv_id = instance.get_hint()
                logger.debug("Using hint %s for object id %s", exeenv_id, object_id)
            else:
                logger.debug("Asking for EE of object with id %s", object_id)
                exeenv_id = self.get_execution_environment_by_oid(object_id)
        
        if exeenv_id == thisExecEnv:        
            logger.debug("Object execution is local")
    
            # Note that fat_instance tend to be the same as instance...
            # *except* if it is a proxy
            try:
                fat_instance = self.execution_environment.get_local_instance(
                    self.execution_environment.thread_local_info.session_id, object_id)
                # get_local_instance should indeed modify the same instance instance,
                # so @abarcelo is leaving the assert just in case
                assert instance is fat_instance, \
                    "A tiny mess with get_local_instance and heap management, check that"
                return self.execution_environment.internal_exec_impl(operation_name, fat_instance, parameters) 
            except Exception as e:
                return self.execution_environment.internal_exec_impl(operation_name, instance, parameters) 
        else:
            logger.debug("Object execution is not local")
    
            object_id = instance.get_object_id()
        
            # // === SERIALIZE PARAMETERS === //
            dcc_extradata = instance.get_class_extradata()
            metaclass_container = dcc_extradata.metaclass_container
            # iface_bm = self.execution_environment.thread_local_info.iface_bm
            operation = metaclass_container.get_operation_from_name(operation_name)

            serialized_params = serialize_params_or_return(
                params=parameters,
                iface_bitmaps=None,
                params_spec=operation.params,
                params_order=operation.paramOrder,
                hint_volatiles=None,
                runtime=self)  # No volatiles inside EEs
        
            # // === EXECUTE === //
            max_retry = 3
            executed = False
            for k in range(max_retry):
                try:
                    execution_client = self.ready_clients[exeenv_id]
                except KeyError:
                    exeenv = self.get_execution_environments_info()[exeenv_id] 
                    logger.verbose("Not found in cache ExecutionEnvironment {%s}! Starting it at %s:%d",
                                   exeenv_id, exeenv.hostname, exeenv.port)
                    execution_client = EEClient(exeenv.hostname, exeenv.port)
                    self.ready_clients[exeenv_id] = execution_client
        
                try:
                    ret = execution_client.ds_execute_implementation(
                        object_id,
                        operation.implementations[0].dataClayID,
                        self.execution_environment.thread_local_info.session_id,
                        serialized_params)
                    executed = True
                    break
                
                except DataClayException:
                    
                    """ prefer different location in case of failure """
                    metadata = self.ready_clients["@LM"].get_metadata_by_oid(
                        self.execution_environment.thread_local_info.session_id, object_id)
                    new_location = False
                    for loc in metadata.locations:
                        if loc != exeenv_id:
                            exeenv_id = loc
                            new_location = True
                    if not new_location: 
                        exeenv_id = iter(metadata.locations).next()

                    if logger.isEnabledFor(logging.DEBUG):
                        logger.debug("MetaDataInfo received for object: %s", object_id)
            
            if not executed:
                raise Exception("Server execution jump failed")
        
            logger.verbose("Result of operation named '%s' received", operation_name)
            if ret is None:
                return None
            else:
                return deserialize_return(ret,
                                            None,
                                            operation.returnType, self)
    
    #########################################
    # Helper functions, not commonruntime methods #
    #########################################
    
    def internal_store(self, instance, make_persistent=True):
        """Perform the storage (StoreObject call) for an instance.
    
        :param instance: The DataClayObject willing to be stored.
        :param make_persistent: Flag, True when DS_STORE_OBJECT should be called
        and False when DS_UPSERT_OBJECT is the method to be called.
        :return: A dictionary containing the classes for all stored objects.
    
        This function works for two main scenarios: the makePersistent one (in
        which the instance is not yet persistent) and the update (in which the
        instance is persistent).
    
        The return dictionary is the same in both cases, but note that the update
        should not use the provided instance for updating metadata to the LM.
        """
        logger.debug("Store procedure for instance %r", instance)
        client = self.ready_clients["@STORAGE"]
    
        pending_objs = [instance]
        stored_objects_classes = dict()
        serialized_objs = list()
        reg_infos = list()
        dataset_id = self.execution_environment.thread_local_info.dataset_id

        while pending_objs:
            current_obj = pending_objs.pop()

            dcc_extradata = current_obj.get_class_extradata()
            object_id = current_obj.get_object_id()

            if make_persistent:
                # Ignore already persistent objects
                if current_obj.is_persistent():
                    continue

                dcc_extradata = current_obj.get_class_extradata()
                infos = [object_id, dcc_extradata.class_id,
                         self.execution_environment.thread_local_info.session_id, dataset_id]
                reg_infos.append(infos)

            # This object will soon be persistent
            current_obj.set_persistent(True)
            current_obj.set_hint(settings.environment_id)
            # Just in case (should have been loaded already)
            current_obj.set_loaded(True)

            # First store since others OIDs are recursively created while creating MetaData
            if not object_id:
                if not make_persistent:
                    raise DataClayException("Objects should never be uuid-less for non-make_persistent use cases")
                object_id = uuid.uuid4()
                current_obj.set_object_id(object_id)
                current_obj.set_dataset_id(self.execution_environment.thread_local_info.dataset_id)
    
            logger.debug("Ready to make persistent object {%s} of class %s {%s}" % 
                         (object_id, dcc_extradata.classname, dcc_extradata.class_id))
    
            stored_objects_classes[object_id] = dcc_extradata.class_id
    
            # If we are not in a make_persistent, the dataset_id hint is null (?)
            serialized_objs.append(serialize_dcobj_with_data(
                current_obj, pending_objs, False, None, self, False))
    
        if make_persistent:
            lm_client = self.ready_clients["@LM"]
            lm_client.register_objects(reg_infos, settings.environment_id, None, None,
                                       LANG_PYTHON)

            client.ds_store_objects(self.execution_environment.thread_local_info.session_id, serialized_objs, False, None)
        else:
            client.ds_upsert_objects(self.execution_environment.thread_local_info.session_id, serialized_objs)

    def run_remote(self, object_id, backend_id, operation_name, value):
        try:
            execution_client = self.ready_clients[backend_id]
        except KeyError:
            exeenv = self.get_execution_environments_info()[backend_id]
            execution_client = EEClient(exeenv.hostname, exeenv.port)
            self.ready_clients[backend_id] = execution_client

        dcc_extradata = self.get_object_by_id(object_id).get_class_extradata()
        metaclass_container = dcc_extradata.metaclass_container
        operation = metaclass_container.get_operation_from_name(operation_name)
        value = serialize_params_or_return(
            params=(value,),
            iface_bitmaps=None,
            params_spec=operation.params,
            params_order=operation.paramOrder,
            hint_volatiles=None,
            runtime=self
        )

        ret = execution_client.ds_execute_implementation(object_id, operation.implementations[0].dataClayID, self.execution_environment.thread_local_info.session_id, value)

        if ret is not None:
            logger.trace("Execution return %s of type %s", ret, operation.returnType)
            return deserialize_return(ret, None, operation.returnType, self)
        
    def add_alias_reference(self, object_id):
        """
        @summary Add +1 reference due to a new alias.
        @param object_id ID of object with alias
        """
        self.alias_references.add(object_id)
        
    def add_session_reference(self, object_id):
        """
        @summary Add +1 reference associated to thread session
        @param object_id ID of object.
        """
        session_id = self.get_session_id()
        
        if not self.references_hold_by_sessions.has_key(object_id): 
            """ race condition: two objects creating set of sessions at same time """ 
            self.lock(object_id)
            try: 
                if not self.references_hold_by_sessions.has_key(object_id): 
                    session_refs = set() 
                    self.references_hold_by_sessions[object_id] = session_refs 
            finally:
                self.unlock(object_id)
        else:
            session_refs = self.references_hold_by_sessions.get(object_id)
        session_refs.add(session_id) 
        
        """ add expiration date of session if not present
        IMPORTANT: if CHECK_SESSION=FALSE then we use a default expiration date for all sessions
        In this case, sessions must be explicitly closed otherwise GC is never going to clean unused objects from sessions.
        Concurrency note: adding two times same expiration date is not a problem since exp. date is the same. We avoid locking.
        """
        if not self.session_expires_dates.has_key(session_id):
            if Configuration.CHECK_SESSION:
                """ TODO: implement session control in python """ 
            else:
                expiration_date = Configuration.NOCHECK_SESSION_EXPIRATION
                                    
            """
            // === concurrency note === //
            T1 is here, before put. This is a session that was already used and was restarted.
            T2 is in @getReferenceCounting and wants to remove session since it expired.
            What if T2 removes it after the put?
            Synchronization is needed to avoid this. It is not a big penalty if session expiration date was already added.
            """
            self.lock(session_id)  # Use same locking system for object ids. 
            try: 
                self.session_expires_dates[session_id] = expiration_date
            finally: 
                self.unlock(session_id)
        
    def close_session_in_ee(self, session_id):
        """
        @summary Close session in EE. Subtract session references for GC.
        @param session_id ID of session closing.
        """
        
        logger.debug("[==DGC==] Closing session %s" % str(session_id))

        """ Closing session means set expiration date to now """
        self.session_expires_dates[session_id] = datetime.datetime.now()
    
    def get_retained_references(self):
        """
        @summary Get retained refs by this EE
        @return Retained refs (alias, sessions, ...)
        """
        logger.debug("Getting retained references")
        retained_refs = list() 
        
        """ memory references """
        retained_refs.extend(self.dataclay_heap_manager.get_object_ids_retained())
        logger.debug("Obtained retained references in memory: %s " % str(len(retained_refs)))

        """ session references """ 
        now = datetime.datetime.now()

        sessions_to_close = set()
        for oid in self.references_hold_by_sessions.keys():  # use keys as copy to avoid concurrency problems
            sessions_of_obj = self.references_hold_by_sessions.get(oid)
            logger.debug("[==DGC==] Object %s is retained by sessions %s" % (oid, str(sessions_of_obj)))
            """ create a copy of the list to avoid modification issues while iterating and concurrence problems """
            for cur_session in list(sessions_of_obj):
                
                """ check session expired """
                """
                ==== session counting design - Race condition ==== //
                Race condition: object is send between two nodes and they are both notifying 0 references. This is not
                solved using quarantine in SL since during quarantine period they could do the same and always send 0: while one is
                notifying 0, the other keeps the object, and send to the other before notifying 0.
                In order to avoid this, since session reference is added every time we communicate
                (even between nodes! not only client - node)
                we do NOT remove session reference till GGC asks TWO times
        
                Explicit closes of sessions set expire date to "now" but user can restart a session
                so, even if session is in quarantine, we must check date.
                """
                session_expired = False
                expired_date = self.session_expires_dates.get(cur_session)
                print expired_date
                if expired_date is not None and now > expired_date:
                    if cur_session in self.quarantine_sessions:
                        # Session is actually removed 
                        session_expired = True
                        
                        """ check again expiration date to see if it is expired. If expired, remove. """
                        cur_expired_date = self.session_expires_dates.get(cur_session)
                        if cur_expired_date is not None and now > cur_expired_date:
                            """
                            do not remove expiration date from session till there is no objects in that session
                            add it to sessions to close after all processing"""
                            sessions_to_close.add(cur_session)
                            
                    else:
                        self.quarantine_sessions.add(cur_session)
                elif expired_date is not None and now < expired_date:
                    # check if session was in quarantine: if so, remove it from there (session restart)
                    if cur_session in self.quarantine_sessions:
                        self.quarantine_sessions.remove(cur_session)
                        
                if session_expired:
                    """ close session """ 
                    sessions_of_obj.remove(cur_session)
                    
                    """
                    // === concurrency note === //
                    when should we remove an entry in the references_hold_by_sessions map?
                    1 - when no session is using the object
                    2 - when object is not in memory
                    so, we check both here and we remove it if needed:
                    TODO: what if after if, it is added?
                    """
                    logger.debug("Session %s expired" % str(cur_session))
                    if not self.dataclay_heap_manager.exists_in_heap(oid) and len(sessions_of_obj) == 0:
                        logger.debug("Removing session reference for oid %s" % str(oid))
                        for oid, oid_ref in self.references_hold_by_sessions.iteritems():
                            oid_ref.discard(cur_session)  # do not raise key error if not found
                        print self.references_hold_by_sessions

                else:
                    retained_refs.append(oid)
        
        """ check closed sessions """ 
        """ Remove all expired sessions if, and only if, there is no object retained by it. 
        TODO: improve this implementation."""
        for session_to_close in sessions_to_close:
            obj_using_session = False
            for sessions_of_obj in self.references_hold_by_sessions.values():
                if session_to_close in sessions_of_obj:
                    obj_using_session = True
                    break
                
            if not obj_using_session:
                del self.session_expires_dates[session_to_close]
        
        logger.debug("Retained references %s" % str(retained_refs))
        return retained_refs
