#!/usr/bin/env python

from distutils.core import setup

setup(name='glue-validator',
      version='2.0.25',
      description='GLUE 2.0 Valiation',
      long_description ='Validation scripts for an LDAP based information system using the GLUE 2.0 schema',
      author='Laurence Field',
      author_email='Laurence.Field@cern.ch',
      license='Apache 2.0',
      url='https://github.com/EGI-Federation/glue-validator',
      scripts = ['bin/glue-validator'],
      packages=['glue2','glue1','egi-glue2','validator'],
      package_dir = {'': 'lib'},
      )
