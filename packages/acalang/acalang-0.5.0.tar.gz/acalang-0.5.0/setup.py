#!/usr/bin/env python3

"""Aca setup script"""

from setuptools import setup
from aca.aca import __VERSION__

with open("README.md", "r") as f:
    LONG_DESC = f.read()

setup(
    name="acalang",
    version=__VERSION__,
    description="Aca, a functional programming language, and shitty toy",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    license="MIT",
    author="AnqurVanillapy",
    author_email="anqurvanillapy@gmail.com",
    url="https://github.com/anqurvanillapy/acalang",
    entry_points={"console_scripts": ["aca=aca.aca:main"]},
    packages=["aca"],
    package_data={"aca": ["*.aca"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
