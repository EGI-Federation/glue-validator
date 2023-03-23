import logging
import os
import sys
import tempfile
import unittest

import glue_validator.validator.EGIProfileTest
import glue_validator.validator.EntryTest
import glue_validator.validator.KnownIssues
import glue_validator.validator.lhcbTest
import glue_validator.validator.ObjectTest
import glue_validator.validator.utils
import glue_validator.validator.WLCGTest


def main():
    config = glue_validator.validator.utils.parse_options()
    log = logging.getLogger(sys.argv[0])
    hdlr = logging.StreamHandler(sys.stderr)
    formatter = logging.Formatter("[%(levelname)s]: %(message)s")
    hdlr.setFormatter(formatter)
    log.addHandler(hdlr)
    log.setLevel(config["debug"])

    if "file" in config:
        if os.path.exists(config["file"]):
            source = "file://%s" % (config["file"])
        else:
            sys.stdout.write("UNKNOWN: File %s does not exist\n" % (config["file"],))
            sys.exit(3)

    if "hostname" in config:
        source = "ldap://%s:%s/%s" % (
            config["hostname"],
            config["port"],
            config["bind"],
        )

    ldif = glue_validator.validator.utils.fast_read_ldif(source, config["timeout"])
    dns_dict = glue_validator.validator.utils.get_dns(ldif)
    if len(dns_dict) == 0:
        sys.stdout.write("UNKNOWN: No LDAP entries returned from %s\n" % (source,))
        sys.exit(3)
    suite = unittest.TestSuite()
    ldif_dict = {}
    for dn in dns_dict:
        entry = ldif[dns_dict[dn][0] : dns_dict[dn][1]]
        entry = glue_validator.validator.utils.convert_entry(entry)
        ldif_dict[dn] = entry
    if config["glue-version"] == "egi-glue2":
        module = sys.modules["glue_validator.validator.ObjectTest"]
        inst = getattr(module, "ObjectTest")
        test_names = unittest.TestLoader().getTestCaseNames(
            glue_validator.validator.ObjectTest.ObjectTest
        )
        for test_name in test_names:
            suite.addTest(inst(test_name, ldif_dict))

    test_config = {
        "general": (
            "EntryTest",
            glue_validator.validator.EntryTest.EntryTest,
            glue_validator.validator.utils.get_glue_version_class(
                config["glue-version"]
            ),
        ),
        "wlcg": (
            "WLCGTest",
            glue_validator.validator.WLCGTest.WLCGTest,
            glue_validator.validator.utils.get_glue_version_class(
                config["glue-version"]
            ),
        ),
        "lhcb": (
            "lchbTest",
            glue_validator.validator.lhcbTest.lhcbTest,
            glue_validator.validator.utils.get_glue_version_class(
                config["glue-version"]
            ),
        ),
        "egi-glue2": (
            "EntryTest",
            glue_validator.validator.EntryTest.EntryTest,
            glue_validator.validator.utils.get_glue_version_class("egi-glue2"),
        ),
    }
    for dn in ldif_dict:
        entry = ldif_dict[dn]
        module_name = (
            "glue_validator.validator.%s" % test_config[config["testsuite"]][0]
        )
        module = sys.modules[module_name]
        inst = getattr(module, test_config[config["testsuite"]][0])
        test_names = unittest.TestLoader().getTestCaseNames(
            test_config[config["testsuite"]][1]
        )
        glue_version = test_config[config["testsuite"]][2]
        if config["testsuite"] in ("general", "egi-profile"):
            for test_name in test_names:
                if (
                    "exclude-known-issues" in config
                    and (
                        test_name not in glue_validator.validator.KnownIssues.test_list
                    )
                ) or "exclude-known-issues" not in config:
                    suite.addTest(inst(test_name, entry, glue_version))
        if config["testsuite"] in ("wlcg", "lhcb"):
            for test_name in test_names:
                attribute = test_name.rsplit("_")[1]
                if attribute in entry:
                    suite.addTest(
                        inst(test_name, entry, entry[attribute], glue_version)
                    )
        if config["testsuite"] == "egi-profile":
            # egi-profile has a 2 set of tests
            module = sys.modules["glue_validator.validator.EGIProfileTest"]
            inst = getattr(module, "EGIProfileTest")
            test_names = unittest.TestLoader().getTestCaseNames(
                glue_validator.validator.EGIProfileTest.EGIProfileTest
            )
            for test_name in test_names:
                attribute = test_name.rsplit("_")[1]
                if attribute in entry:
                    if (
                        "exclude-known-issues" in config
                        and (
                            test_name
                            not in glue_validator.validator.KnownIssues.test_list
                        )
                    ) or "exclude-known-issues" not in config:
                        suite.addTest(
                            inst(test_name, entry, entry[attribute], glue_version)
                        )

    if "nagios" in config:
        auxfile = tempfile.mkstemp()
        fh = open(auxfile[1], "w")
        unittest.TextTestRunner(stream=fh, verbosity=2).run(suite)
        fh.close()
        if "verbosity" in config:
            debug_level = int(config["verbosity"])
        else:
            debug_level = 0
        glue_validator.validator.utils.nagios_output(debug_level, auxfile[1])
    else:  # Deprecated since default is always nagios output
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
