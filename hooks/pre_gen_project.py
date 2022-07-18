#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hooks called before generating the project structure.

This hook checks whether the informed project name is a valid Python package name.
"""
import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
PACKAGE_NAME = '{{ cookiecutter.package_name }}'


if not re.match(MODULE_REGEX, PACKAGE_NAME):
    print(f'ERROR: {PACKAGE_NAME} is not a valid Python module name!')

    # exits with status 1 to indicate failure
    sys.exit(1)
