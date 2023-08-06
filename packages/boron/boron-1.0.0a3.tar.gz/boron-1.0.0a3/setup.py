#!/usr/bin/env python

# Copyright 2018 Brandon Schlueter
# This file is part of boron.
#
# Boron is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup


boron = __import__('boron')

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='boron',
    author='Brandon Schlueter',
    author_email='b@schlueter.blue',
    description=boron.description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://boron.schlueter.blue',
    version=boron.version,
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=['boron'],
    install_requires=[
        'bjoern',
        'pyyaml',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'boron = boron.cli:main',
        ],
    },
)
