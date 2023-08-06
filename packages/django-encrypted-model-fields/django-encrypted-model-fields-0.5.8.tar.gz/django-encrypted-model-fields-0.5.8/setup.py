#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
from setuptools import setup, find_packages


with open('encrypted_model_fields/__init__.py', 'r') as init_file:
    version = re.search(
        '^__version__ = [\'"]([^\'"]+)[\'"]',
        init_file.read(),
        re.MULTILINE,
    ).group(1)

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-encrypted-model-fields',
    version=version,
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    description=(
        'A set of django fields that internally are encrypted using the '
        'cryptography.io native python encryption library.'
    ),
    long_description=open('README.rst').read(),
    url='http://gitlab.com/lansharkconsulting/django/django-encrypted-model-fields/',
    download_url='https://gitlab.com/lansharkconsulting/django/django-encrypted-model-fields/repository/archive.tar.gz?ref=v{}'.format(version),
    author='Scott Sharkey',
    author_email='ssharkey@lanshark.com',
    maintainer="Scott Sharkey",
    maintainer_email="ssharkey@lanshark.com",
    install_requires=[
        'Django>=1.9',
        'cryptography>=2.3',
        'six',
    ],
    tests_require=['tox'],
    keywords=['encryption', 'django', 'fields', ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Topic :: Internet :: WWW/HTTP",
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.5",
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
    ],
)
