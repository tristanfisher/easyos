#!/usr/bin/env python

import os
import sys
import easyos

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('README.rst') as f:
    readme = f.read()

setup(
    name='easyos',
    version=easyos.__version__,
    description='Common OS attributes in a user-friendly format.',
    long_description=readme,
    author='Tristan Fisher',
    author_email='code@tristanfisher.com',
    url='http://github.com/tristanfisher/easyos',
    packages=['easyos'],
    package_data={'': ['LICENSE']},
    license='Apache 2.0',
    keywords = 'os environment operating system',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ),
)
