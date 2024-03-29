import logging
import os
import signal
import sys
import tempfile
import time

import ldap
import ldap.modlist as modlist

import glue_validator.validator.utils


def start_slapd():
    global config
    print("Starting slapd server.")
    # Set up Signal handler for SIGTERM (kill -15) and SIGINT (ctrl-c)
    signal.signal(signal.SIGTERM, handler)
    signal.signal(signal.SIGINT, handler)

    core = None
    backend = ""
    if os.path.exists("/etc/openldap/schema/core.schema"):
        core = "/etc/openldap/schema/core.schema"
    elif os.path.exists("/etc/ldap/schema/core.schema"):
        core = "/etc/ldap/schema/core.schema"
        backend = "moduleload      back_bdb"
    else:
        sys.stderr.write(
            "Error: Could not find core.schema file, do you have OpenLDAP installed?\n"
        )
        sys.exit(1)

    if not os.path.exists("/etc/ldap/schema/GLUE20.schema"):
        sys.stderr.write(
            "Error: Could not find GLUE20.schema file, "
            "do you have glue-schema installed?\n"
        )
        sys.exit(1)
    config["tmp_dir"] = tempfile.mkdtemp()
    if os.path.exists(config["tmp_dir"]):
        file = open(config["tmp_dir"] + "/slapd.conf", "w")
        file.write(
            """
include """
            + core
            + """
include /etc/ldap/schema/GLUE20.schema

pidfile         """
            + config["tmp_dir"]
            + """/slapd.pid
argsfile        """
            + config["tmp_dir"]
            + """/slapd.args
idletimeout     120
sizelimit       80000
timelimit       2400
"""
            + backend
            + """

#######################################################################
# database definitions
#######################################################################

database        bdb
cachesize       60000
dbnosync
suffix          "o=glue
rootdn          "o=glue"
rootpw          secret
directory       """
            + config["tmp_dir"]
            + """
"""
        )
        file.close()
        # Start slapd server
        command = (
            "/usr/sbin/slapd -f "
            + config["tmp_dir"]
            + "/slapd.conf -h ldap://localhost:21700"
        )
        os.system(command)
        time.sleep(1)
        if not os.path.exists(config["tmp_dir"] + "/slapd.pid"):
            sys.stderr.write("Error: Could not start slapd.\n")
            print(command)
            sys.exit(1)
    else:
        sys.stderr.write("Error: Directory %s does not exists") % (config["tmp_dir"])
        sys.exit(1)


def stop_slapd():
    global config

    if os.path.exists(config["tmp_dir"] + "/slapd.pid"):
        print("Stopping slapd server ...")
        slapd_pid = open(config["tmp_dir"] + "/slapd.pid").read()
        os.kill(int(slapd_pid), signal.SIGTERM)
        os.system("rm -rf " + config["tmp_dir"])
    else:
        os.system("rm -rf " + config["tmp_dir"])


# Signal handler
def handler(signum, frame):
    sys.stderr.write("Shutting Down slapd\n")
    stop_slapd()
    sys.exit(0)


# Schema validation function
def test_ldif(entry):
    connect = ldap.initialize("ldap://localhost:21700")
    connect.simple_bind_s("o=glue", "secret")

    dn = entry["dn"][0]
    entry.pop("dn")
    try:
        #       sys.stdout.write("Trying to add %s ... " %(dn))
        connect.add(dn, modlist.addModlist(entry))
        connect.result()
        return True
    except Exception as e:
        message = "Error: %s\n%s\n\n" % (dn, e)
        sys.stderr.write(message)
        return False


def main():
    global config
    config = glue_validator.validator.utils.parse_options()
    log = logging.getLogger(sys.argv[0])
    hdlr = logging.StreamHandler(sys.stderr)
    formatter = logging.Formatter("[%(levelname)s]: %(message)s")
    hdlr.setFormatter(formatter)
    log.addHandler(hdlr)
    log.setLevel(config["debug"])

    if "file" in config:
        source = "file://%s" % (config["file"])
    if "host" in config:
        source = "ldap://%s:%s/%s" % (config["host"], config["port"], config["bind"])

    ldif = glue_validator.validator.utils.fast_read_ldif(source, config["timeout"])
    dns = glue_validator.validator.utils.get_dns(ldif)

    ordered_dns = dns.keys()
    ordered_dns.sort(key=lambda x: len(x))
    start_slapd()

    defaults = {
        "o=glue": """dn: o=glue
objectClass: organization
o: glue""",
        "GLUE2GroupID=resource,o=glue": """dn: GLUE2GroupID=resource,o=glue
objectClass: GLUE2Group
GLUE2GroupID: resource
""",
        "GLUE2GroupID=grid,o=glue": """dn: GLUE2GroupID=grid,o=glue
objectClass: GLUE2Group
GLUE2GroupID: grid
""",
    }

    total = 0
    fail = 0
    ok = 0

    for dn in defaults:
        if dn.lower() in ordered_dns:
            entry = ldif[dns[dn.lower()][0] : dns[dn.lower()][1]].strip()
            entry = glue_validator.validator.utils.convert_entry(entry)
            total += 1
            result = test_ldif(entry)
            if result:
                ok += 1
            else:
                fail += 1
            ordered_dns.remove(dn.lower())

        else:
            entry = glue_validator.validator.utils.convert_entry(defaults[dn])
            result = test_ldif(entry)

    for dn in ordered_dns:
        entry = ldif[dns[dn][0] : dns[dn][1]].strip()
        entry = glue_validator.validator.utils.convert_entry(entry)
        total += 1
        result = test_ldif(entry)
        if result:
            ok += 1
        else:
            fail += 1
    stop_slapd()
    if fail > 0:
        print("Test Failed! (%i/%i)" % (ok, total))
        sys.exit(1)
    else:
        print("Test Passed! (%i/%i)" % (ok, total))
        sys.exit()


if __name__ == "__main__":
    main()
