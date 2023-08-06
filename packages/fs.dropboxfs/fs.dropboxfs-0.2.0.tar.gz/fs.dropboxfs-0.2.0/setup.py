#!/usr/bin/env python

from setuptools import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: System :: Filesystems',
]

import io
with io.open('README.rst', 'r', encoding='utf8') as f:
    DESCRIPTION = f.read()

with io.open('HISTORY.rst', 'r', encoding='utf8') as f:
    HISTORY = f.read()

REQUIREMENTS = [
    "fs~=2.0.7",
    "dropbox",

]

setup(
    author="guojian.li",
    author_email="guojianlee@qq.com",
    classifiers=CLASSIFIERS,
    description="Dropbox support for pyfilesystem2",
    entry_points={
        'fs.opener': 'dropbox = dropboxfs.opener:DropboxOpener'
    },
    install_requires=REQUIREMENTS,
    license="MIT",
    long_description=DESCRIPTION + "\n" + HISTORY,
    name='fs.dropboxfs',
    packages=find_packages(exclude=("tests",)),
    platforms=['any'],
    setup_requires=['nose'],
    tests_require=[],
    test_suite='dropboxfs.tests',
    url="http://pypi.python.org/pypi/fs.dropboxfs/",
    version="0.2.0",
)
