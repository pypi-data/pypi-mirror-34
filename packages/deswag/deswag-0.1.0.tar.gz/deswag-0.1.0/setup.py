#!/usr/bin/env python

from setuptools import setup

setup(
    setup_requires=['pbr>=1.9', 'setuptools>=17.1'],
    pbr=True,
    entry_points={
        'console_scripts': [
            'deswag = deswag.cli:main',
        ],
    },
)
