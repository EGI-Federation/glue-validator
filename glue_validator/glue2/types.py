import re

import glue_validator.glue2.data

MAX_INT32 = 2**31 - 1
MAX_INT64 = 2**63 - 1
MAX_UINT32 = 2**32 - 1
MAX_UINT64 = 2**64 - 1


def is_DN_t(value):
    return is_String(value)


def is_LocalID_t(value):
    return is_String(value)


def is_ObjectClass(value):
    if value in glue_validator.glue2.data.schema:
        return True
    else:
        return False


def is_String(value):
    if value == "":
        return False
    else:
        return True


def is_ExtendedBoolean_t(value):
    value = value.lower()
    if value in ["false", "true", "undefined"]:
        return True
    else:
        return False


def is_URI(value):
    return is_String(value)
    # RFC 3986: http://www.ietf.org/rfc/rfc3986.txt
    # Check URL (subtype of URI)
    # uri = "^[a-zA-Z][a-zA-Z0-9+-.]*://[a-zA-Z0-9_.]+(:[0-9]+)*
    #       (/[a-zA-Z0-9_]*)*(\?[a-zA-Z0-9+-:@?./]+)?(#[a-zA-Z0-9+-:#@?./]+)?$"
    # if re.match(uri, value):
    #     return True
    # else:
    #     # Check other URIs
    #     uri = "^[a-zA-Z][a-zA-Z0-9+-.@:]*:[a-zA-Z0-9+-.@:]*$"
    #     if re.match(uri, value):
    #         return True
    #     else:
    #         return False


def is_URL(value):
    # RFC 1738: http://www.ietf.org/rfc/rfc1738.txt
    # Protocols accepted: see is_allowed_URL_Schema
    # Protocols rejected on purpose: gopher|news|nntp|telnet|mailto|file|etc.
    url = (
        "(?:(?:([a-z0-9+.-]+)://)|(www\\.))+(([a-zA-Z0-9\\._-]+\\.[a-zA-Z]{2,6})"
        "|([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}))"
        "(/[a-zA-Z0-9\\&amp;%_\\./-~-]*)?"
    )
    m = re.match(url, value)
    if m is None:
        return False
    return is_allowed_URL_Schema(m.group(1))


def is_allowed_URL_Schema(value):
    types = [
        "http",
        "ftp",
        "https",
        "ftps",
        "sftp",
        "gsiftp",
        "xroot",
        "dcap",
        "gsidcap",
        "httpg",
        "ldap",
        "voms",
        "myproxy",
        "lfc",
    ]
    if value in types:
        return True
    else:
        return False


def is_Real32(value):
    # IEE 754-2008: http://en.wikipedia.org/wiki/IEEE_754-2008
    # I just check it is a floating point number
    floatingpoint = "-*[0-9]+(.[0-9]+)*"
    if re.match(floatingpoint, value):
        return True
    else:
        return False


def is_ContactType_t(value):
    value = value.lower()
    if value in ["general", "security", "sysadmin", "usersupport"]:
        return True
    else:
        return False


def is_Int32(value):
    # Check http://en.wikipedia.org/wiki/Integer_(computer_science)
    if re.match("^(?:[-+])?[0-9]+$", value):
        if -MAX_INT32 <= int(value) <= MAX_INT32:
            return True
        return False


def is_UInt32(value):
    # Check http://en.wikipedia.org/wiki/Integer_(computer_science)
    if re.match("^[0-9]+$", value):
        if int(value) <= MAX_UINT32:
            return True
        return False


def is_UInt64(value):
    # Check http://en.wikipedia.org/wiki/Integer_(computer_science)
    if re.match("^[0-9]+$", value):
        if int(value) <= MAX_UINT32:
            return True
        return False


def is_DateTime_t(value):
    # Check http://www.w3.org/TR/xmlschema-2/#dateTime
    dateTime = (
        "^-?[0-9]{4}-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1])"
        "T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z?$"
    )

    if re.match(dateTime, value):
        return True
    return False


def is_Email_t(email):
    if len(email) > 7:
        if re.match(
            "mailto:[ ]*.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\."
            "([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",
            email,
        ):
            return True
    return False


def is_QualityLevel_t(value):
    quality_levels = ["development", "pre-production", "production", "testing"]
    if value in quality_levels:
        return True
    else:
        return False


def is_InterfaceName_t(value):
    interfaces = [
        "ogf.bes",
        "ogf.srm",
        "org.ogf.bes",
        "org.ogf.glue.emies.activitycreation",
        "org.ogf.glue.emies.activitymanagement",
        "org.ogf.glue.emies.resourceinfo",
        "org.ogf.glue.emies.activityinfo",
        "org.ogf.glue.emies.delegation",
        "org.glite.Argus.PDP",
        "org.glite.Argus.PAP",
        "org.glite.Argus.PEP",
        "org.nordugrid.ldapglue1",
        "org.nordugrid.wsrfglue2",
        "org.nordugrid.ldapglue2",
        "org.nordugrid.gridftpjob",
        "org.nordugrid.ldapng",
    ]
    if value in interfaces:
        return True
    else:
        return is_ServiceType_t(value) or is_allowed_URL_Schema(value)


