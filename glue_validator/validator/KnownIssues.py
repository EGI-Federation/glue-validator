test_list = (
    "test_GLUE2EndpointImplementationVersion_OK",
    "test_GLUE2EndpointDowntimeAnnounce_OK",
    "test_GLUE2EndpointDowntimeAnnounce_checkStart",
    "test_GLUE2EndpointDowntimeStart_OK",
    "test_GLUE2EndpointDowntimeEnd_OK",
    "test_GLUE2StorageServiceCapacityTotalSize_OK",
    "test_GLUE2StorageServiceCapacityFreeSize_OK",
    "test_GLUE2StorageServiceCapacityUsedSize_OK",
    "test_GLUE2StorageServiceCapacityReservedSize_OK",
    "test_GLUE2StorageShareCapacityTotalSize_OK",
    "test_GLUE2StorageShareCapacityFreeSize_OK",
    "test_GLUE2StorageShareCapacityUsedSize_OK",
    "test_GLUE2ExecutionEnvironmentTotalInstances_MinRange",
    "test_GLUE2ExecutionEnvironmentTotalInstances_MaxRange",
    "test_GLUE2ExecutionEnvironmentUsedInstances_OK",
    "test_GLUE2ExecutionEnvironmentUnavailableInstances_OK",
    "test_GLUE2ExecutionEnvironmentPhysicalCPUs_MaxRange",
    "test_GLUE2ExecutionEnvironmentLogicalCPUs_MaxRange",
    "test_GLUE2ExecutionEnvironmentCPUTimeScalingFactor_MaxRange",
    "test_GLUE2ExecutionEnvironmentCPUTimeScalingFactor_MinRange",
    "test_GLUE2ExecutionEnvironmentWallTimeScalingFactor_MaxRange",
    "test_GLUE2ExecutionEnvironmentWallTimeScalingFactor_MinRange",
    "test_GLUE2StorageShareDefaultLifeTime_OK",
    "test_GLUE2StorageShareMaximumLifeTime_OK",
    "test_mandatory_attributes",
    "test_data_types",
)

