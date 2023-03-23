schema = {
    "organization": {
        "o": ("String", True, True),
    },
    "GLUE2Entity": {
        "dn": ("DN_t", True, True),
        "objectClass": ("ObjectClass", False, True),
        "GLUE2EntityCreationTime": ("DateTime_t", True, False),
        "GLUE2EntityValidity": ("UInt64", True, False),
    },
    "GLUE2Group": {
        "GLUE2GroupID": ("URI", True, False),
        "GLUE2GroupName": ("URI", True, False),
    },
    "GLUE2Extension": {
        "GLUE2ExtensionLocalID": ("LocalID_t", True, True),
        "GLUE2ExtensionKey": ("String", True, True),
        "GLUE2ExtensionValue": ("String", True, True),
    },
    "GLUE2Location": {
        "GLUE2LocationID": ("URI", True, True),
        "GLUE2LocationAddress": ("String", True, False),
        "GLUE2LocationPlace": ("String", True, False),
        "GLUE2LocationCountry": ("String", True, False),
        "GLUE2LocationPostCode": ("String", True, False),
        "GLUE2LocationLatitude": ("Real32", True, False),
        "GLUE2LocationLongitude": ("Real32", True, False),
        "GLUE2LocationDomainForeignKey": ("URI", False, False),
    },
    "GLUE2Contact": {
        "GLUE2ContactID": ("URI", True, True),
        "GLUE2ContactName": ("String", True, False),
        "GLUE2ContactDetail": ("URI", True, True),
        "GLUE2ContactType": ("ContactType_t", True, True),
        "GLUE2ContactDomainForeignKey": ("URI", True, False),
    },
    "GLUE2Domain": {
        "GLUE2DomainID": ("URI", True, True),
        "GLUE2DomainName": ("String", True, False),
        "GLUE2DomainDescription": ("String", True, False),
        "GLUE2DomainWWW": ("URL", False, False),
    },
    "GLUE2AdminDomain": {
        "GLUE2AdminDomainDistributed": ("ExtendedBoolean_t", True, False),
        "GLUE2AdminDomainOwner": ("String", False, False),
        "GLUE2AdminDomainAdminDomainForeignKey": ("URI", False, False),
    },
    "GLUE2UserDomain": {
        "GLUE2UserDomainLevel": ("UInt32", True, False),
        "GLUE2UserDomainUserManager": ("URI", False, False),
        "GLUE2UserDomainMember": ("String", False, False),
        "GLUE2UserDomainUserDomainForeignKey": ("URI", False, False),
    },
    "GLUE2Service": {
        "GLUE2ServiceID": ("URI", True, True),
        "GLUE2ServiceCapability": ("Capability_t", False, False),
        "GLUE2ServiceType": ("ServiceType_t", True, True),
        "GLUE2ServiceQualityLevel": ("QualityLevel_t", True, True),
        "GLUE2ServiceStatusInfo": ("URL", False, False),
        "GLUE2ServiceComplexity": ("String", True, False),
        "GLUE2ServiceAdminDomainForeignKey": ("URI", True, True),
        "GLUE2ServiceServiceForeignKey": ("URI", True, False),
    },
    "GLUE2Endpoint": {
        "GLUE2EndpointID": ("URI", True, True),
        "GLUE2EndpointURL": ("URL", True, True),
        "GLUE2EndpointCapability": ("Capability_t", False, False),
        "GLUE2EndpointTechnology": ("EndpointTechnology_t", True, False),
        "GLUE2EndpointInterfaceName": ("InterfaceName_t", True, True),
        "GLUE2EndpointInterfaceVersion": ("String", True, False),
        "GLUE2EndpointInterfaceExtension": ("URI", False, False),
        "GLUE2EndpointWSDL": ("URL", False, False),
        "GLUE2EndpointSupportedProfile": ("URI", False, False),
        "GLUE2EndpointSemantics": ("URL", False, False),
        "GLUE2EndpointImplementor": ("String", True, False),
        "GLUE2EndpointImplementationName": ("String", True, False),
        "GLUE2EndpointImplementationVersion": ("String", True, False),
        "GLUE2EndpointQualityLevel": ("QualityLevel_t", True, True),
        "GLUE2EndpointHealthState": ("EndpointHealthState_t", True, True),
        "GLUE2EndpointHealthStateInfo": ("String", False, False),
        "GLUE2EndpointServingState": ("ServingState_t", True, True),
        "GLUE2EndpointStartTime": ("DateTime_t", True, False),
        "GLUE2EndpointIssuerCA": ("DN_t", True, False),
        "GLUE2EndpointTrustedCA": ("DN_t", False, False),
        "GLUE2EndpointDowntimeAnnounce": ("DateTime_t", True, False),
        "GLUE2EndpointDowntimfeStart": ("DateTime_t", True, False),
        "GLUE2EndpointDowntimeEnd": ("DateTime_t", True, False),
        "GLUE2EndpointDowntimeInfo": ("String", True, False),
        "GLUE2EndpointServiceForeignKey": ("URI", True, False),
    },
    "GLUE2Policy": {
        "GLUE2PolicyID": ("URI", True, True),
        "GLUE2PolicyScheme": ("PolicyScheme_t", True, True),
        "GLUE2PolicyRule": ("String", False, True),
        "GLUE2PolicyUserDomainForeignKey": ("URI", False, False),
        "GLUE2PolicyEndpointForeignKey": ("URI", True, False),
    },
    "GLUE2AccessPolicy": {},
    "GLUE2MappingPolicy": {},
    "GLUE2Share": {
        "GLUE2ShareID": ("URI", True, True),
        "GLUE2ShareDescription": ("String", True, False),
        "GLUE2ShareServiceForeignKey": ("URI", True, False),
    },
    "GLUE2Manager": {
        "GLUE2ManagerID": ("URI", True, True),
        "GLUE2ManagerProductName": ("String", True, True),
        "GLUE2ManagerProductVersion": ("String", True, False),
        "GLUE2ManagerServiceForeignKey": ("URI", True, False),
    },
    "GLUE2Resource": {
        "GLUE2ResourceID": ("URI", True, True),
        "GLUE2ResourceManagerForeignKey": ("URI", True, False),
    },
    "GLUE2Activity": {
        "GLUE2ActivityID": ("URI", True, True),
        "GLUE2ActivityUserDomainForeignKey": ("URI", True, False),
        "GLUE2ActivityEndpointForeignKey": ("URI", True, False),
        "GLUE2ActivityShareForeignKey": ("URI", True, False),
        "GLUE2ActivityResourceForeignKey": ("URI", True, False),
        "GLUE2ActivityActivityForeignKey": ("URI", False, False),
    },
    "GLUE2ComputingService": {
        "GLUE2ComputingServiceTotalJobs": ("UInt32", True, False),
        "GLUE2ComputingServiceRunningJobs": ("UInt32", True, False),
        "GLUE2ComputingServiceWaitingJobs": ("UInt32", True, False),
        "GLUE2ComputingServiceStagingJobs": ("UInt32", True, False),
        "GLUE2ComputingServiceSuspendedJobs": ("UInt32", True, False),
        "GLUE2ComputingServicePreLRMSWaitingJobs": ("UInt32", True, False),
    },
    "GLUE2ComputingEndpoint": {
        "GLUE2ComputingEndpointStaging": ("Staging_t", True, False),
        "GLUE2ComputingEndpointJobDescription": ("JobDescription_t", False, False),
        "GLUE2ComputingEndpointTotalJobs": ("UInt32", True, False),
        "GLUE2ComputingEndpointRunningJobs": ("UInt32", True, False),
        "GLUE2ComputingEndpointWaitingJobs": ("UInt32", True, False),
        "GLUE2ComputingEndpointStagingJobs": ("UInt32", True, False),
        "GLUE2ComputingEndpointSuspendedJobs": ("UInt32", True, False),
        "GLUE2ComputingEndpointPreLRMSWaitingJobs": ("UInt32", True, False),
        # 'GLUE2ComputingEndpointComputingServiceForeignKey': ('URI', True, True),
    },
    "GLUE2ComputingShare": {
        "GLUE2ComputingShareMappingQueue": ("String", True, False),
        "GLUE2ComputingShareMaxWallTime": ("UInt64", True, False),
        "GLUE2ComputingShareMaxMultiSlotWallTime": ("UInt64", True, False),
        "GLUE2ComputingShareMinWallTime": ("UInt64", True, False),
        "GLUE2ComputingShareDefaultWallTime": ("UInt64", True, False),
        "GLUE2ComputingShareMaxCPUTime": ("UInt64", True, False),
        "GLUE2ComputingShareMaxTotalCPUTime": ("UInt64", True, False),
        "GLUE2ComputingShareMinCPUTime": ("UInt64", True, False),
        "GLUE2ComputingShareDefaultCPUTime": ("UInt64", True, False),
        "GLUE2ComputingShareMaxTotalJobs": ("UInt32", True, False),
        "GLUE2ComputingShareMaxRunningJobs": ("UInt32", True, False),
        "GLUE2ComputingShareMaxWaitingJobs": ("UInt32", True, False),
        "GLUE2ComputingShareMaxPreLRMSWaitingJobs": ("UInt32", True, False),
        "GLUE2ComputingShareMaxUserRunningJobs": ("UInt32", True, False),
        "GLUE2ComputingShareMaxSlotsPerJob": ("UInt32", True, False),
        "GLUE2ComputingShareMaxStageInStreams": ("UInt32", True, False),
        "GLUE2ComputingShareMaxStageOutStreams": ("UInt32", True, False),
        "GLUE2ComputingShareSchedulingPolicy": ("SchedulingPolicy_t", True, False),
        "GLUE2ComputingShareMaxMainMemory": ("UInt64", True, False),
        "GLUE2ComputingShareGuaranteedMainMemory": ("UInt64", True, False),
        "GLUE2ComputingShareMaxVirtualMemory": ("UInt64", True, False),
        "GLUE2ComputingShareGuaranteedVirtualMemory": ("UInt64", True, False),
        "GLUE2ComputingShareMaxDiskSpace": ("UInt64", True, False),
        "GLUE2ComputingShareDefaultStorageService": ("URI", True, False),
        "GLUE2ComputingSharePreemption": ("ExtendedBoolean_t", True, False),
        "GLUE2ComputingShareServingState": ("ServingState_t", True, True),
        "GLUE2ComputingShareTotalJobs": ("UInt32", True, False),
        "GLUE2ComputingShareRunningJobs": ("UInt32", True, False),
        "GLUE2ComputingShareLocalRunningJobs": ("UInt32", True, False),
        "GLUE2ComputingShareWaitingJobs": ("UInt32", True, False),
        "GLUE2ComputingShareLocalWaitingJobs": ("UInt32", True, False),
        "GLUE2ComputingShareSuspendedJobs": ("UInt32", True, False),
        "GLUE2ComputingShareLocalSuspendedJobs": ("UInt32", True, False),
        "GLUE2ComputingShareStagingJobs": ("UInt32", True, False),
        "GLUE2ComputingSharePreLRMSWaitingJobs": ("UInt32", True, False),
        "GLUE2ComputingShareEstimatedAverageWaitingTime": ("UInt64", True, False),
        "GLUE2ComputingShareEstimatedWorstWaitingTime": ("UInt64", True, False),
        "GLUE2ComputingShareFreeSlots": ("UInt32", True, False),
        "GLUE2ComputingShareFreeSlotsWithDuration": ("String", True, False),
        "GLUE2ComputingShareUsedSlots": ("UInt32", True, False),
        "GLUE2ComputingShareRequestedSlots": ("UInt32", True, False),
        "GLUE2ComputingShareReservationPolicy": ("ReservationPolicy_t", True, False),
        "GLUE2ComputingShareTag": ("String", False, False),
    },
    "GLUE2ComputingManager": {
        "GLUE2ComputingManagerReservation": ("ExtendedBoolean_t", True, False),
        "GLUE2ComputingManagerBulkSubmission": ("ExtendedBoolean_t", True, False),
        "GLUE2ComputingManagerTotalPhysicalCPUs": ("UInt32", True, False),
        "GLUE2ComputingManagerTotalLogicalCPUs": ("UInt32", True, False),
        "GLUE2ComputingManagerTotalSlots": ("UInt32", True, False),
        "GLUE2ComputingManagerSlotsUsedByLocalJobs": ("UInt32", True, False),
        "GLUE2ComputingManagerSlotsUsedByGridJobs": ("UInt32", True, False),
        "GLUE2ComputingManagerHomogeneous": ("ExtendedBoolean_t", True, False),
        "GLUE2ComputingManagerNetworkInfo": ("NetworkInfo_t", False, False),
        "GLUE2ComputingManagerLogicalCPUDistribution": ("String", True, False),
        "GLUE2ComputingManagerWorkingAreaShared": ("ExtendedBoolean_t", True, False),
        "GLUE2ComputingManagerWorkingAreaGuaranteed": (
            "ExtendedBoolean_t",
            True,
            False,
        ),
        "GLUE2ComputingManagerWorkingAreaTotal": ("UInt64", True, False),
        "GLUE2ComputingManagerWorkingAreaFree": ("UInt64", True, False),
        "GLUE2ComputingManagerWorkingAreaLifeTime": ("UInt64", True, False),
        "GLUE2ComputingManagerWorkingAreaMultiSlotTotal": ("UInt64", True, False),
        "GLUE2ComputingManagerWorkingAreaMultiSlotFree": ("UInt64", True, False),
        "GLUE2ComputingManagerWorkingAreaMultiSlotLifeTime": ("UInt64", True, False),
        "GLUE2ComputingManagerCacheTotal": ("UInt64", True, False),
        "GLUE2ComputingManagerCacheFree": ("UInt64", True, False),
        "GLUE2ComputingManagerTmpDir": ("String", True, False),
        "GLUE2ComputingManagerScratchDir": ("String", True, False),
        "GLUE2ComputingManagerApplicationDir": ("String", True, False),
        "GLUE2ComputingManagerComputingServiceForeignKey": ("URI", True, True),
    },
    "GLUE2Benchmark": {
        "GLUE2BenchmarkID": ("URI", True, True),
        "GLUE2BenchmarkType": ("Benchmark_t", True, True),
        "GLUE2BenchmarkValue": ("Real32", True, True),
        "GLUE2BenchmarkExecutionEnvironmentForeignKey": ("URI", True, False),
        "GLUE2BenchmarkComputingManagerForeignKey": ("URI", True, False),
    },
    "GLUE2ExecutionEnvironment": {
        "GLUE2ExecutionEnvironmentPlatform": ("Platform_t", True, True),
        "GLUE2ExecutionEnvironmentVirtualMachine": ("ExtendedBoolean_t", True, False),
        "GLUE2ExecutionEnvironmentTotalInstances": ("UInt32", True, False),
        "GLUE2ExecutionEnvironmentUsedInstances": ("UInt32", True, False),
        "GLUE2ExecutionEnvironmentUnavailableInstances": ("UInt32", True, False),
        "GLUE2ExecutionEnvironmentPhysicalCPUs": ("UInt32", True, False),
        "GLUE2ExecutionEnvironmentLogicalCPUs": ("UInt32", True, False),
        "GLUE2ExecutionEnvironmentCPUMultiplicity": ("CPUMultiplicity_t", True, False),
        "GLUE2ExecutionEnvironmentCPUVendor": ("String", True, False),
        "GLUE2ExecutionEnvironmentCPUModel": ("String", True, False),
        "GLUE2ExecutionEnvironmentCPUVersion": ("String", True, False),
        "GLUE2ExecutionEnvironmentCPUClockSpeed": ("UInt32", True, False),
        "GLUE2ExecutionEnvironmentCPUTimeScalingFactor": ("Real32", True, False),
        "GLUE2ExecutionEnvironmentWallTimeScalingFactor": ("Real32", True, False),
        "GLUE2ExecutionEnvironmentMainMemorySize": ("UInt64", True, True),
        "GLUE2ExecutionEnvironmentVirtualMemorySize": ("UInt64", True, False),
        "GLUE2ExecutionEnvironmentOSFamily": ("OSFamily_t", True, True),
        "GLUE2ExecutionEnvironmentOSName": ("OSName_t", True, False),
        "GLUE2ExecutionEnvironmentOSVersion": ("String", True, False),
        "GLUE2ExecutionEnvironmentConnectivityIn": ("ExtendedBoolean_t", True, True),
        "GLUE2ExecutionEnvironmentConnectivityOut": ("ExtendedBoolean_t", True, True),
        "GLUE2ExecutionEnvironmentNetworkInfo": ("NetworkInfo_t", False, False),
        "GLUE2ExecutionEnvironmentComputingManagerForeignKey": ("URI", True, True),
    },
    "GLUE2ApplicationEnvironment": {
        "GLUE2ApplicationEnvironmentID": ("URI", True, True),
        "GLUE2ApplicationEnvironmentName": ("String", True, False),
        "GLUE2ApplicationEnvironmentAppName": ("String", True, True),
        "GLUE2ApplicationEnvironmentAppVersion": ("String", True, False),
        "GLUE2ApplicationEnvironmentRepository": ("URL", True, False),
        "GLUE2ApplicationEnvironmentState": ("AppEnvState_t", True, False),
        "GLUE2ApplicationEnvironmentRemovalDate": ("DateTime_t", True, False),
        "GLUE2ApplicationEnvironmentLicense": ("License_t", True, False),
        "GLUE2ApplicationEnvironmentDescription": ("String", True, False),
        "GLUE2ApplicationEnvironmentBestBenchmark": ("Benchmark_t", True, False),
        "GLUE2ApplicationEnvironmentParallelSupport": (
            "ParallelSupport_t",
            True,
            False,
        ),
        "GLUE2ApplicationEnvironmentMaxSlots": ("UInt32", True, False),
        "GLUE2ApplicationEnvironmentMaxJobs": ("UInt32", True, False),
        "GLUE2ApplicationEnvironmentMaxUserSeats": ("UInt32", True, False),
        "GLUE2ApplicationEnvironmentFreeSlots": ("UInt32", True, False),
        "GLUE2ApplicationEnvironmentFreeJobs": ("UInt32", True, False),
        "GLUE2ApplicationEnvironmentFreeUserSeats": ("UInt32", True, False),
        "GLUE2ApplicationEnvironmentComputingManagerForeignKey": ("URI", True, False),
        "GLUE2ApplicationEnvironmentExecutionEnvironmentForeignKey": (
            "URI",
            False,
            False,
        ),
    },
    "GLUE2ApplicationHandle": {
        "GLUE2ApplicationHandleID": ("URI", True, True),
        "GLUE2ApplicationHandleType": ("ApplicationHandle_t", True, True),
        "GLUE2ApplicationHandleValue": ("String", True, True),
        "GLUE2ApplicationHandleApplicationEnvironmentForeignKey": ("URI", True, False),
    },
    "GLUE2ComputingActivity": {
        "GLUE2ComputingActivityType": ("ComputingActivityType_t", True, False),
        "GLUE2ComputingActivityIDFromEndpoint": ("URI", True, False),
        "GLUE2ComputingActivityLocalIDFromManager": ("String", True, False),
        "GLUE2ComputingActivityJobDescription": ("JobDescription_t", True, False),
        "GLUE2ComputingActivityState": ("ComputingActivityState_t", False, True),
        "GLUE2ComputingActivityRestartState": (
            "ComputingActivityState_t",
            False,
            False,
        ),
        "GLUE2ComputingActivityExitCode": ("Int32", True, False),
        "GLUE2ComputingActivityComputingManagerExitCode": ("String", True, False),
        "GLUE2ComputingActivityError": ("String", False, False),
        "GLUE2ComputingActivityWaitingPosition": ("UInt32", True, False),
        "GLUE2ComputingActivityUserDomain": ("String", True, False),
        "GLUE2ComputingActivityOwner": ("String", True, True),
        "GLUE2ComputingActivityLocalOwner": ("String", True, False),
        "GLUE2ComputingActivityRequestedTotalWallTime": ("UInt64", True, False),
        "GLUE2ComputingActivityRequestedTotalCPUTime": ("UInt64", True, False),
        "GLUE2ComputingActivityRequestedSlots": ("UInt32", True, False),
        "GLUE2ComputingActivityRequestedApplicationEnvironment": (
            "String",
            False,
            False,
        ),
        "GLUE2ComputingActivityStdIn": ("String", True, False),
        "GLUE2ComputingActivityStdOut": ("String", True, False),
        "GLUE2ComputingActivityStdErr": ("String", True, False),
        "GLUE2ComputingActivityLogDir": ("String", True, False),
        "GLUE2ComputingActivityExecutionNode": ("String", False, False),
        "GLUE2ComputingActivityQueue": ("String", True, False),
        "GLUE2ComputingActivityUsedTotalWallTime": ("UInt64", True, False),
        "GLUE2ComputingActivityUsedTotalCPUTime": ("UInt64", True, False),
        "GLUE2ComputingActivityUsedMainMemory": ("UInt64", True, False),
        "GLUE2ComputingActivitySubmissionTime": ("DateTime_t", True, False),
        "GLUE2ComputingActivityComputingManagerSubmissionTime": (
            "DateTime_t",
            True,
            False,
        ),
        "GLUE2ComputingActivityStartTime": ("DateTime_t", True, False),
        "GLUE2ComputingActivityComputingManagerEndTime": ("DateTime_t", True, False),
        "GLUE2ComputingActivityEndTime": ("DateTime_t", True, False),
        "GLUE2ComputingActivityWorkingAreaEraseTime": ("DateTime_t", True, False),
        "GLUE2ComputingActivityProxyExpirationTime": ("DateTime_t", True, False),
        "GLUE2ComputingActivitySubmissionHost": ("String", True, False),
        "GLUE2ComputingActivitySubmissionClientName": ("String", True, False),
        "GLUE2ComputingActivityOtherMessages": ("String", False, False),
        "GLUE2ComputingActivityComputingEndpointForeignKey": ("URI", True, False),
        "GLUE2ComputingActivityComputingShareForeignKey": ("URI", True, False),
        "GLUE2ComputingActivityExecutionEnvironmentForeignKey": ("URI", True, False),
    },
    "GLUE2ToStorageService": {
        "GLUE2ToStorageServiceID": ("URI", True, True),
        "GLUE2ToStorageServiceLocalPath": ("String", True, False),
        "GLUE2ToStorageServiceRemotePath": ("String", True, False),
        "GLUE2ToStorageServiceComputingServiceForeignKey": ("URI", True, True),
        "GLUE2ToStorageServiceStorageServiceForeignKey": ("URI", True, True),
    },
    "GLUE2StorageService": {},
    "GLUE2StorageServiceCapacity": {
        "GLUE2StorageServiceCapacityID": ("URI", True, True),
        "GLUE2StorageServiceCapacityType": ("StorageCapacity_t", True, False),
        "GLUE2StorageServiceCapacityTotalSize": ("UInt64", True, False),
        "GLUE2StorageServiceCapacityFreeSize": ("UInt64", True, False),
        "GLUE2StorageServiceCapacityUsedSize": ("UInt64", True, False),
        "GLUE2StorageServiceCapacityReservedSize": ("UInt64", True, False),
        "GLUE2StorageServiceCapacityStorageServiceForeignKey": ("URI", True, False),
    },
    "GLUE2StorageAccessProtocol": {
        "GLUE2StorageAccessProtocolID": ("URI", True, True),
        "GLUE2StorageAccessProtocolType": ("StorageAccessProtocol_t", True, True),
        "GLUE2StorageAccessProtocolVersion": ("String", True, True),
        "GLUE2StorageAccessProtocolMaxStreams": ("UInt32", True, False),
        "GLUE2StorageAccessProtocolStorageServiceForeignKey": ("URI", True, False),
    },
    "GLUE2StorageShare": {
        "GLUE2StorageShareServingState": ("ServingState_t", True, True),
        "GLUE2StorageSharePath": ("String", True, False),
        "GLUE2StorageShareAccessMode": ("AccessMode_t", False, False),
        "GLUE2StorageShareSharingID": ("LocalID_t", True, True),
        "GLUE2StorageShareAccessLatency": ("AccessLatency_t", True, True),
        "GLUE2StorageShareRetentionPolicy": ("RetentionPolicy_t", False, False),
        "GLUE2StorageShareExpirationMode": ("ExpirationMode_t", False, False),
        "GLUE2StorageShareDefaultLifeTime": ("UInt32", True, False),
        "GLUE2StorageShareMaximumLifeTime": ("UInt32", True, False),
        "GLUE2StorageShareTag": ("String", True, False),
        "GLUE2StorageShareStorageServiceForeignKey": ("URI", True, True),
        "GLUE2StorageShareStorageEndpointForeignKey": ("URI", False, False),
        "GLUE2StorageShareDataStoreForeignKey": ("URI", False, False),
    },
    "GLUE2StorageShareCapacity": {
        "GLUE2StorageShareCapacityID": ("URI", True, True),
        "GLUE2StorageShareCapacityType": ("StorageCapacity_t", True, True),
        "GLUE2StorageShareCapacityTotalSize": ("UInt64", True, False),
        "GLUE2StorageShareCapacityFreeSize": ("UInt64", True, False),
        "GLUE2StorageShareCapacityUsedSize": ("UInt64", True, False),
        "GLUE2StorageShareCapacityReservedSize": ("UInt64", True, False),
        "GLUE2StorageShareCapacityStorageShareForeignKey": ("URI", True, False),
    },
    "GLUE2DataStore": {
        "GLUE2DataStoreType": ("DataStoreType_t", True, True),
        "GLUE2DataStoreLatency": ("AccessLatency_t", True, True),
        "GLUE2DataStoreTotalSize": ("UInt64", True, False),
        "GLUE2DataStoreFreeSize": ("UInt64", True, False),
        "GLUE2DataStoreUsedSize": ("UInt64", True, False),
        "GLUE2DataStoreStorageManagerForeignKey": ("URI", True, True),
    },
    "GLUE2ToComputingService": {
        "GLUE2ToComputingServiceID": ("URI", True, True),
        "GLUE2ToComputingServiceNetworkInfo": ("NetworkInfo_t", True, False),
        "GLUE2ToComputingServiceBandwidth": ("UInt32", True, False),
        "GLUE2ToComputingServiceStorageAccessProtocolForeignKey": ("URI", False, False),
        "GLUE2ToComputingServiceStorageServiceForeignKey": ("URI", True, True),
        "GLUE2ToComputingServiceComputingServiceForeignKey": ("URI", True, True),
    },
    "GLUE2StorageEndpoint": {
        # 'GLUE2StorageEndpointStorageServiceForeignKey': ('URI', True, True),
    },
    "GLUE2StorageManager": {
        "GLUE2StorageManagerStorageServiceForeignKey": ("URI", True, True),
    },
}
