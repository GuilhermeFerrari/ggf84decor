#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup Script
"""

from distutils.core import setup
import ggf84decor

setup(
    name='ggf84decor',
    version='1.0',
    author='Guilherme G. Ferrari',
    author_email='gg.ferrari@gmail.com',
    py_modules=['ggf84decor'],
    license='MIT License',
    description=ggf84decor.__doc__.strip(),
)

########## end of file ##########
