# -*- coding: utf8 -*-
import os

import setuptools
from setuptools import setup, find_packages
import setuptools.command.bdist_egg

build = os.environ.get('PIP_BUILD', '100-local')
keywords = os.environ.get('PIP_KEYWORDS', 'test')

if len(str(build).split('.')) > 1:
    version = build
else:
    version = '0.0.{}'.format(build)


def read_requirements(name=None):
    name = 'requirements.txt' if name is None else '{}-requirements.txt'.format(name)
    with open(name) as f:
        return [r for r in f.readlines() if len(r.strip()) > 0 and r.strip()[0] != '#']


setup(
    name='mali',
    version=version,
    description='Command line tool for missinglink.ai platform',
    author='missinglink.ai',
    author_email='support+mali@missinglink.ai',
    url='https://missinglink.ai',
    license='Apache',
    py_modules=['mali'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7'
    ],
    packages=find_packages(),
    install_requires=read_requirements(),
    extras_require={
        'gcp': read_requirements('gcp'),
        'xattr': read_requirements('xattr'),
    },
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        'mali_commands.utilities': ['*.json'],
    },
    entry_points='''
        [console_scripts]
        mali=mali:main
    ''',
)
