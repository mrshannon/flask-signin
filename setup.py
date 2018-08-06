from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os
import re
from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as infile:
        text = infile.read()
    return text

def is_requirement(line):
    line = line.strip()
    requirement = not (
        line == '' or
        line.startswith('--') or
        line.startswith('-r') or
        line.startswith('#') or
        line.startswith('-e') or
        line.startswith('git+')
    )
    return requirement

def get_requirements(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as infile:
        lines = infile.readlines()
    return [line.strip() for line in lines if is_requirement(line)]

VERSION = ''
VERSION = re.search(
    r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    read('flask_signin/__init__.py'), re.MULTILINE).group(1)

setup(
    name='Flask-SignIn',
    version=VERSION,
    author='Michael R. Shannon',
    author_email='mrshannon.aerospace@gmail.com',
    description='Simplified authentication for Flask.',
    long_description=read('README.rst'),
    license='MIT',
    url='https://github.com/mrshannon/flask-signin',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    tests_require=get_requirements('dev-requirements.txt'),
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Framework :: Flask',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ),
    zip_safe=True
)
