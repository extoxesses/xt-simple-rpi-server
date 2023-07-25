#!/usr/bin/env python

from distutils.core import setup

setup(
	name='RpiMonitor',
	version='1.0',
	description='Raspberry Pi hardware monitor service',
	author='Extoxesses',
	author_email='extoxesses@gmail.com',
	url='',
	packages=['config', 'monitor', 'server', 'service', 'utils'],
)