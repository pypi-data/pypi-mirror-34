#!/usr/bin/env python

from os import path
from codecs import open
from setuptools import find_packages, setup, Extension

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'jf',
  version = '0.4.5',
  description = 'Python jsonl query engine',
  long_description=long_description,
  author = 'Lasse Hyyrynen',
  author_email = 'leh@protonmail.com',
  maintainer = 'Lasse Hyyrynen',
  maintainer_email = 'leh@protonmail.com',
  license = 'MIT',
  keywords = ['json', 'yaml', 'jq'],
  download_url = 'https://github.com/alhoo/jf/archive/0.4.5.tar.gz',
  url = 'https://github.com/alhoo/jf',
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Topic :: Utilities'
  ],
  packages = ['jf'],
  setup_requires = [
    'setuptools>=20.2.2'
  ],
  ext_modules = [Extension("jf.jsonlgen",
    sources=["jf/jsonlgen.cc"],
    extra_compile_args=['-std=c++11'],
    ),
  ],
  install_requires = [
    'pygments>=2.0.0',
    'regex>=2016.3.2',
    'python-dateutil>=2.6.1',
    'PyYAML>=3.12',
    'PyYAML>=3.12',
    'lxml>=4.0.1',
    'dateparser>=0.6.0',
    'ipython>=6.2.0',
    'csvtomd>=0.3.0',
    'pandas>=0.22.0',
    'pandas-profiling>=1.4.1'
  ],
  tests_require = [
    'nose>=1.3.0',
    'pandas>=0.22.0',
    'xlrd>=1.1.0',
    'pylint>=1.8.2'
  ],
  test_suite = 'tests',
  zip_safe = True,
  entry_points = {
    'console_scripts': ['jf=jf.__main__:main']
  }
)

