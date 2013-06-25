#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pspec',
    version='0.0.2',
    description='Python testing for humans',
    author='Ben Firshman',
    author_email='ben@firshman.co.uk',
    url='https://github.com/bfirsh/pspec',
    packages=['pspec', 'pspec.groups'],
    package_data={},
    install_requires=[
        'docopt==0.6.1',
        'Attest',
    ],
    dependency_links=[
        'http://github.com/dag/attest/tarball/b1ad455a7bef86b073a46fbc1dffae4b1aac8338#egg=Attest-0.6',
    ],
    entry_points={
        'console_scripts': [
            'pspec = pspec.cli:main',
        ],
    }
)

