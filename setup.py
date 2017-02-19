from __future__ import absolute_import, division, print_function

import os
import versioneer
from setuptools import setup, find_packages

setup(
    name="foo",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Richard Postelnik",
    author_email="postelrich@gmail.com",
    description="foo",
    packages=find_packages(exclude=['tests']),
    long_description=open('README.md').read() if os.path.exists('README.md') else '',)