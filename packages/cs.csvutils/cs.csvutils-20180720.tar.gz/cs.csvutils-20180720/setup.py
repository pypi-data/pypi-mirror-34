#!/usr/bin/env python
from setuptools import setup
setup(
  name = 'cs.csvutils',
  description = 'CSV file related facilities',
  author = 'Cameron Simpson',
  author_email = 'cs@cskk.id.au',
  version = '20180720',
  url = 'https://bitbucket.org/cameron_simpson/css/commits/all',
  classifiers = ['Programming Language :: Python', 'Programming Language :: Python :: 2', 'Programming Language :: Python :: 3', 'Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'Operating System :: OS Independent', 'Topic :: Software Development :: Libraries :: Python Modules', 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
  install_requires = ['cs.deco', 'cs.logutils', 'cs.mappings', 'cs.pfx'],
  keywords = ['python2', 'python3'],
  package_dir = {'': 'lib/python'},
  py_modules = ['cs.csvutils'],
)
