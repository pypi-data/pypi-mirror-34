#!/usr/bin/env python
import sys, pkcrypt2
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(name='pkcrypt2',
      version=pkcrypt2.__version__,
      description='public key cryptography',
      long_description=open('README.md').read,
      author='Joel Ward',
      author_email='jmward@gmail.com',
      license='MIT',
      platforms='any',
      url='http://gist.github.com/val314159/3b384398406822f231bf58727c73fa70',
      py_modules=['pkcrypt2','x85'],
      scripts=['pkcrypt2.py','x85.py'],
      install_requires=['fastexdsa','pyaml','cryptography'],
     )
