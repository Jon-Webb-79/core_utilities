# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='core_utilities',
    version='0.1.0',
    description='Core utility functions for python software',
    long_description=readme,
    author='Jonathan Webb',
    author_email='webbja123@gmail.com',
    license=license,
    packages=['core-utilities'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: MacOS",
        "Operating System :: POSIX::Linux"
    ]
)
