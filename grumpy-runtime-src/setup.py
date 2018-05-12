#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The setup script."""

import sys
from setuptools import setup, find_packages
from setuptools.command.bdist_egg import bdist_egg as BdistEggCommand
from distutils.command.build import build as BuildCommand
import subprocess

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
    # TODO: Put package requirements here
    'importlib2>=3.5.0.2',
    'click-default-group>=1.2',
]

setup_requirements = [
    'setuptools>=28.8.0',
    'pytest-runner',
    # TODO(alanjds): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: Put package test requirements here
]

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
if needs_pytest:
    setup_requirements += ['pytest-runner']

COMMON_OPTIONS = dict(
    version='0.1.1',
    description="Grumpy Runtime & Transpiler",
    long_description=readme,
    author="Dylan Trotter et al.",
    maintainer="Alan Justino et al.",
    maintainer_email="alan.justino@yahoo.com.br",
    url='https://github.com/google/grumpy',
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='grumpy_runtime',
    python_requires='~=2.7.0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)


def _run_make(self, *args, **kwargs):
    subprocess.check_call(["""echo "print 'Make Runtime Success'" | make run --debug"""], shell=True)


class BuildMakeCommand(BuildCommand):
    def run(self, *args, **kwargs):
        _run_make(self, *args, **kwargs)
        result = BuildCommand.run(self, *args, **kwargs)


class BdistEggMakeCommand(BdistEggCommand):
    def run(self, *args, **kwargs):
        _run_make(self, *args, **kwargs)
        result = BdistEggCommand.run(self, *args, **kwargs)


GRUMPY_RUNTIME_OPTIONS = dict(
    name='grumpy-runtime',
    requires=['grumpy_tools'],
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"],
    ),
    include_package_data=True,
    cmdclass={
        'build': BuildMakeCommand,
        'bdist_egg': BdistEggMakeCommand,
    },
    zip_safe=False,
)
GRUMPY_RUNTIME_OPTIONS.update(COMMON_OPTIONS)

setup(**GRUMPY_RUNTIME_OPTIONS)