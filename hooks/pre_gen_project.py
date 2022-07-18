#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hooks called before generating the project structure.

This hook checks whether the informed project name is a valid Python package name.
"""
import re
import sys
from pathlib import Path


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
PACKAGE_NAME = '{{ cookiecutter.package_name }}'
PROJECT_NAME = '{{ cookiecutter.project_name }}'


if not re.match(MODULE_REGEX, PACKAGE_NAME):
    print(f'ERROR: \"{PACKAGE_NAME}\" is not a valid Python module name!')
    print('Please try again using a name like \"my_awesome_project\".')
    max_tries = 3
    project_directory = Path.cwd().joinpath(PROJECT_NAME)
    # Search for the project directory. If found, we'll remove it.
    while max_tries > 0 and not project_directory.is_dir():
        max_tries -= 1
        project_directory = Path('..').joinpath(project_directory)
    if project_directory.is_dir():
        print('Removing the project directory: ', project_directory)
        project_directory.unlink(missing_ok=True)
    # Exits with status 1 to show failure
    sys.exit(1)
