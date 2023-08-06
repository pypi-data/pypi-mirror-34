#!/usr/bin/env python
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(name='pkcrypt2',
      version='1.0.0',
      description='public key cryptography',
      author='Joel Ward',
      author_email='jmward@gmail.com',
      license='MIT',
      platforms='any',
      url='https://gitlab.com/circleclicklabs/pkcrypt2.git',
      py_modules=['pkcrypt2','b85'],
      scripts=['pkcrypt2.py','b85.py'],
      install_requires=['fastecdsa','pyaml','cryptography'],
     )
