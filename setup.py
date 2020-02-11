#!/usr/bin/env python

from setuptools import find_packages, Extension
from numpy.distutils.core import setup

setup(name='ytfcontour',
      version='0.0',
      description='Small contouring library designed for YTFC projects.',
      author='Zach Marin',
      author_email='zach.marin@yale.edu',
      packages=find_packages(),
     )