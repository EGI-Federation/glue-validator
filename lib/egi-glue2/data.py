schema = {
    "organization": {
        "o": ("String", True, "Mandatory"),
    },
    "GLUE2Entity": {
        "dn": ("DN_t", True, "Mandatory"),
        "objectClass": ("ObjectClass", False, "Mandatory"),
        "GLUE2EntityCreationTime": ("DateTime_t", True, "Recommended"),
        "GLUE2EntityValidity": ("UInt64", True, "Desirable"),
        "GLUE2EntityOtherInfo": ("EntityOtherInfo_t", False, "Optional"),
    },
    "GLUE2Group": {
        "GLUE2GroupID": ("URI", True, "Mandatory"),
        "GLUE2GroupName": ("URI", True, "Optional"),
    },
    "GLUE2Extension": {
        "GLUE2ExtensionLocalID": ("LocalID_t", True, "Mandatory"),
        "GLUE2ExtensionKey": ("String", True, "Mandatory"),
        "GLUE2ExtensionValue": ("String", True, "Mandatory"),
    },
    "GLUE2Location": {
        "GLUE2LocationID": ("URI", True, "Mandatory"),
        "GLUE2LocationAddress": ("String", True, "Optional"),
        "GLUE2LocationPlace": ("String", True, "Desirable"),
        "GLUE2LocationCountry": ("String", True, "Recommended"),
        "GLUE2LocationPostCode": ("String", True, "Optional"),
        "GLUE2LocationLatitude": ("Real32", True, "Recommended"),
        "GLUE2LocationLongitude": ("Real32", True, "Recommended"),
        "GLUE2LocationDomainForeignKey": ("URI", False, "Optional"),
    },
    "GLUE2Contact": {
        "GLUE2ContactID": ("URI", True, "Mandatory"),
        "GLUE2ContactName": ("String", True, "Optional"),
        "GLUE2ContactDetail": ("URI", True, "Mandatory"),
        "GLUE2ContactType": ("ContactType_t", True, "Mandatory"),
        "GLUE2ContactDomainForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2Domain": {
        "GLUE2DomainID": ("URI", True, "Mandatory"),
        "GLUE2DomainName": ("String", True, "Optional"),
        "GLUE2DomainDescription": ("String", True, "Desirable"),
        "GLUE2DomainWWW": ("URL", False, "Desirable"),
    },
    "GLUE2AdminDomain": {
        "GLUE2AdminDomainDistributed": ("ExtendedBoolean_t", True, "Desirable"),
        "GLUE2AdminDomainOwner": ("String", False, "Optional"),
        "GLUE2AdminDomainAdminDomainForeignKey": ("URI", False, "Optional"),
    },
    "GLUE2UserDomain": {
        "GLUE2UserDomainLevel": ("UInt32", True, "Optional"),
        "GLUE2UserDomainUserManager": ("URI", False, "Desirable"),
        "GLUE2UserDomainMember": ("String", False, "Undesirable"),
        "GLUE2UserDomainUserDomainForeignKey": ("URI", False, "Optional"),
    },
    "GLUE2Service": {
        "GLUE2ServiceID": ("URI", True, "Mandatory"),
        "GLUE2ServiceCapability": ("Capability_t", False, "Recommended"),
        "GLUE2ServiceType": ("ServiceType_t", True, "Mandatory"),
        "GLUE2ServiceQualityLevel": ("QualityLevel_t", True, "Mandatory"),
        "GLUE2ServiceStatusInfo": ("URL", False, "Optional"),
        "GLUE2ServiceComplexity": ("String", True, "Desirable"),
        "GLUE2ServiceAdminDomainForeignKey": ("URI", True, "Mandatory"),
        "GLUE2ServiceServiceForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2Endpoint": {
        "GLUE2EndpointID": ("URI", True, "Mandatory"),
        "GLUE2EndpointURL": ("URL", True, "Mandatory"),
        "GLUE2EndpointCapability": ("Capability_t", False, "Recommended"),
        "GLUE2EndpointTechnology": ("EndpointTechnology_t", True, "Optional"),
        "GLUE2EndpointInterfaceName": ("InterfaceName_t", True, "Mandatory"),
        "GLUE2EndpointInterfaceVersion": ("String", True, "Recommended"),
        "GLUE2EndpointInterfaceExtension": ("URI", False, "Optional"),
        "GLUE2EndpointWSDL": ("URL", False, "Optional"),
        "GLUE2EndpointSupportedProfile": ("URI", False, "Optional"),
        "GLUE2EndpointSemantics": ("URL", False, "Desirable"),
        "GLUE2EndpointImplementor": ("String", True, "Desirable"),
        "GLUE2EndpointImplementationName": ("String", True, "Mandatory"),
        "GLUE2EndpointImplementationVersion": ("String", True, "Mandatory"),
        "GLUE2EndpointQualityLevel": ("QualityLevel_t", True, "Mandatory"),
        "GLUE2EndpointHealthState": ("EndpointHealthState_t", True, "Mandatory"),
        "GLUE2EndpointHealthStateInfo": ("String", False, "Desirable"),
        "GLUE2EndpointServingState": ("ServingState_t", True, "Mandatory"),
        "GLUE2EndpointStartTime": ("DateTime_t", True, "Desirable"),
        "GLUE2EndpointIssuerCA": ("DN_t", True, "Recommended"),
        "GLUE2EndpointTrustedCA": ("DN_t", False, "Optional"),
        "GLUE2EndpointDowntimeAnnounce": ("DateTime_t", True, "Optional"),
        "GLUE2EndpointDowntimfeStart": ("DateTime_t", True, "Optional"),
        "GLUE2EndpointDowntimeEnd": ("DateTime_t", True, "Optional"),
        "GLUE2EndpointDowntimeInfo": ("String", True, "Optional"),
        "GLUE2EndpointServiceForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2Policy": {
        "GLUE2PolicyID": ("URI", True, "Mandatory"),
        "GLUE2PolicyScheme": ("PolicyScheme_t", True, "Mandatory"),
        "GLUE2PolicyRule": ("String", False, "Mandatory"),
        "GLUE2PolicyUserDomainForeignKey": ("URI", False, "Recommended"),
        "GLUE2PolicyEndpointForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2AccessPolicy": {},
    "GLUE2MappingPolicy": {},
    "GLUE2Share": {
        "GLUE2ShareID": ("URI", True, "Mandatory"),
        "GLUE2ShareDescription": ("String", True, "Desirable"),
        "GLUE2ShareServiceForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2Manager": {
        "GLUE2ManagerID": ("URI", True, "Mandatory"),
        "GLUE2ManagerProductName": ("String", True, "Mandatory"),
        "GLUE2ManagerProductVersion": ("String", True, "Mandatory"),
        "GLUE2ManagerServiceForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2Resource": {
        "GLUE2ResourceID": ("URI", True, "Mandatory"),
        "GLUE2ResourceManagerForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2Activity": {
        "GLUE2ActivityID": ("URI", True, "Mandatory"),
        "GLUE2ActivityUserDomainForeignKey": ("URI", True, "Optional"),
        "GLUE2ActivityEndpointForeignKey": ("URI", True, "Optional"),
        "GLUE2ActivityShareForeignKey": ("URI", True, "Optional"),
        "GLUE2ActivityResourceForeignKey": ("URI", True, "Optional"),
        "GLUE2ActivityActivityForeignKey": ("URI", False, "Optional"),
    },
    "GLUE2ComputingService": {
        "GLUE2ComputingServiceTotalJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingServiceRunningJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingServiceWaitingJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingServiceStagingJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingServiceSuspendedJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingServicePreLRMSWaitingJobs": ("UInt32", True, "Optional"),
    },
    "GLUE2ComputingEndpoint": {
        "GLUE2ComputingEndpointStaging": ("Staging_t", True, "Optional"),
        "GLUE2ComputingEndpointJobDescription": ("JobDescription_t", False, "Optional"),
        "GLUE2ComputingEndpointTotalJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingEndpointRunningJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingEndpointWaitingJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingEndpointStagingJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingEndpointSuspendedJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingEndpointPreLRMSWaitingJobs": ("UInt32", True, "Optional"),
        # 'GLUE2ComputingEndpointComputingServiceForeignKey' : ('URI', True, 'Optional'),
    },
    "GLUE2ComputingShare": {
        "GLUE2ComputingShareMappingQueue": ("String", True, "Recommended"),
        "GLUE2ComputingShareMaxWallTime": ("UInt64", True, "Recommended"),
        "GLUE2ComputingShareMaxMultiSlotWallTime": ("UInt64", True, "Recommended"),
        "GLUE2ComputingShareMinWallTime": ("UInt64", True, "Recommended"),
        "GLUE2ComputingShareDefaultWallTime": ("UInt64", True, "Mandatory"),
        "GLUE2ComputingShareMaxCPUTime": ("UInt64", True, "Recommended"),
        "GLUE2ComputingShareMaxTotalCPUTime": ("UInt64", True, "Recommended"),
        "GLUE2ComputingShareMinCPUTime": ("UInt64", True, "Recommended"),
        "GLUE2ComputingShareDefaultCPUTime": ("UInt64", True, "Mandatory"),
        "GLUE2ComputingShareMaxTotalJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingShareMaxRunningJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingShareMaxWaitingJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingShareMaxPreLRMSWaitingJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingShareMaxUserRunningJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingShareMaxSlotsPerJob": ("UInt32", True, "Mandatory"),
        "GLUE2ComputingShareMaxStageInStreams": ("UInt32", True, "Optional"),
        "GLUE2ComputingShareMaxStageOutStreams": ("UInt32", True, "Optional"),
        "GLUE2ComputingShareSchedulingPolicy": ("SchedulingPolicy_t", True, "Optional"),
        "GLUE2ComputingShareMaxMainMemory": ("UInt64", True, "Mandatory"),
        "GLUE2ComputingShareGuaranteedMainMemory": ("UInt64", True, "Mandatory"),
        "GLUE2ComputingShareMaxVirtualMemory": ("UInt64", True, "Mandatory"),
        "GLUE2ComputingShareGuaranteedVirtualMemory": ("UInt64", True, "Mandatory"),
        "GLUE2ComputingShareMaxDiskSpace": ("UInt64", True, "Optional"),
        "GLUE2ComputingShareDefaultStorageService": ("URI", True, "Optional"),
        "GLUE2ComputingSharePreemption": ("ExtendedBoolean_t", True, "Optional"),
        "GLUE2ComputingShareServingState": ("ServingState_t", True, "Mandatory"),
        "GLUE2ComputingShareTotalJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingShareRunningJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingShareLocalRunningJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingShareWaitingJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingShareLocalWaitingJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingShareSuspendedJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingShareLocalSuspendedJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingShareStagingJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingSharePreLRMSWaitingJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingShareEstimatedAverageWaitingTime": ("UInt64", True, "Mandatory"),
        "GLUE2ComputingShareEstimatedWorstWaitingTime": ("UInt64", True, "Mandatory"),
        "GLUE2ComputingShareFreeSlots": ("UInt32", True, "Mandatory"),
        "GLUE2ComputingShareFreeSlotsWithDuration": ("String", True, "Optional"),
        "GLUE2ComputingShareUsedSlots": ("UInt32", True, "Mandatory"),
        "GLUE2ComputingShareRequestedSlots": ("UInt32", True, "Recommended"),
        "GLUE2ComputingShareReservationPolicy": (
            "ReservationPolicy_t",
            True,
            "Optional",
        ),
        "GLUE2ComputingShareTag": ("String", False, "Optional"),
    },
    "GLUE2ComputingManager": {
        "GLUE2ComputingManagerReservation": ("ExtendedBoolean_t", True, "Optional"),
        "GLUE2ComputingManagerBulkSubmission": ("ExtendedBoolean_t", True, "Optional"),
        "GLUE2ComputingManagerTotalPhysicalCPUs": ("UInt32", True, "Mandatory"),
        "GLUE2ComputingManagerTotalLogicalCPUs": ("UInt32", True, "Mandatory"),
        "GLUE2ComputingManagerTotalSlots": ("UInt32", True, "Recommended"),
        "GLUE2ComputingManagerSlotsUsedByLocalJobs": ("UInt32", True, "Optional"),
        "GLUE2ComputingManagerSlotsUsedByGridJobs": ("UInt32", True, "Recommended"),
        "GLUE2ComputingManagerHomogeneous": ("ExtendedBoolean_t", True, "Optional"),
        "GLUE2ComputingManagerNetworkInfo": ("NetworkInfo_t", False, "NetworkInfo"),
        "GLUE2ComputingManagerLogicalCPUDistribution": ("String", True, "Optional"),
        "GLUE2ComputingManagerWorkingAreaShared": (
            "ExtendedBoolean_t",
            True,
            "Desirable",
        ),
        "GLUE2ComputingManagerWorkingAreaGuaranteed": (
            "ExtendedBoolean_t",
            True,
            "Desirable",
        ),
        "GLUE2ComputingManagerWorkingAreaTotal": ("UInt64", True, "Desirable"),
        "GLUE2ComputingManagerWorkingAreaFree": ("UInt64", True, "Desirable"),
        "GLUE2ComputingManagerWorkingAreaLifeTime": ("UInt64", True, "Desirable"),
        "GLUE2ComputingManagerWorkingAreaMultiSlotTotal": ("UInt64", True, "Desirable"),
        "GLUE2ComputingManagerWorkingAreaMultiSlotFree": ("UInt64", True, "Desirable"),
        "GLUE2ComputingManagerWorkingAreaMultiSlotLifeTime": (
            "UInt64",
            True,
            "Desirable",
        ),
        "GLUE2ComputingManagerCacheTotal": ("UInt64", True, "Desirable"),
        "GLUE2ComputingManagerCacheFree": ("UInt64", True, "Desirable"),
        "GLUE2ComputingManagerTmpDir": ("String", True, "Optional"),
        "GLUE2ComputingManagerScratchDir": ("String", True, "Optional"),
        "GLUE2ComputingManagerApplicationDir": ("String", True, "Optional"),
        "GLUE2ComputingManagerComputingServiceForeignKey": ("URI", True, "Mandatory"),
    },
    "GLUE2Benchmark": {
        "GLUE2BenchmarkID": ("URI", True, "Mandatory"),
        "GLUE2BenchmarkType": ("Benchmark_t", True, "Mandatory"),
        "GLUE2BenchmarkValue": ("Real32", True, "Mandatory"),
        "GLUE2BenchmarkExecutionEnvironmentForeignKey": ("URI", True, "Optional"),
        "GLUE2BenchmarkComputingManagerForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2ExecutionEnvironment": {
        "GLUE2ExecutionEnvironmentPlatform": ("Platform_t", True, "Mandatory"),
        "GLUE2ExecutionEnvironmentVirtualMachine": (
            "ExtendedBoolean_t",
            True,
            "Desirable",
        ),
        "GLUE2ExecutionEnvironmentTotalInstances": ("UInt32", True, "Recommended"),
        "GLUE2ExecutionEnvironmentUsedInstances": ("UInt32", True, "Optional"),
        "GLUE2ExecutionEnvironmentUnavailableInstances": ("UInt32", True, "Optional"),
        "GLUE2ExecutionEnvironmentPhysicalCPUs": ("UInt32", True, "Recommended"),
        "GLUE2ExecutionEnvironmentLogicalCPUs": ("UInt32", True, "Recommended"),
        "GLUE2ExecutionEnvironmentCPUMultiplicity": (
            "CPUMultiplicity_t",
            True,
            "Recommended",
        ),
        "GLUE2ExecutionEnvironmentCPUVendor": ("String", True, "Recommended"),
        "GLUE2ExecutionEnvironmentCPUModel": ("String", True, "Recommended"),
        "GLUE2ExecutionEnvironmentCPUVersion": ("String", True, "Recommended"),
        "GLUE2ExecutionEnvironmentCPUClockSpeed": ("UInt32", True, "Recommended"),
        "GLUE2ExecutionEnvironmentCPUTimeScalingFactor": ("Real32", True, "Mandatory"),
        "GLUE2ExecutionEnvironmentWallTimeScalingFactor": ("Real32", True, "Mandatory"),
        "GLUE2ExecutionEnvironmentMainMemorySize": ("UInt64", True, "Mandatory"),
        "GLUE2ExecutionEnvironmentVirtualMemorySize": ("UInt64", True, "Mandatory"),
        "GLUE2ExecutionEnvironmentOSFamily": ("OSFamily_t", True, "Mandatory"),
        "GLUE2ExecutionEnvironmentOSName": ("OSName_t", True, "Mandatory"),
        "GLUE2ExecutionEnvironmentOSVersion": ("String", True, "Mandatory"),
        "GLUE2ExecutionEnvironmentConnectivityIn": (
            "ExtendedBoolean_t",
            True,
            "Mandatory",
        ),
        "GLUE2ExecutionEnvironmentConnectivityOut": (
            "ExtendedBoolean_t",
            True,
            "Mandatory",
        ),
        "GLUE2ExecutionEnvironmentNetworkInfo": ("NetworkInfo_t", False, "Optional"),
        "GLUE2ExecutionEnvironmentComputingManagerForeignKey": (
            "URI",
            True,
            "Mandatory",
        ),
    },
    "GLUE2ApplicationEnvironment": {
        "GLUE2ApplicationEnvironmentID": ("URI", True, "Mandatory"),
        "GLUE2ApplicationEnvironmentName": ("String", True, "Optional"),
        "GLUE2ApplicationEnvironmentAppName": ("String", True, "Mandatory"),
        "GLUE2ApplicationEnvironmentAppVersion": ("String", True, "Optional"),
        "GLUE2ApplicationEnvironmentRepository": ("URL", True, "Optional"),
        "GLUE2ApplicationEnvironmentState": ("AppEnvState_t", True, "Optional"),
        "GLUE2ApplicationEnvironmentRemovalDate": ("DateTime_t", True, "Optional"),
        "GLUE2ApplicationEnvironmentLicense": ("License_t", True, "Optional"),
        "GLUE2ApplicationEnvironmentDescription": ("String", True, "Optional"),
        "GLUE2ApplicationEnvironmentBestBenchmark": ("Benchmark_t", True, "Optional"),
        "GLUE2ApplicationEnvironmentParallelSupport": (
            "ParallelSupport_t",
            True,
            "Optional",
        ),
        "GLUE2ApplicationEnvironmentMaxSlots": ("UInt32", True, "Optional"),
        "GLUE2ApplicationEnvironmentMaxJobs": ("UInt32", True, "Optional"),
        "GLUE2ApplicationEnvironmentMaxUserSeats": ("UInt32", True, "Optional"),
        "GLUE2ApplicationEnvironmentFreeSlots": ("UInt32", True, "Optional"),
        "GLUE2ApplicationEnvironmentFreeJobs": ("UInt32", True, "Optional"),
        "GLUE2ApplicationEnvironmentFreeUserSeats": ("UInt32", True, "Optional"),
        "GLUE2ApplicationEnvironmentComputingManagerForeignKey": (
            "URI",
            True,
            "Optional",
        ),
        "GLUE2ApplicationEnvironmentExecutionEnvironmentForeignKey": (
            "URI",
            False,
            "Optional",
        ),
    },
    "GLUE2ApplicationHandle": {
        "GLUE2ApplicationHandleID": ("URI", True, "Mandatory"),
        "GLUE2ApplicationHandleType": ("ApplicationHandle_t", True, "Mandatory"),
        "GLUE2ApplicationHandleValue": ("String", True, "Mandatory"),
        "GLUE2ApplicationHandleApplicationEnvironmentForeignKey": (
            "URI",
            True,
            "Optional",
        ),
    },
    "GLUE2ComputingActivity": {
        "GLUE2ComputingActivityType": ("ComputingActivityType_t", True, "Undesirable"),
        "GLUE2ComputingActivityIDFromEndpoint": ("URI", True, "Undesirable"),
        "GLUE2ComputingActivityLocalIDFromManager": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityJobDescription": (
            "JobDescription_t",
            True,
            "Undesirable",
        ),
        "GLUE2ComputingActivityState": (
            "ComputingActivityState_t",
            False,
            "Undesirable",
        ),
        "GLUE2ComputingActivityRestartState": (
            "ComputingActivityState_t",
            False,
            "Undesirable",
        ),
        "GLUE2ComputingActivityExitCode": ("Int32", True, "Undesirable"),
        "GLUE2ComputingActivityComputingManagerExitCode": (
            "String",
            True,
            "Undesirable",
        ),
        "GLUE2ComputingActivityError": ("String", False, "Undesirable"),
        "GLUE2ComputingActivityWaitingPosition": ("UInt32", True, "Undesirable"),
        "GLUE2ComputingActivityUserDomain": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityOwner": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityLocalOwner": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityRequestedTotalWallTime": ("UInt64", True, "Undesirable"),
        "GLUE2ComputingActivityRequestedTotalCPUTime": ("UInt64", True, "Undesirable"),
        "GLUE2ComputingActivityRequestedSlots": ("UInt32", True, "Undesirable"),
        "GLUE2ComputingActivityRequestedApplicationEnvironment": (
            "String",
            False,
            "Undesirable",
        ),
        "GLUE2ComputingActivityStdIn": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityStdOut": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityStdErr": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityLogDir": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityExecutionNode": ("String", False, "Undesirable"),
        "GLUE2ComputingActivityQueue": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityUsedTotalWallTime": ("UInt64", True, "Undesirable"),
        "GLUE2ComputingActivityUsedTotalCPUTime": ("UInt64", True, "Undesirable"),
        "GLUE2ComputingActivityUsedMainMemory": ("UInt64", True, "Undesirable"),
        "GLUE2ComputingActivitySubmissionTime": ("DateTime_t", True, "Undesirable"),
        "GLUE2ComputingActivityComputingManagerSubmissionTime": (
            "DateTime_t",
            True,
            "Undesirable",
        ),
        "GLUE2ComputingActivityStartTime": ("DateTime_t", True, "Undesirable"),
        "GLUE2ComputingActivityComputingManagerEndTime": (
            "DateTime_t",
            True,
            "Undesirable",
        ),
        "GLUE2ComputingActivityEndTime": ("DateTime_t", True, "Undesirable"),
        "GLUE2ComputingActivityWorkingAreaEraseTime": (
            "DateTime_t",
            True,
            "Undesirable",
        ),
        "GLUE2ComputingActivityProxyExpirationTime": (
            "DateTime_t",
            True,
            "Undesirable",
        ),
        "GLUE2ComputingActivitySubmissionHost": ("String", True, "Undesirable"),
        "GLUE2ComputingActivitySubmissionClientName": ("String", True, "Undesirable"),
        "GLUE2ComputingActivityOtherMessages": ("String", False, "Undesirable"),
        "GLUE2ComputingActivityComputingEndpointForeignKey": (
            "URI",
            True,
            "Undesirable",
        ),
        "GLUE2ComputingActivityComputingShareForeignKey": ("URI", True, "Undesirable"),
        "GLUE2ComputingActivityExecutionEnvironmentForeignKey": (
            "URI",
            True,
            "Undesirable",
        ),
    },
    "GLUE2ToStorageService": {
        "GLUE2ToStorageServiceID": ("URI", True, "Mandatory"),
        "GLUE2ToStorageServiceLocalPath": ("String", True, "Mandatory"),
        "GLUE2ToStorageServiceRemotePath": ("String", True, "Mandatory"),
        "GLUE2ToStorageServiceComputingServiceForeignKey": ("URI", True, "Mandatory"),
        "GLUE2ToStorageServiceStorageServiceForeignKey": ("URI", True, "Mandatory"),
    },
    "GLUE2StorageService": {},
    "GLUE2StorageServiceCapacity": {
        "GLUE2StorageServiceCapacityID": ("URI", True, "Mandatory"),
        "GLUE2StorageServiceCapacityType": ("StorageCapacity_t", True, "Mandatory"),
        "GLUE2StorageServiceCapacityTotalSize": ("UInt64", True, "Mandatory"),
        "GLUE2StorageServiceCapacityFreeSize": ("UInt64", True, "Recommended"),
        "GLUE2StorageServiceCapacityUsedSize": ("UInt64", True, "Recommended"),
        "GLUE2StorageServiceCapacityReservedSize": ("UInt64", True, "Recommended"),
        "GLUE2StorageServiceCapacityStorageServiceForeignKey": (
            "URI",
            True,
            "Optional",
        ),
    },
    "GLUE2StorageAccessProtocol": {
        "GLUE2StorageAccessProtocolID": ("URI", True, "Mandatory"),
        "GLUE2StorageAccessProtocolType": (
            "StorageAccessProtocol_t",
            True,
            "Mandatory",
        ),
        "GLUE2StorageAccessProtocolVersion": ("String", True, "Mandatory"),
        "GLUE2StorageAccessProtocolMaxStreams": ("UInt32", True, "Optional"),
        "GLUE2StorageAccessProtocolStorageServiceForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2StorageShare": {
        "GLUE2StorageShareServingState": ("ServingState_t", True, "Mandatory"),
        "GLUE2StorageSharePath": ("String", True, "Optional"),
        "GLUE2StorageShareAccessMode": ("AccessMode_t", False, "Optional"),
        "GLUE2StorageShareSharingID": ("LocalID_t", True, "Mandatory"),
        "GLUE2StorageShareAccessLatency": ("AccessLatency_t", True, "Mandatory"),
        "GLUE2StorageShareRetentionPolicy": ("RetentionPolicy_t", False, "Mandatory"),
        "GLUE2StorageShareExpirationMode": ("ExpirationMode_t", False, "Mandatory"),
        "GLUE2StorageShareDefaultLifeTime": ("UInt32", True, "Optional"),
        "GLUE2StorageShareMaximumLifeTime": ("UInt32", True, "Optional"),
        "GLUE2StorageShareTag": ("String", True, "Desirable"),
        "GLUE2StorageShareStorageServiceForeignKey": ("URI", True, "Mandatory"),
        "GLUE2StorageShareStorageEndpointForeignKey": ("URI", False, "Optional"),
        "GLUE2StorageShareDataStoreForeignKey": ("URI", False, "Optional"),
    },
    "GLUE2StorageShareCapacity": {
        "GLUE2StorageShareCapacityID": ("URI", True, "Mandatory"),
        "GLUE2StorageShareCapacityType": ("StorageCapacity_t", True, "Mandatory"),
        "GLUE2StorageShareCapacityTotalSize": ("UInt64", True, "Mandatory"),
        "GLUE2StorageShareCapacityFreeSize": ("UInt64", True, "Recommended"),
        "GLUE2StorageShareCapacityUsedSize": ("UInt64", True, "Recommended"),
        "GLUE2StorageShareCapacityReservedSize": ("UInt64", True, "Recommended"),
        "GLUE2StorageShareCapacityStorageShareForeignKey": ("URI", True, "Optional"),
    },
    "GLUE2DataStore": {
        "GLUE2DataStoreType": ("DataStoreType_t", True, "Mandatory"),
        "GLUE2DataStoreLatency": ("AccessLatency_t", True, "Mandatory"),
        "GLUE2DataStoreTotalSize": ("UInt64", True, "Mandatory"),
        "GLUE2DataStoreFreeSize": ("UInt64", True, "Desirable"),
        "GLUE2DataStoreUsedSize": ("UInt64", True, "Desirable"),
        "GLUE2DataStoreStorageManagerForeignKey": ("URI", True, "Mandatory"),
    },
    "GLUE2ToComputingService": {
        "GLUE2ToComputingServiceID": ("URI", True, "Mandatory"),
        "GLUE2ToComputingServiceNetworkInfo": ("NetworkInfo_t", True, "Mandatory"),
        "GLUE2ToComputingServiceBandwidth": ("UInt32", True, "Mandatory"),
        "GLUE2ToComputingServiceStorageAccessProtocolForeignKey": (
            "URI",
            False,
            "Optional",
        ),
        "GLUE2ToComputingServiceStorageServiceForeignKey": ("URI", True, "Mandatory"),
        "GLUE2ToComputingServiceComputingServiceForeignKey": ("URI", True, "Mandatory"),
    },
    "GLUE2StorageEndpoint": {
        # 'GLUE2StorageEndpointStorageServiceForeignKey' : ('URI', True, 'Mandatory'),
    },
    "GLUE2StorageManager": {
        "GLUE2StorageManagerStorageServiceForeignKey": ("URI", True, "Mandatory"),
    },
}
