#!/usr/bin/python3
# Copyright 2022 Sergio Doreste Buerles
# See LICENSE for details.
# Author: Sergio Doreste Buerles


import io
from setuptools import setup, find_packages


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()


def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            yield line.strip()


setup(
    name='adult_api',
    version='1.0',
    packages=find_packages(),
    url="https://github.com/sdores/adult-api",
    download_url="https://github.com/sdores/adult-api/adult_api",
    license='LICENSE.md',
    author='Sergio Doreste Buerles',
    author_email='sdores23@hotmail.com',
    description='',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=list(requirements(filename='requirements.txt')),
    data_files=[],
    entry_points={
        'console_scripts': [
            'adult_api=adult_api.run:main'
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers"
    ],
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/sdores/adult-api/adult_api/issues',
        'Source': 'https://github.com/sdores/adult-api/adult_api'
    },
)
