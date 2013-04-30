messages = {
"E001" : ( "Creation time in the future", "GLUE2EntityCreationTime" ), 
"E002" : ( "Obsolete entry", "GLUE2EntityValidity" ),
"E003" : ( "Wrong share percentage", "GLUE2EntityOtherInfo" ),
"E004" : ( "VO appears more than once in share", "GLUE2EntityOtherInfo" ),
"E005" : ( "Wrong share format", "GLUE2EntityOtherInfo" ),
"E006" : ( "Wrong attribute format", "GLUE2EntityOtherInfo" ),
"E007" : ( "Total published shares > 100%", "GLUE2EntityOtherInfo" ),
"E008" : ( "Longitude out of range", "GLUE2LocationLongitude" ),
"E009" : ( "Latitude out of range", "GLUE2LocationLatitude" ),
"E010" : ( "Start time in the future", "GLUE2EndpointStartTime" ),
"E011" : ( "Downtime announcement in the future", "GLUE2EndpointDowntimeAnnounce" ),
"E012" : ( "Downtime start time is older than end time", "GLUE2EndpointDowntimeStart" ),
"E013" : ( "Downtime end time is published without a start time", "GLUE2EndpointDowntimeEnd" ),
"E014" : ( "Incoherent number of total capacity", "GLUE2StorageServiceCapacityTotalSize" ),
"E015" : ( "Incoherent attribute range", "GLUE2StorageServiceCapacityFreeSize" ),
"E016" : ( "Incoherent attribute range", "GLUE2StorageServiceCapacityUsedSize" ),
"E017" : ( "Incoherent attribute range", "GLUE2StorageServiceCapacityReservedSize" ),
"E018" : ( "Incoherent number of total share capacity", "GLUE2StorageShareCapacityTotalSize" ),
"E019" : ( "Incoherent attribute range", "GLUE2StorageShareCapacityFreeSize" ),
"E020" : ( "Incoherent attribute range", "GLUE2StorageShareCapacityUsedSize" ),
"E021" : ( "The object class is not valid", "Several attributes" ),
"W001" : ( "Creation time more than one year old", "GLUE2EntityCreationTime" ),
"W002" : ( "GLUE2EntityValidity published when GLUE2EntityCreationTime is not published", "GLUE2EntityValidity" ),
"W003" : ( "Unknown profile name", "GLUE2EntityOtherInfo" ),
"W004" : ( "Incorrect profile version", "GLUE2EntityOtherInfo" ),
"W005" : ( "Incoherent number of total jobs", "GLUE2ComputingServiceTotalJobs" ),
"W006" : ( "Start time more than two years old", "GLUE2EndpointStartTime" ),
"W007" : ( "Downtime announce more than one year old", "GLUE2EndpointDowntimeAnnounce" ),
"W008" : ( "Downtime announcement with no Downtime start published", "GLUE2EndpointDowntimeAnnounce" ),
"W009" : ( "Downtime start time is scheduled more than one year ahead", "GLUE2EndpointDowntimeStart" ),
"W010" : ( "Downtime start time more than one year old", "GLUE2EndpointDowntimeStart" ),
"W011" : ( "Downtime end time is scheduled more than one year ahead", "GLUE2EndpointDowntimeEnd" ),
"W012" : ( "Downtime end time is more than one week old", "GLUE2EndpointDowntimeEnd" ),
"W013" : ( "Incoherent number of total jobs", "GLUE2ComputingEndpointTotalJobs" ),
"W014" : ( "Incoherent attribute range", "GLUE2ComputingShareMinWallTime" ),
"W015" : ( "Attribute out of predefined range", "GLUE2ComputingShareDefaultWallTime" ),
"W016" : ( "Attribute out of predefined range", "GLUE2ComputingShareDefaultWallTime" ),
"W017" : ( "Incoherent attribute range", "GLUE2ComputingShareMinCPUTime" ),
"W018" : ( "Attribute out of predefined range", "GLUE2ComputingShareDefaultCPUTime" ),
"W019" : ( "Attribute out of predefined range", "GLUE2ComputingShareDefaultCPUTime" ),
"W020" : ( "Number of total jobs is zero", "GLUE2ComputingShareMaxTotalJobs" ),
"W021" : ( "Attribute out of predefined range", "GLUE2ComputingShareMaxTotalJobs" ),
"W022" : ( "Number of jobs is zero", "GLUE2ComputingShareMaxUserRunningJobs" ),
"W023" : ( "Incoherent attribute range", "GLUE2ComputingShareMaxUserRunningJobs" ),
"W024" : ( "Number of maximum slots per job is zero", "GLUE2ComputingShareMaxSlotsPerJob" ),
"W025" : ( "Incoherent number of total jobs", "GLUE2ComputingShareTotalJobs" ),
"W026" : ( "Memory lower than 100 MB", "GLUE2ComputingShareMaxMainMemory" ),
"W027" : ( "Incoherent attribute range", "GLUE2ComputingShareGuaranteedMainMemory" ),
"W028" : ( "Incoherent attribute range", "GLUE2ComputingShareMaxVirtualMemory" ),
"W029" : ( "Incoherent attribute range", "GLUE2ComputingShareGuaranteedVirtualMemory" ),
"W030" : ( "Incoherent attribute range", "GLUE2ComputingManagerTotalPhysicalCPUs" ),
"W031" : ( "Incoherent attribute range", "GLUE2ComputingManagerTotalSlots" ),
"W032" : ( "Incoherent attribute range", "GLUE2ComputingManagerSlotsUsedByLocalJobs" ),
"W033" : ( "Incoherent attribute range", "GLUE2ComputingManagerSlotsUsedByGridJobs" ),
"W034" : ( "Mandatory attribute not present", "Several attributes" ),
"W035" : ( "Undesirable attribute is present", "Several attributes" ),
"W036" : ( "Single valued attribute with more than one value", "Several attributes" ),
"W037" : ( "Wrong type", "Several attributes" ),
"W038" : ( "Empty attribute", "Several attributes" ),
"I001" : ( "Unknown Grid Infrastructure name", "GLUE2EntityOtherInfo" ),
"I002" : ( "Unknown configuration tool", "GLUE2EntityOtherInfo" ),
"I003" : ( "Unknown EGI NGI", "GLUE2EntityOtherInfo" ),
"I004" : ( "Incorrect blog URL", "GLUE2EntityOtherInfo" ),
"I005" : ( "Incorrect icon URL", "GLUE2EntityOtherInfo" ),
"I006" : ( "Unknown WLCG Tier", "GLUE2EntityOtherInfo" ),
"I007" : ( "Unknown WLCG Name", "GLUE2EntityOtherInfo" ),
"I008" : ( "Incorrect icon WLCG name icon URL", "GLUE2EntityOtherInfo" ),
"I009" : ( "Unknown middleware name", "GLUE2EntityOtherInfo" ),
"I010" : ( "Incorrect middleware version", "GLUE2EntityOtherInfo" ),
"I011" : ( "Incorrect DN syntax", "GLUE2EntityOtherInfo" ),
"I012" : ( "Unknown VO name in share", "GLUE2EntityOtherInfo" ),
"I013" : ( "Unknown benchmark name in share", "GLUE2EntityOtherInfo" ),
"I014" : ( "Number of jobs higher than 1 million", "GLUE2ComputingServiceRunningJobs" ),
"I015" : ( "Number of jobs higher than 1 million", "GLUE2ComputingServiceWaitingJobs" ),
"I016" : ( "Number of jobs higher than 1 million", "GLUE2ComputingServiceStagingJobs" ),
"I017" : ( "Number of jobs higher than 1 million", "GLUE2ComputingServiceSuspendedJobs" ),
"I018" : ( "Number of jobs higher than 1 million", "GLUE2ComputingServicePreLRMSWaitingJobs" ),
"I019" : ( "Issuer CA published as 'unknown'", "GLUE2EndpointIssuerCA" ),
"I020" : ( "Trusted CA published as 'unknown'", "GLUE2EndpointTrustedCA" ),
"I021" : ( "Number of jobs higher than 1 million", "GLUE2ComputingEndpointRunningJobs" ),
"I022" : ( "Number of jobs higher than 1 million", "GLUE2ComputingEndpointWaitingJobs" ),
"I023" : ( "Number of jobs higher than 1 million", "GLUE2ComputingEndpointStagingJobs" ),
"I024" : ( "Number of jobs higher than 1 million", "GLUE2ComputingEndpointSuspendedJobs" ),
"I025" : ( "Number of jobs higher than 1 million", "GLUE2ComputingEndpointPreLRMSWaitingJobs" ),
"I026" : ( "Default value published", "GLUE2ComputingShareMaxWallTime" ),
"I027" : ( "Default value published", "GLUE2ComputingShareMaxMultiSlotWallTime" ),
"I028" : ( "Default value published", "GLUE2ComputingShareDefaultWallTime" ),
"I029" : ( "Default value published", "GLUE2ComputingShareMaxCPUTime" ),
"I030" : ( "Default value published", "GLUE2ComputingShareMaxTotalCPUTime" ),
"I031" : ( "Default value published", "GLUE2ComputingShareDefaultCPUTime" ),
"I032" : ( "Default value published", "GLUE2ComputingShareMaxTotalJobs" ),
"I033" : ( "Default value published", "GLUE2ComputingShareMaxRunningJobs" ),
"I034" : ( "Default value published", "GLUE2ComputingShareMaxWaitingJobs" ),
"I035" : ( "Number of jobs higher than 1 million", "GLUE2ComputingShareRunningJobs" ),
"I036" : ( "Number of jobs higher than 1 million", "GLUE2ComputingShareLocalRunningJobs" ),
"I037" : ( "Number of jobs higher than 1 million", "GLUE2ComputingShareWaitingJobs" ),
"I038" : ( "Number of jobs higher than 1 million", "GLUE2ComputingShareLocalWaitingJobs" ),
"I039" : ( "Number of jobs higher than 1 million", "GLUE2ComputingShareSuspendedJobs" ),
"I040" : ( "Number of jobs higher than 1 million", "GLUE2ComputingShareLocalSuspendedJobs" ),
"I041" : ( "Number of jobs higher than 1 million", "GLUE2ComputingShareStagingJobs" ),
"I042" : ( "Number of jobs higher than 1 million", "GLUE2ComputingSharePreLRMSWaitingJobs" ),
"I043" : ( "Memory higher than 100,000 MB", "GLUE2ComputingShareMaxMainMemory" ),
"I044" : ( "Memory higher than 100,000 MB", "GLUE2ComputingShareGuaranteedMainMemory" ),
"I045" : ( "Memory higher than 100,000 MB", "GLUE2ComputingShareMaxVirtualMemory" ),
"I046" : ( "Number of seconds higher than 1 million", "GLUE2ComputingShareEstimatedAverageWaitingTime" ),
"I047" : ( "Number of seconds higher than 1 million", "GLUE2ComputingShareEstimatedWorstWaitingTime" ),
"I048" : ( "Number of slots higher than 1 million", "GLUE2ComputingShareFreeSlots" ),
"I049" : ( "Number of slots higher than 1 million", "GLUE2ComputingShareUsedSlots" ),
"I050" : ( "Number of slots higher than 1 million", "GLUE2ComputingShareRequestedSlots" ),
"I051" : ( "Number of logical CPUs lower than 10", "GLUE2ComputingManagerTotalLogicalCPUs" ),
"I052" : ( "Number of logical CPUs greater than 1 million", "GLUE2ComputingManagerTotalLogicalCPUs" ),
"I053" : ( "Number of physical CPUs lower than 10", "GLUE2ComputingManagerTotalPhysicalCPUs" ),
"I054" : ( "Number of logical CPUs greater than 1 million", "GLUE2ComputingManagerTotalPhysicalCPUs" ),
"I055" : ( "Number of total slots lower than 10", "GLUE2ComputingManagerTotalSlots" ),
"I056" : ( "Number of total slots greater than 1 million", "GLUE2ComputingManagerTotalSlots" ),
"I057" : ( "Total working area greater than 1 million GB", "GLUE2ComputingManagerWorkingAreaTotal" ),
"I058" : ( "Free working area greater than 1 million GB", "GLUE2ComputingManagerWorkingAreaFree" ),
"I059" : ( "Multi slot working area greater than 1 million GB", "GLUE2ComputingManagerWorkingAreaMultiSlotTotal" ),
"I060" : ( "Multi slot free working area greater than 1 million GB", "GLUE2ComputingManagerWorkingAreaMultiSlotFree" ),
"I061" : ( "Total cache greater than 1 million GB", "GLUE2ComputingManagerCacheTotal" ),
"I062" : ( "Free cache greater than 1 million GB", "GLUE2ComputingManagerCacheFree" ),
"I063" : ( "Total instances less than 10", "GLUE2ExecutionEnvironmentTotalInstances" ),
"I064" : ( "Total instances more than 1 million", "GLUE2ExecutionEnvironmentTotalInstances" ),
"I065" : ( "Incoherent attribute range", "GLUE2ExecutionEnvironmentUsedInstances" ),
"I066" : ( "Incoherent attribute range", "GLUE2ExecutionEnvironmentUnavailableInstances" ),
"I067" : ( "Number of physical CPUs greater than 10", "GLUE2ExecutionEnvironmentPhysicalCPUs" ),
"I068" : ( "Number of logical CPUs greater than 1000", "GLUE2ExecutionEnvironmentLogicalCPUs" ),
"I069" : ( "CPU clock speed greater than 1000", "GLUE2ExecutionEnvironmentCPUClockSpeed" ),
"I070" : ( "CPU clock speed less than 100", "GLUE2ExecutionEnvironmentCPUClockSpeed" ),
"I071" : ( "CPU time scaling factor greater than 1", "GLUE2ExecutionEnvironmentCPUTimeScalingFactor" ),
"I072" : ( "CPU time scaling factor less than 0.1", "GLUE2ExecutionEnvironmentCPUTimeScalingFactor" ),
"I073" : ( "Wall time scaling factor greater than 1", "GLUE2ExecutionEnvironmentWallTimeScalingFactor" ),
"I074" : ( "Wall time scaling factor less than 0.1", "GLUE2ExecutionEnvironmentWallTimeScalingFactor" ),
"I075" : ( "Main memory size greater than 1 million MB", "GLUE2ExecutionEnvironmentMainMemorySize" ),
"I076" : ( "Main memory size less than 100 MB", "GLUE2ExecutionEnvironmentMainMemorySize" ),
"I077" : ( "Virtual memory size greater than 1 million MB", "GLUE2ExecutionEnvironmentVirtualMemorySize" ),
"I078" : ( "Virtual memory size less than 100 MB", "GLUE2ExecutionEnvironmentVirtualMemorySize" ),
"I079" : ( "Removal date in the past", "GLUE2ApplicationEnvironmentRemovalDate" ),
"I080" : ( "Number of maximum slots is zero", "GLUE2ApplicationEnvironmentMaxSlots" ),
"I081" : ( "Number of maximum jobs is zero", "GLUE2ApplicationEnvironmentMaxJobs" ),
"I082" : ( "Number of maximum user seats is zero", "GLUE2ApplicationEnvironmentMaxUserSeats" ),
"I083" : ( "Incoherent attribute range", "GLUE2ApplicationEnvironmentFreeSlots" ),
"I084" : ( "Incoherent attribute range", "GLUE2ApplicationEnvironmentFreeJobs" ),
"I085" : ( "Incoherent attribute range", "GLUE2ApplicationEnvironmentFreeUserSeats" ),
"I086" : ( "Total capacity size less than 1000 GB", "GLUE2StorageServiceCapacityTotalSize" ),
"I087" : ( "Total capacity size greater than 1 million GB", "GLUE2StorageServiceCapacityTotalSize" ),
"I088" : ( "Access latency is 'offline'", "GLUE2StorageShareAccessLatency" ),
"I089" : ( "Default life time less than 100000 seconds", "GLUE2StorageShareDefaultLifeTime" ),
"I090" : ( "Maximum life time less than 100000 seconds", "GLUE2StorageShareMaximumLifeTime" ),
"I091" : ( "Total share capacity size less than 1000 GB", "GLUE2StorageShareCapacityTotalSize" ),
"I092" : ( "Total share capacity size greater than 1 million GB", "GLUE2StorageShareCapacityTotalSize" ),
"I093" : ( "Bandwidth less than 100", "GLUE2ToComputingServiceBandwidth" ),
"I094" : ( "Bandwidth greater than 100000", "GLUE2ToComputingServiceBandwidth" ),
"I095" : ( "Recommended attribute not present", "Several attributes" )
}