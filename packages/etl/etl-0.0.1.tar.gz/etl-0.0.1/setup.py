#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

readme = "coming soon"
history = ""

tests_require = [
]

setup(
    name="etl",
    version='0.0.1',

    packages=[
        "etl",

    ],
    package_dir={
        '': 'src'
    },

    package_data={
    },

    tests_require=tests_require,

    install_requires=[
    ],

    setup_requires=[
        'pytest-runner',
    ],

    license="MIT license",

    keywords='',
    description="etl",
    long_description="%s\n\n%s" % (readme, history),

    entry_points={
        'console_scripts': [
            'etl=etl.main:main',
        ],
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
