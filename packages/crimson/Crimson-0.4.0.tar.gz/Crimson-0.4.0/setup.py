#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) 2015-2018 Wibowo Arindrarto <bow@bow.web.id>
from setuptools import find_packages, setup

from crimson import __author__, __contact__, \
        __homepage__, __version__


with open("README.rst") as src:
    readme = src.read()

with open("CHANGELOG.rst") as src:
    changelog = src.read().replace(".. :changelog:", "").strip()

with open("requirements.txt") as src:
    requirements = [line.strip() for line in src]

with open("requirements-dev.txt") as src:
    test_requirements = [line.strip() for line in src]


setup(
    name="Crimson",
    version=__version__,
    description="Bioinformatics tool outputs converter to JSON or YAML.",
    long_description=readme + "\n\n" + changelog,
    author=__author__,
    author_email=__contact__,
    url=__homepage__,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*",
                                    "tests"]),
    include_package_data=True,
    install_requires=requirements,
    extras_require={"dev": test_requirements},
    license="BSD",
    zip_safe=False,
    entry_points="""
    [console_scripts]
    crimson=crimson.cli:main
    """,
    keywords="crimson bioinformatics json yaml samtools picard fastqc",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries",
    ],
)
