# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 18:42:06 2018

@author: yatheen!
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="novigo",
    version="0.0.12",
    author="yatheen!",
    author_email="pravan.yatheen@gmail.com",
    description="A small example package",
    include_package_data=True,
    package_data = {'models':'./novigo/models/*'},
    url='https://github.com/Yatheen07/novigo-python-package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = ['numpy','sklearn','scipy'],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)