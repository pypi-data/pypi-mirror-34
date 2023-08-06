#!/usr/bin/env python
import os

with open('openstack_opentracing/version.py', 'w+') as f:
    f.write("__version__ = '0.1.%s'"%(os.getenv('TRAVIS_BUILD_NUMBER', '0')))


