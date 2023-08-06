#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(
    name='es_metricbeats_cleaner',
    version='1.0',
    description='Elasticsearch cleanup for metricbeats',
    author='Omar Diaz',
    author_email='diaz@autoaid.de',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'elasticsearch',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'es_metricbeats_cleaner = es_cleaner:main',
        ]
    },
)