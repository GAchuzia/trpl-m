#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='trpl-m',
    version='1.0.0',
    author='Grant Achuzia',
    author_email='achuziaduby@gmail.com',
    description='Mental math game in your terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests', 'venv']),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Games/Entertainment',
    ],
    python_requires='>=3.6',
    install_requires=[
        'rich>=13.0.0'
    ],
    entry_points={
        'console_scripts': [
            'trpl_m = triple_m.main:Trplm', 
        ]
    }
)
