# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ECON221',
    version='0.1.0',
    description='ECON221 for python',
    long_description=readme,
    author='Saeid Adli',
    author_email='saeid.adli@gmail.com',
    url='https://github.com/saeidadli/ECON221',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