def is_PolicyScheme_t(value):
    schemes = ["basic", "gacl", "org.glite.standard"]
    if value in schemes:
        return True
    else:
        return False


def is_ServiceType_t(value):
    types = [
        "APEL",
        "BDII",
        "bdii_site",
        "bdii_top",
        "CE",
        "egi.GRIDVIEW",
        "egi.GSTAT",
        "egi.MetricsPortal",
        "egi.NetworkPortal",
        "egi.OpsPortal",
        "eu.egi.AccountingPortal",
        "eu.egi.APELRepository",
        "eu.egi.GGUS",
        "eu.egi.GOCDB",
        "eu.egi.MSGBroker",
        "gLExec",
        "gLite-APEL",
        "MDS-GIIS",
        "MyProxy",
        "ngi.OpsPortal",
        "OpenSSH",
        "org.dcache.storage",
        "org.glite.AMGA",
        "org.glite.Argus",
        "org.glite.argus",
        "org.glite.ce.CREAM",
        "org.glite.ce.Monitor",
        "org.glite.ChannelAgent",
        "org.glite.ChannelManagement",
        "org.glite.Delegation",
        "org.glite.FiremanCatalog",
        "org.glite.FileTransfer",
        "org.glite.FileTransferStats",
        "org.glite.fts",
        "org.glite.KeyStore",
        "org.glite.lb",
        "org.glite.lb.Server",
        "org.glite.Metadata",
        "org.glite.rgma.Registry",
        "org.glite.rgma.Schema",
        "org.glite.rgma.Browser",
        "org.glite.rgma.PrimaryProducer",
        "org.glite.rgma.SecondaryProducer",
        "org.glite.rgma.OnDemandProducer",
        "org.glite.RTEPublisher",
        "org.glite.SEIndex",
        "org.glite.voms",
        "org.glite.voms-admin",
        "org.glite.wms",
        "org.glite.wms.WMProxy",
        "org.irods.irods3",
        "org.lcg.Frontier",
        "org.lcg.Squid",
        "org.nordugrid.arex",
        "org.nordugrid.execution.arex",
        "org.nordugrid.information.egiis",
        "org.nordugrid.storage",
        "org.nordugrid.isis",
        "org.ogf.bes.BESFactory",
        "org.ogf.bes.BESManagement",
        "org.ogf.glue.emir",
        "pbs.torque.server",
        "pbs.torque.maui",
        "SGAS",
        "UI",
        "eu.unicore.USE",
        "unicore6.Registry",
        "unicore6.ServiceOrchestrator",
        "unicore6.StorageFactory",
        "unicore6.StorageManagement",
        "unicore6.TargetSystemFactory",
        "unicore6.UVOSAssertionQueryService",
        "unicore6.WorkflowFactory",
        "VOBOX",
        "xroot",
        "SRM",
        "data-location-interface",
        "edu.caltech.cacr.monalisa",
        "GridCat",
        "gridmap-file",
        "gsiftp",
        "GUMS",
        "it.infn.GridICE",
        "lcg-file-catalog",
        "lcg-local-file-catalog",
        "local-data-location-interface",
        "msg.broker.rest",
        "msg.broker.stomp",
        "msg.broker.stomp-ssl",
        "msg.broker.openwire",
        "msg.broker.openwire-ssl",
        "Nagios",
        "National-NAGIOS",
        "org.edg.gatekeeper",
        "org.lcg.Frontier",
        "org.lcg.Squid",
        "Project-NAGIOS",
        "Regional-NAGIOS",
        "other",
    ]
    if value in types:
        return True
    else:
        return False


def is_Capability_t(value):
    types = [
        "data.access.flatfiles",
        "data.access.relational",
        "data.access.xml",
        "data.access.sessiondir",
        "data.access.stageindir",
        "data.access.stageoutdir",
        "data.management.replica",
        "data.management.storage",
        "data.management.transfer",
        "data.naming.resolver",
        "data.naming.scheme",
        "data.transfer",
        "data.transfer.cepull",
        "data.transfer.cepush",
        "executionmanagement.candidatesetgenerator",
        "executionmanagement.dynamicvmdeploy",
        "executionmanagement.executionandplanning",
        "executionmanagement.jobdescription",
        "executionmanagement.jobexecution",
        "executionmanagement.jobmanager",
        "executionmanagement.reservation",
        "executionmanagement.jobcreation",
        "executionmanagement.jobmanagement",
        "information.discovery",
        "information.discovery.job",
        "information.discovery.resource",
        "information.logging",
        "information.model",
        "information.monitoring",
        "information.provenance",
        "information.publication",
        "information.lookup.job",
        "information.query",
        "security.accounting",
        "security.attributeauthority",
        "security.authentication",
        "security.authorization",
        "security.credentialstorage",
        "security.delegation",
        "security.identitymapping",
    ]
    if value in types:
        return True
    else:
        return False


