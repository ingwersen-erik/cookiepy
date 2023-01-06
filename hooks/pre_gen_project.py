#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script defines steps needed to be executed prior to the repository creation.

Hook checks whether the user set a valid project and Python package names
when executing the command:

.. code-block:: console

    $ cookiecutter gh:ingwersen-erik/cookiepy

Additionally, it also checks whether a project of the same name already exists
and if so, deletes the preexisting project.
"""
from __future__ import annotations

import os
import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
PACKAGE_NAME = "{{ cookiecutter.package_name }}"
PROJECT_NAME = "{{ cookiecutter.project_name }}"


def main_pregen():
    """
    Execute the steps that need to be executed prior to project generation.
    """
    os.environ.setdefault("PROJECT_NAME", PROJECT_NAME)
    os.environ.setdefault("PACKAGE_NAME", PACKAGE_NAME)
    os.environ.setdefault("MODULE_REGEX", MODULE_REGEX)
    if re.match(MODULE_REGEX, PACKAGE_NAME):
        return
    print(f'ERROR: "{PACKAGE_NAME}" is not a valid Python module name!')
    print('Please try again using a name like "my_awesome_project".')
    sys.exit(1)


if __name__ == "__main__":
    try:
        main_pregen()
    except Exception as exc:  # pylint: disable=broad-except
        print(
            "Failed to execute the pre package generation process.\n Error "
            f"message: {exc}"
        )
        sys.exit(1)
