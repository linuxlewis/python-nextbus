#!/usr/bin/env python

import os
import sys

import nextbus

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'nextbus',
]

requires = ['requests', 'lxml']

readme =''
history =''

setup(
    name='python-nextbus',
    version=nextbus.__version__,
    description='python client for nextbus api',
    long_description=readme + '\n\n' + history,
    author='Sam Bolgert',
    author_email='sbolgert@gmail.com',
    url='http://python.org',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'nextbus': 'nextbus'},
    include_package_data=True,
    install_requires=requires,
    license=license,
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',

    ),
)