# List of existing tests
# 'test_GLUE2EntityCreationTime_OK'
# 'test_GLUE2EntityValidity_OK'
# 'test_GLUE2EntityOtherInfo_OK'
# 'test_GLUE2LocationLongitude_OK'
# 'test_GLUE2LocationLatitude_OK'
# 'test_GLUE2ServiceID_OK'
# 'test_GLUE2ComputingServiceTotalJobs_OK'
# 'test_GLUE2ComputingServiceRunningJobs_OK'
# 'test_GLUE2ComputingServiceWaitingJobs_OK'
# 'test_GLUE2ComputingServiceStagingJobs_OK'
# 'test_GLUE2ComputingServiceSuspendedJobs_OK'
# 'test_GLUE2ComputingServicePreLRMSWaitingJobs_OK'
# 'test_GLUE2EndpointID_OK'
# 'test_GLUE2EndpointImplementationVersion_OK'
# 'test_GLUE2EndpointStartTime_OK'
# 'test_GLUE2EndpointIssuerCA_OK'
# 'test_GLUE2EndpointTrustedCA_OK'
# 'test_GLUE2EndpointDowntimeAnnounce_OK'
# 'test_GLUE2EndpointDowntimeAnnounce_checkStart'
# 'test_GLUE2EndpointDowntimeStart_OK'
# 'test_GLUE2EndpointDowntimeEnd_OK'
# 'test_GLUE2ComputingEndpointTotalJobs_OK'
# 'test_GLUE2ComputingEndpointRunningJobs_OK'
# 'test_GLUE2ComputingEndpointWaitingJobs_OK'
# 'test_GLUE2ComputingEndpointStagingJobs_OK'
# 'test_GLUE2ComputingEndpointSuspendedJobs_OK'
# 'test_GLUE2ComputingEndpointPreLRMSWaitingJobs_OK'
# 'test_GLUE2ComputingShareMaxWallTime_OK'
# 'test_GLUE2ComputingShareMaxMultiSlotWallTime_OK'
# 'test_GLUE2ComputingShareDefaultWallTime_OK'
# 'test_GLUE2ComputingShareMinWallTime_OK'
# 'test_GLUE2ComputingShareDefaultWallTime_MaxRange'
# 'test_GLUE2ComputingShareDefaultWallTime_MinRange'
# 'test_GLUE2ComputingShareMaxCPUTime_OK'
# 'test_GLUE2ComputingShareMaxTotalCPUTime_OK'
# 'test_GLUE2ComputingShareDefaultCPUTime_OK'
# 'test_GLUE2ComputingShareMinCPUTime_OK'
# 'test_GLUE2ComputingShareDefaultCPUTime_MaxRange'
# 'test_GLUE2ComputingShareDefaultCPUTime_MinRange'
# 'test_GLUE2ComputingShareMaxTotalJobs_default'
# 'test_GLUE2ComputingShareMaxTotalJobs_zero'
# 'test_GLUE2ComputingShareMaxTotalJobs_OK'
# 'test_GLUE2ComputingShareMaxUserRunningJobs_zero'
# 'test_GLUE2ComputingShareMaxUserRunningJobs_OK'
# 'test_GLUE2ComputingShareMaxRunningJobs_OK'
# 'test_GLUE2ComputingShareMaxWaitingJobs_OK'
# 'test_GLUE2ComputingShareMaxSlotsPerJob_zero'
# 'test_GLUE2ComputingShareTotalJobs_OK'
# 'test_GLUE2ComputingShareRunningJobs_OK'
# 'test_GLUE2ComputingShareLocalRunningJobs_OK'
# 'test_GLUE2ComputingShareWaitingJobs_OK'
# 'test_GLUE2ComputingShareLocalWaitingJobs_OK'
# 'test_GLUE2ComputingShareSuspendedJobs_OK'
# 'test_GLUE2ComputingShareLocalSuspendedJobs_OK'
# 'test_GLUE2ComputingShareStagingJobs_OK'
# 'test_GLUE2ComputingSharePreLRMSWaitingJobs_OK'
# 'test_GLUE2ComputingShareMaxMainMemory_MinRange'
# 'test_GLUE2ComputingShareMaxMainMemory_MaxRange'
# 'test_GLUE2ComputingShareGuaranteedMainMemory_MinRange'
# 'test_GLUE2ComputingShareGuaranteedMainMemory_MaxRange'
# 'test_GLUE2ComputingShareMaxVirtualMemory_MinRange'
# 'test_GLUE2ComputingShareMaxVirtualMemory_MaxRange'
# 'test_GLUE2ComputingShareGuaranteedVirtualMemory_MinRange'
# 'test_GLUE2ComputingShareGuaranteedVirtualMemory_MaxRange'
# 'test_GLUE2ComputingShareEstimatedAverageWaitingTime_OK'
# 'test_GLUE2ComputingShareEstimatedWorstWaitingTime_OK'
# 'test_GLUE2ComputingShareFreeSlots_OK'
# 'test_GLUE2ComputingShareUsedSlots_OK'
# 'test_GLUE2ComputingShareRequestedSlots_OK'
# 'test_GLUE2ComputingManagerTotalLogicalCPUs_MinRange'
# 'test_GLUE2ComputingManagerTotalLogicalCPUs_MaxRange'
# 'test_GLUE2ComputingManagerTotalPhysicalCPUs_OK'
# 'test_GLUE2ComputingManagerTotalPhysicalCPUs_MinRange'
# 'test_GLUE2ComputingManagerTotalPhysicalCPUs_MaxRange'
# 'test_GLUE2ComputingManagerTotalSlots_OK'
# 'test_GLUE2ComputingManagerTotalSlots_MinRange'
# 'test_GLUE2ComputingManagerTotalSlots_MaxRange'
# 'test_GLUE2ComputingManagerSlotsUsedByLocalJobs_OK'
# 'test_GLUE2ComputingManagerSlotsUsedByGridJobs_OK'
# 'test_GLUE2ComputingManagerWorkingAreaTotal_OK'
# 'test_GLUE2ComputingManagerWorkingAreaFree_OK'
# 'test_GLUE2ComputingManagerWorkingAreaMultiSlotTotal_OK'
# 'test_GLUE2ComputingManagerWorkingAreaMultiSlotFree_OK'
# 'test_GLUE2ComputingManagerCacheTotal_OK'
# 'test_GLUE2ComputingManagerCacheFree_OK'
# 'test_GLUE2ExecutionEnvironmentTotalInstances_MinRange'
# 'test_GLUE2ExecutionEnvironmentTotalInstances_MaxRange'
# 'test_GLUE2ExecutionEnvironmentUsedInstances_OK'
# 'test_GLUE2ExecutionEnvironmentUnavailableInstances_OK'
# 'test_GLUE2ExecutionEnvironmentPhysicalCPUs_MaxRange'
# 'test_GLUE2ExecutionEnvironmentLogicalCPUs_MaxRange'
# 'test_GLUE2ExecutionEnvironmentCPUClockSpeed_MaxRange'
# 'test_GLUE2ExecutionEnvironmentCPUClockSpeed_MinRange'
# 'test_GLUE2ExecutionEnvironmentCPUTimeScalingFactor_MaxRange'
# 'test_GLUE2ExecutionEnvironmentCPUTimeScalingFactor_MinRange'
# 'test_GLUE2ExecutionEnvironmentWallTimeScalingFactor_MaxRange'
# 'test_GLUE2ExecutionEnvironmentWallTimeScalingFactor_MinRange'
# 'test_GLUE2ExecutionEnvironmentMainMemorySize_MaxRange'
# 'test_GLUE2ExecutionEnvironmentMainMemorySize_MinRange'
# 'test_GLUE2ExecutionEnvironmentVirtualMemorySize_MaxRange'
# 'test_GLUE2ExecutionEnvironmentVirtualMemorySize_MinRange'
# 'test_GLUE2ApplicationEnvironmentRemovalDate_OK'
# 'test_GLUE2ApplicationEnvironmentMaxSlots_OK'
# 'test_GLUE2ApplicationEnvironmentMaxJobs_OK'
# 'test_GLUE2ApplicationEnvironmentMaxUserSeats_OK'
# 'test_GLUE2ApplicationEnvironmentFreeSlots_OK'
# 'test_GLUE2ApplicationEnvironmentFreeJobs_OK'
# 'test_GLUE2ApplicationEnvironmentFreeUserSeats_OK'
# 'test_GLUE2StorageServiceCapacityTotalSize_OK'
# 'test_GLUE2StorageServiceCapacityTotalSize_MinRange'
# 'test_GLUE2StorageServiceCapacityTotalSize_MaxRange'
# 'test_GLUE2StorageServiceCapacityFreeSize_OK'
# 'test_GLUE2StorageServiceCapacityUsedSize_OK'
# 'test_GLUE2StorageServiceCapacityReservedSize_OK'
# 'test_GLUE2StorageShareAccessLatency_OK'
# 'test_GLUE2StorageShareDefaultLifeTime_OK'
# 'test_GLUE2StorageShareMaximumLifeTime_OK'
# 'test_GLUE2StorageShareCapacityTotalSize_OK'
# 'test_GLUE2StorageShareCapacityTotalSize_MinRange'
# 'test_GLUE2StorageShareCapacityTotalSize_MaxRange'
# 'test_GLUE2StorageShareCapacityFreeSize_OK'
# 'test_GLUE2StorageShareCapacityUsedSize_OK'
# 'test_GLUE2ToComputingServiceBandwidth_MinRange'
# 'test_GLUE2ToComputingServiceBandwidth_MaxRange'
