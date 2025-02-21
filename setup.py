#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='trpl-m',
    version='1.0.0',
    author='Grant Achuzia',
    author_email='achuziaduby@gmail.com',
    description='Mental math game in your terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests', 'venv']),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License : OSI Approved :: MIT License',
        'Topic :: Games/Entertainment',
    ],
)
    


