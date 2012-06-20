#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pspec',
    version='0.0.1',
    description='',
    author='Ben Firshman',
    author_email='ben@firshman.co.uk',
    url='http://www.ep.io/',
    packages = [
        'pspec'
    ],
    package_data = {},
    include_package_data=True,
    install_requires = open('requirements.txt').readlines(),
    entry_points={
        'console_scripts': [
            'pspec = pspec.cli:main',
        ],
    }
    #test_suite = 'nose.collector',
)

