schema = {
    "Mds": {},
    "organization": {
        "o": ("String", True, True),
    },
    "GlueTop": {},
    "GlueCETop": {},
    "GlueSETop": {},
    "GlueSATop": {},
    "GlueGeneralTop": {},
    "GlueClusterTop": {},
    "GlueKey": {},
    "GlueSchemaVersion": {},
    "GlueInformationService": {},
    "GlueSite": {
        "GlueSiteUniqueID": ("String", True, True),
        "GlueSiteName": ("String", True, False),
        "GlueSiteDescription": ("String", True, True),
        "GlueSiteEmailContact": ("Email_t", True, False),
        "GlueSiteUserSupportContact": ("Email_t", True, False),
        "GlueSiteSysAdminContact": ("Email_t", True, False),
        "GlueSiteSecurityContact": ("Email_t", True, False),
        "GlueSiteLocation": ("String", True, True),
        "GlueSiteLatitude": ("Real32", True, True),
        "GlueSiteLongitude": ("Real32", True, True),
        "GlueSiteWeb": ("URL", True, True),
        "GlueSiteSponsor": ("String", False, False),
        "GlueSiteOtherInfo": ("String", False, False),
    },
    "GlueService": {
        "GlueServiceUniqueID": ("String", True, True),
        "GlueServiceName": ("String", True, False),
        "GlueServiceType": ("ServiceType_t", True, False),
        "GlueServiceVersion": ("String", True, False),
        "GlueServiceEndpoint": ("URL", True, False),
        "GlueServiceStatus": ("String", True, False),
        "GlueServiceStatusInfo": ("String", True, False),
        "GlueServiceWSDL": ("String", True, False),
        "GlueServiceSemantics": ("URL", True, False),
        "GlueServiceStartTime": ("DateTime_t", True, False),
        "GlueServiceOwner": ("String", False, False),
        "GlueServiceAccessControlBaseRule": ("ACBR_t", False, False),
    },
    "GlueServiceData": {
        "GlueServiceDataKey": ("String", True, True),
        "GlueServiceDataValue": ("String", True, False),
    },
    "GlueCluster": {
        "GlueClusterUniqueID": ("String", True, True),
        "GlueClusterName": ("String", True, False),
        "GlueClusterTmpDir": ("String", True, False),
        "GlueClusterWNTmpDir": ("String", True, False),
    },
    "GlueCE": {
        "GlueCEUniqueID": ("String", True, True),
        "GlueCEName": ("String", True, True),
        "GlueCEImplementationName": ("String", True, True),
        "GlueCEImplementationVersion": ("String", True, True),
        "GlueCECapability": ("String", False, True),
    },
    "GlueCEInfo": {
        "GlueCEInfoLRMSType": ("lrms_t", True, False),
        "GlueCEInfoLRMSVersion": ("String", True, False),
        "GlueCEInfoGRAMVersion": ("String", True, False),
        "GlueCEInfoHostName": ("String", True, False),
        "GlueCEInfoGatekeeperPort": ("Int32", True, False),
        "GlueCEInfoJobManager": ("String", True, False),
        "GlueCEInfoContactString": ("String", True, False),
        "GlueCEInfoTotalCPUs": ("Int32", True, False),
        "GlueCEInfoApplicationDir": ("String", True, False),
        "GlueCEInfoDataDir": ("String", True, False),
        "GlueCEInfoDefaultSE": ("String", True, False),
    },
    "GlueCEState": {
        "GlueCEStateRunningJobs": ("Int32", True, False),
        "GlueCEStateWaitingJobs": ("Int32", True, False),
        "GlueCEStateTotalJobs": ("Int32", True, True),
        "GlueCEStateEstimatedResponseTime": ("Int32", True, False),
        "GlueCEStateWorstResponseTime": ("Int32", True, False),
        "GlueCEStateFreeJobSlots": ("Int32", True, False),
        "GlueCEStateFreeCPUs": ("Int32", True, False),
        "GlueCEStateStatus": ("String", True, False),
    },
    "GlueCEPolicy": {
        "GlueCEPolicyMaxWallClockTime": ("Int32", True, False),
        "GlueCEPolicyMaxObtainableWallClockTime": ("Int32", True, False),
        "GlueCEPolicyMaxCPUTime": ("Int32", True, False),
        "GlueCEPolicyMaxObtainableCPUTime": ("Int32", True, False),
        "GlueCEPolicyMaxTotalJobs": ("Int32", True, False),
        "GlueCEPolicyMaxRunningJobs": ("Int32", True, False),
        "GlueCEPolicyMaxWaitingJobs": ("Int32", True, False),
        "GlueCEPolicyPriority": ("Int32", True, False),
        "GlueCEPolicyAssignedJobSlots": ("Int32", True, False),
        "GlueCEPolicyMaxSlotsPerJobs": ("Int32", True, False),
        "GlueCEPolicyPreemption": ("Int32", True, False),
    },
    "GlueCEAccessControlBase": {
        "GlueCEAccessControlBaseRule": ("ACBR_t", False, True),
    },
    "GlueVOView": {
        "GlueVOViewLocalID": ("String", True, True),
    },
    "GlueSubCluster": {
        "GlueSubClusterUniqueID": ("String", True, True),
        "GlueSubClusterName": ("String", True, True),
        "GlueSubClusterPhysicalCPUs": ("Int32", True, True),
        "GlueSubClusterLogicalCPUs": ("Int32", True, True),
    },
    "GlueHost": {
        "GlueHostProperty": ("String", True, True),
    },
    "GlueHostOperatingSystem": {
        "GlueHostOperatingSystemName": ("String", True, False),
        "GlueHostOperatingSystemRelease": ("String", True, False),
        "GlueHostOperatingSystemVersion": ("String", True, False),
    },
    "GlueHostProcessor": {
        "GlueHostProcessorModel": ("String", True, False),
        "GlueHostProcessorVersion": ("String", True, False),
        "GlueHostProcessorVendor": ("String", True, False),
        "GlueHostProcessorClockSpeed": ("Int32", True, False),
        "GlueHostProcessorInstructionSet": ("String", True, False),
        "GlueHostProcessorOtherDescription": ("String", True, False),
    },
    "GlueHostMainMemory": {
        "GlueHostMainMemoryRAMSize": ("Int32", True, True),
        "GlueHostMainMemoryVirtualSize": ("Int32", True, True),
    },
    "GlueHostNetworkAdapter": {
        "GlueHostNetworkAdapterOutboundIP": ("Boolean", True, True),
        "GlueHostNetworkAdapterInboundIP": ("Boolean", True, True),
    },
    "GlueHostArchitecture": {
        "GlueHostArchitecturePlatformType": ("String", True, True),
        "GlueHostArchitectureSMPSize": ("Int32", True, True),
    },
    "GlueHostBenchmark": {
        "GlueHostBenchmarkSI00": ("Int32", True, True),
        "GlueHostBenchmarkSF00": ("Int32", True, True),
    },
    "GlueHostApplicationSoftware": {
        "GlueHostApplicationSoftwareRunTimeEnvironment": ("String", False, False),
    },
    "GlueLocation": {},
    "GlueSE": {
        "GlueSEUniqueID": ("String", True, True),
        "GlueSEName": ("String", True, False),
        "GlueSEArchitecture": ("SEArch_t", True, False),
        "GlueSESizeTotal": ("Int32", True, False),
        "GlueSESizeFree": ("Int32", True, False),
        "GlueSEPort": ("Int32", True, False),
        "GlueSEStateCurrentIOLoad": ("String", True, False),
        "GlueSEImplementationName": ("SSImpl_t", True, False),
        "GlueSEImplementationVersion": ("String", True, False),
        "GlueSEStatus": ("SEStatus_t", True, False),
        "GlueSETotalOnlineSize": ("Int32", True, False),
        "GlueSETotalNearlineSize": ("Int32", True, False),
        "GlueSEUsedOnlineSize": ("Int32", True, False),
        "GlueSEUsedNearlineSize": ("Int32", True, False),
    },
    "GlueSA": {
        "GlueSALocalID": ("String", True, True),
        "GlueSARoot": ("String", True, False),
        "GlueSAPath": ("String", True, False),
        "GlueSAType": ("SAType_t", True, False),
        "GlueSAAccessControlBase.Rule": ("ACBR_t", True, False),
        "GlueSAName": ("String", True, False),
        "GlueSATotalOnlineSize": ("Int32", True, False),
        "GlueSAUsedOnlineSize": ("Int32", True, False),
        "GlueSAFreeOnlineSize": ("Int32", True, False),
        "GlueSAReservedOnlineSize": ("Int32", True, False),
        "GlueSATotalNearlineSize": ("Int32", True, False),
        "GlueSAUsedNearlineSize": ("Int32", True, False),
        "GlueSAFreeNearlineSize": ("Int32", True, False),
        "GlueSAReservedNearlineSize": ("Int32", True, False),
        "GlueSARetentionPolicy": ("RetentionPolicy_t", True, False),
        "GlueSAAccessLatency": ("AccessLatency_t", True, False),
        "GlueSAExpirationMode": ("ExpirationMode_t", True, False),
        "GlueSACapability": ("String", False, True),
    },
    "GlueSAPolicy": {
        "GlueSAPolicyQuota": ("Int32", True, False),
        "GlueSAPolicyMinFileSize": ("Int32", True, False),
        "GlueSAPolicyMaxFileSize": ("Int32", True, False),
        "GlueSAPolicyMaxData": ("Int32", True, False),
        "GlueSAPolicyMaxNumFiles": ("Int32", True, False),
        "GlueSAPolicyMaxPinDuration": ("Int32", True, False),
        "GlueSAPolicyFileLifeTime": ("String", True, False),
    },
    "GlueSAState": {
        "GlueSAStateUsedSpace": ("Int32", True, False),
        "GlueSAStateAvailableSpace": ("Int32", True, False),
    },
    "GlueSAAccessControlBase": {},
    "GlueSEControlProtocol": {
        "GlueSEControlProtocolLocalID": ("String", True, True),
        "GlueSEControlProtocolEndpoint": ("URL", True, False),
        "GlueSEControlProtocolType": ("ControlProtocol_t", True, False),
        "GlueSEControlProtocolVersion": ("String", True, False),
        "GlueSEControlProtocolCapability": ("String", False, False),
    },
    "GlueSEAccessProtocol": {
        "GlueSEAccessProtocolLocalID": ("String", True, True),
        "GlueSEAccessProtocolEndpoint": ("URL", True, False),
        "GlueSEAccessProtocolType": ("AccessProtocol_t", True, False),
        "GlueSEAccessProtocolVersion": ("String", True, False),
        "GlueSEAccessProtocolCapability": ("String", False, False),
        "GlueSEAccessProtocolSupportedSecurity": ("String", False, False),
        "GlueSEAccessProtocolPort": ("Int32", True, False),
        "GlueSEAccessProtocolAccessTime": ("Int32", True, False),
        "GlueSEAccessProtocolMaxStreams": ("Int32", True, False),
    },
    "GlueVOInfo": {
        "GlueVOInfoLocalID": ("String", True, True),
        "GlueVOInfoName": ("String", True, False),
        "GlueVOInfoPath": ("String", True, False),
        "GlueVOInfoTag": ("String", True, False),
    },
    "GlueCESEBindGroup": {},
    "GlueCESEBind": {},
}
