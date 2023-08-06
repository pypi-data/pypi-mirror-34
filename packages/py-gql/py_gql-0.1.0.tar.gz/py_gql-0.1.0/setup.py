#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=all
"""
"""

import imp
import itertools
import os
import sys

from setuptools import find_packages, setup

ABBOUT = imp.load_source("about", os.path.join(".", "py_gql", "__version__.py"))


def run_setup():

    with open("README.md") as f:
        readme = "\n" + f.read()

    setup(
        name=ABBOUT.__title__,
        version=ABBOUT.__version__,
        description=ABBOUT.__description__,
        long_description=readme,
        long_description_content_type="text/markdown",
        author=ABBOUT.__author__,
        author_email=ABBOUT.__author_email__,
        url=ABBOUT.__url__,
        license=ABBOUT.__license__,
        keywords="graphql",
        zip_safe=False,
        packages=find_packages(
            exclude=("tests", "tests.*", "docs", "examples")
        ),
        # package_data={},
        install_requires=_split_requirements("requirements.txt"),
        include_package_data=True,
        python_requires=">2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
        ext_modules=_cython_ext_modules(
            "py_gql",
            "py_gql.lang",
            "py_gql.validation",
            "py_gql.validation.rules",
            "py_gql.utilities",
            "py_gql.schema",
            "py_gql.schema.build",
            "py_gql.execution",
        ),
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Operating System :: POSIX",
            "Operating System :: MacOS :: MacOS X",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries",
        ],
        tests_require=(
            _split_requirements(
                "test-requirements.txt", "py3-test-requirements.txt"
            )
            if sys.version >= "3"
            else _split_requirements("test-requirements.txt")
        ),
    )


def _cython_ext_modules(*packages):
    try:
        from Cython.Build import cythonize
    except ImportError:
        return []
    else:
        enable_linetrace = "CYTHON_TRACE" in os.environ
        ext_modules = [
            cythonize(
                "%s/*.py" % package.replace(".", "/"),
                compiler_directives={
                    "embedsignature": True,
                    "linetrace": enable_linetrace,
                },
            )
            for package in packages
        ]
        return list(itertools.chain.from_iterable(ext_modules))


def _split_requirements(*requirements_files):
    req = []
    for requirements_file in requirements_files:
        with open(requirements_file) as f:
            req.extend(
                [
                    line.strip()
                    for line in f.readlines()
                    if line.strip() and not line.startswith("#")
                ]
            )
    return req


if __name__ == "__main__":
    run_setup()
