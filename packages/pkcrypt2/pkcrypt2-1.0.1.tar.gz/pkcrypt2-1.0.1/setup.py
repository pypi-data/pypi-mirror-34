#!/usr/bin/env python
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = open('README.md').read()
from pkcrypt2 import __version__

setup(name='pkcrypt2',
      version=__version__,
      description='public key cryptography',
      long_description=long_description,
      author='Joel Ward',
      author_email='jmward@gmail.com',
      license='MIT',
      platforms='any',
      url='https://gitlab.com/circleclicklabs/pkcrypt2.git',
      py_modules=['pkcrypt2','b85'],
      scripts=['pkcrypt2.py','b85.py'],
      install_requires=['fastecdsa','pyaml','cryptography'],
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
     )