def is_AppEnvState_t(value):
    states = [
        "installable",
        "installationfailed",
        "installedbroken",
        "installednotverified",
        "installedverified",
        "installingautomatically",
        "installingmanually",
        "notinstallable",
        "pendingremoval",
        "removing",
    ]
    if value in states:
        return True
    else:
        return False


def is_SchedulingPolicy_t(value):
    policies = ["fairshare", "fifo", "random"]
    if value in policies:
        return True
    else:
        return False


def is_ComputingActivityType_t(value):
    types = ["collectionelement", "parallelelement", "single", "workflownode"]
    if value in types:
        return True
    else:
        return False


def is_ComputingActivityState_t(value):
    # open season!
    return True


def is_AccessMode_t(value):
    # not described in the spec
    return True


def is_ApplicationHandle_t(value):
    types = ["executable", "module", "Path", "softenv"]
    if value in types:
        return True
    else:
        return False


def is_CPUMultiplicity_t(value):
    types = [
        "multicpu-multicore",
        "multicpu-singlecore",
        "singlecpu-multicore",
        "singlecpu-singlecore",
    ]
    if value in types:
        return True
    else:
        return False


def is_DataStoreType_t(value):
    types = ["disk", "optical", "tape"]
    if value in types:
        return True
    else:
        return False


def is_License_t(value):
    types = ["commercial", "opensource", "unknown"]
    if value in types:
        return True
    else:
        return False


def is_NetworkInfo_t(value):
    types = ["100megabitethernet", "gigabitethernet", "infiniband", "myrinet"]
    if value in types:
        return True
    else:
        # let it pass
        return True


def is_OSFamily_t(value):
    types = ["linux", "macosx", "solaris", "windows"]
    if value in types:
        return True
    else:
        return False


def is_OSName_t(value):
    types = [
        "aix",
        "centos",
        "debian",
        "fedoracore",
        "gentoo",
        "leopard",
        "linux-rocks",
        "mandrake",
        "redhatenterpriseas",
        "scientificlinux",
        "scientificlinuxcern",
        "suse",
        "ubuntu",
        "windowsvista",
        "windowsxp",
    ]
    if value in types:
        return True
    else:
        # let it pass
        return True


def is_ParallelSupport_t(value):
    types = ["mpi", "none", "openmp"]
    if value in types:
        return True
    else:
        return False


def is_Platform_t(value):
    types = ["amd64", "i386", "itanium", "powerpc", "sparc"]
    if value in types:
        return True
    else:
        return False


def is_ReservationPolicy_t(value):
    types = ["mandatory", "none", "optional"]
    if value in types:
        return True
    else:
        return False


def is_RetentionPolicy_t(value):
    types = ["custodial", "output", "replica"]
    if value in types:
        return True
    else:
        return False


def is_AccessLatency_t(value):
    types = ["online", "nearline", "offline"]
    if value in types:
        return True
    else:
        return False


def is_StorageCapacity_t(value):
    types = [
        "online",
        "installedonline",
        "nearline",
        "installednearline",
        "offline",
        "cache",
    ]
    if value in types:
        return True
    else:
        return False


def is_StorageAccessProtocol_t(value):
    types = [
        "afs",
        "dcap",
        "file",
        "gsidcap",
        "gsiftp",
        "gsirfio",
        "http",
        "https",
        "nfs",
        "rfio",
        "root",
        "xrootd",
    ]
    if value in types:
        return True
    else:
        return False


def is_ExpirationMode_t(value):
    types = ["neverexpire", "releasewhenexpired Support", "warnwhenexpired"]
    if value in types:
        return True
    else:
        return False


def is_EndpointHealthState_t(value):
    types = ["critical", "ok", "other", "unknown", "warning"]
    if value in types:
        return True
    else:
        return False


def is_EndpointTechnology_t(value):
    types = ["corba", "jndi", "webservice"]
    if value in types:
        return True
    else:
        return False


def is_ServingState_t(value):
    types = ["closed", "draining", "production", "queueing"]
    if value in types:
        return True
    else:
        return False


def is_Staging_t(value):
    types = ["none", "stagingin", "staginginout", "stagingout"]
    if value in types:
        return True
    else:
        return False


def is_Benchmark_t(value):
    types = [
        "bogomips",
        "cfp2006",
        "cint2006",
        "linpack",
        "specfp2000",
        "specint2000",
        "hep-spec06",
    ]
    if value in types:
        return True
    else:
        return False


def is_JobDescription_t(value):
    types = [
        "condor",
        "egee:jdl",
        "globus:rsl",
        "nordugrid:xrsl",
        "ogf:jsdl:1.0",
        "glite:jdl",
    ]
    if value in types:
        return True
    else:
        return False
