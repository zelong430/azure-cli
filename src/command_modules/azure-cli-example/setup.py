#!/usr/bin/env python

from codecs import open
from setuptools import setup

VERSION = '0.1.6'

# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
    'azure-cli-core',
]

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()


setup(
    name='azure-cli-example',
    version=VERSION,
    description='Example Command Module',
    long_description=README + '\n\n',
    license='MIT',
    author='Zelong Qiu',
    author_email='ze',
    url='https://github.com/Azure/azure-cli',
    classifiers=CLASSIFIERS,
    namespace_packages=[
        'azure',
        'azure.cli',
        'azure.cli.command_modules',
    ],
    packages=[
        'azure.cli.command_modules.example',
    ],
    install_requires=DEPENDENCIES,
)
