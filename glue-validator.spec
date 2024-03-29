Name: glue-validator
Version: 2.1.0
Release: 1%{?dist}
Summary: A validation framework for Grid information providers
Group: Development/Libraries
License: ASL 2.0
URL: https://github.com/EGI-Federation/glue-validator
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: rsync
BuildRequires: make
BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-rpm-macros
Requires: openldap-clients
Requires: python3
Requires: python3-ldap

%description
A validation framework for Grid information providers

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make install python=python3 prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license /usr/share/licenses/%{name}-%{version}/COPYRIGHT
%license /usr/share/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Fri Mar 17 2023 Baptiste Grenier <baptiste.grenier@egi.eu> - 2.1.0-1
- Switch to python3. (#7) (Enol Fernandez)
- Fix tests. (#7) (Enol Fernandez)
- Build and release packages using AlmaLinux 8 and 9. (#7) (Baptiste Grenier)

* Fri Oct 03 2014 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.25-0
- # GRIDINFO-58: Workaround for StoRM in the Domain Foreign Keys Test
- Fix help examples that were not correct

* Wed Sep 03 2014 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.24-1
- Increased version

* Tue Sep 02 2014 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.24-0
- #GRIDINFO-6: Test mandatory objects are present
- #GRIDINFO-3: Test GLUE2ServiceAdminDomainForeignKey = GLUE2DomainID in the DN 
 
* Fri Aug 08 2014 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.23-0
- #GRIDINFO-52: xroot should be used when referring to the xrootd protocol
- #GRIDINFO-51: Add new ServiceType values
- #GRIDINFO-50: Obsolete WLCG_NAME test
- #GRIDINFO-47: Add 'notification' in the capability type
- #GRIDINFO-46: Bugs reported by DPM (II)

* Thu Apr 10 2014 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.22-0
- #GRIDINFO-48: Fix test_GLUE2ComputingShareTotalJobs_OK 

* Wed Mar 05 2014 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.21-0
- #GRIDINFO-33: Add LHCb testuite
- #GRIDINFO-27: Add service and interface names for QCG
- #GRIDINFO-25: Add +-1 margin for Storage Capacities
- #GRIDINFO-44: Add service and interface names for DPM
- #GRIDINFO-45: workaround for ARC validity bug

* Wed Oct 02 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.20-0 
- Add tolerances for job totals
- Add ERROR messages for default values in AWT/EWT and WaitingJobs
- Add new tests to known issues for final version for EGI validation
- Fixed the list of grid infrastructure names in types 

* Fri Sep 06 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.19-0
- Add correct case in OS names
- Add tests for OS types and add general type checking test to known issues
- Add known-issues to the general tests
- Added +-(1+0.5%) tolerance to Share and Storage Service Capacity tests
- Adapted Share and Storage Service Capacity tests to current way of publishing for DPM, dCache and StoRM
- Changed upper limit in Share and Storage Service Capacity to 1 billion GB instead of 1 million GB
- Updated known-issues with list of tests 
- Activate --exclude-known-issues option
- Change glue-validator to make "wlcg" testsuite work as a debugging testsuite to execute only some selected tests
- Add new info message I096 and I097
- Allow nagios option to work with all glue options
- Add separator in additional info in the message generator
- Improved usage of glue-validator command line options and define default options
- BUG #101997: Fix to work with bindings containing "/" 
- BUG #101996: Accept single strings in OtherInfo
- BUG #101934: Align OS Names with EGI guidelines and enable the OS Name checking that was disabled
- BUG #101130: Test to check Endpoint and Service IDs do not start with '_'
- BUG #102224: Test for GLUE2EndpointImplementationVersion
 
* Fri Jun 21 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.18-0
- BUG #101815: Redirect timeout error message to stdout
- BUG #101828: Accept GLUE2EntityOtherInfo: This CREAM-CE is using Argus as correct until CREAM CE fixes syntax
- BUG #101829: Increase time range when checking dates

* Fri May 31 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.17-0
- Fixed messages in EntryTest that were not concatenated
- Removed obsolete of glue-validator-cron that is now fixed
- Update spec URL to point to new Information System web pages

* Mon May 06 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.16-0
- Fixed bug with dates: GLUE dates were transformed into UTC when they already are UTC 

* Tue Apr 30 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.15-0
- Defined new verbose level 2 for nagios output
- Added associated attribute to message dictionary
- Added sanity checks for the command line options (nagios, verbosity level and separator) 

* Mon Apr 29 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.14-0
- Defined a general message generator function and added an option to define a separator
- Added missing type
- Fixed OtherInfo type check that is not done in the general test but on specific tests

* Fri Apr 26 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.13-0
- Improved error, warning and info messages defining a common structure for all tests
- Defined OtherInfo as a multivalued attribute in the EGI profile
- Improved the EGI profile types

* Fri Apr 12 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.12-0
- Modified Entrytest to collect all erros within an object instead of terminating after the first error is found
- Modified EGIProfile to fix bug related to date and time and references to non existing attributes
- Removed extra type checks from individual tests in EGIProfile
- Defined OtherInfo attribute as optional
- Updated the nagios output function in utils to deal with 'grouped' failure messages coming from Entrytest tests  

* Tue Mar 12 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.11-0
- Transformed creation times into UTC
- Extended types after reviewing information providers

* Fri Mar 08 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.10-0
- Fixed datetime problem not working in SL5
- Removed tests that were already part of the general type check test
- Reviewed ForeignKey attributes

* Thu Mar 07 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.9-0
- Improved error messages and fixed bugs in existing tests after feedback from beta testing
- Fixed problem with output redirection to file for the testsuite output
- Added exclude-known-issues flag 

* Tue Mar 05 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.8-0
- BUG #100733: Applied changes requested by Nagios team to be Nagios compliant

* Thu Feb 28 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.7-0
- Added missing error message type
- Added missing Endpoint_t, Capability_t and ServiceType_t requested by ARC

* Wed Feb 27 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.6-0
- Added types for Middleware names
- Fixed typo in data.py
- Added specific attribute tests: ExecutionEnvironment, ApplicationEnvironment, Storage, Endpoint

* Tue Feb 26 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.5-0
- Added types for WLCG names, VO names and EGI NGIs.
- Added specific attribute tests: OtherInfo, ComputingManager and ExecutionEnvironment (ongoing)

* Mon Feb 25 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.4-0
- Added specific attribute tests: ComputingShare and ComputingManager (ongoing)
- BUG #100467: Fixed typo in Capability_t and added values reported at the EMT
- BUG #100608: Added values reported at the EMT for ServiceType_t and InterfaceName_t 

* Wed Feb 13 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.3-0
- Modified EntryTest to check Undesirable attributes
- Added specific attribute tests in EGIProfileTest
- Added types in egi-glue2 types

* Wed Feb 06 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.2-0
- Adapt EntryTest to be used also for EGI profile and leave specific attribute tests in EGIProfileTest
- Tuning of egi-glue2/data.py and egi-glue2/types.py
- Added verbose debug level in nagios output

* Tue Feb 05 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.1-0
- New option to produce nagios output 

* Mon Jan 28 2013 Maria Alandes <maria.alandes.pradillo@cern.ch> - 2.0.0-0
- Changes to include validation against EGI profile for GLUE 2.0 and WLCG specific tests

* Wed Nov 21 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.5-1
- BUG #98982: voms added to is_allowed_URL_Schema in GLUE 1 and 2

* Tue Nov 20 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.4-1
- BUG #98683: New test to check attributes are not empty  
- BUG #98948: GLUE2Group class has been updated with GLUE2GroupName

* Fri Oct 12 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 1.0.3-1
- BUG #98104: ldap added to is_allowed_URL_Schema in GLUE 1 and 2
- BUG #97155: information.publication is now added to Capability_t

* Wed Dec 14 2011 Laurence Field <laurence.field@cern.ch>  - 1.0.2-1
- New upstream version and packaging improvements

* Mon Dec 05 2011 Laurence Field <laurence.field@cern.ch>  - 1.0.1-1
- New upstream version and packaging improvements

* Fri Nov 11 2011 Laurence Field <laurence.field@cern.ch>  - 1.0.0-1
- Initial Release
