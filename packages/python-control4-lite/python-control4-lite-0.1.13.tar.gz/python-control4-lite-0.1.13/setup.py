#!/usr/bin/env python
# -*- coding:utf-8 -*-

import io
from setuptools import setup

version = '0.1.13'

setup(
    name='python-control4-lite',
    version=version,
    description='Python Bindings for Control4 API',
    keywords='control4',
    author='Aleksi Asikainen',
    author_email='aleksi.asikainen@solera.com',
    url='https://github.com/r3pi/python-control4-lite',
    packages=['control4',],
    install_requires=['aiohttp>=3.0.0','urllib3>=1.0',],
    license='MIT',
    long_description=io.open('README.md', encoding='UTF-8').read(),
    test_suite='nose.collector',
    tests_require=['nose', 'aiounittest'],
    python_requires='>=3.6.0'
)
