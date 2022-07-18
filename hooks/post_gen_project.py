#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hooks called after generating the project structure.
"""

from __future__ import annotations, print_function

import contextlib
import json
import os
import sys
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
COOKIECUTTER_FILE = '.cookiecutter.json'


def reindent_cookiecutter_json(cookiecutter_json: str | Path = COOKIECUTTER_FILE) -> None:
    """
    Indent `.cookiecutter.json <./.cookiecutter.json>`_ using two spaces.

    "jsonify" extension uses an indentation width of four spaces.
    This indentation width conflicts with the default indentation required by
    Prettier for JSON files. Code executes Prettier as a pre-commit hook in
    continuous integration (CI). Pre-commit hooks define a set of rules and
    transformations, applied to the project files before the user pushes new commits
    to the repository.

    Parameters
    ----------
    cookiecutter_json : str | Path, optional
        The filepath of the `.cookiecutter.json <./.cookiecutter.json>`_ file.
        The default is `./.cookiecutter.json`.

    Raises
    ------
    FileNotFoundError
        If the `.cookiecutter.json <./.cookiecutter.json>`_ file doesn't exist.
        Error might occur if the `.cookiecutter.json <./.cookiecutter.json>`_
        file gets deleted by the user.
    """
    path = Path(cookiecutter_json)

    if not path.is_file():
        raise FileNotFoundError(f"{path} does not exist.")

    with path.open(mode='r', encoding='utf-8') as io:
        data = json.load(io)

    with path.open(mode='w', encoding='utf-8') as io:
        json.dump(data, io, sort_keys=True, indent=2)
        io.write('\n')


def remove_file(filepath: str | Path) -> None:
    """Remove a file using its `filepath`.

    Parameters
    ----------
    filepath : str | Path
        The filepath of the file to be removed.

    Examples
    --------
    The following example, creates a fake file, proves it exists, and then removes it.
    >>> from pathlib import Path
    >>> import os
    >>> import subprocess
    >>> test_path = 'test'
    >>> test_path = Path(test_path + str(hash(test_path))).with_suffix('.txt')
    >>> test_path.touch(exist_ok=True)
    >>> if os.name != 'nt':
    ...     resp = subprocess.run(['ls'], capture_output=True).stdout
    ... else:
    ...     resp = subprocess.run(['dir'], capture_output=True).stdout
    >>> print('b{}'.format(test_path.name) in resp)  # noqa
    True
    >>> remove_file(test_path)
    >>> print('b{}'.format(test_path.name) in resp)  # noqa
    False
    """
    with contextlib.suppress(FileNotFoundError):
        os.remove(os.path.join(PROJECT_DIRECTORY, str(filepath)))


def create_dotenv(project_filepath: str | Path = PROJECT_DIRECTORY) -> None:
    """
    Create a `.env` file inside the project directory.

    The `.env` file stores environment variables. The environment variables
    often store sensitive information like passwords.
    Also, you might use `.env` to define configurations
    that vary with machine. For example, directories paths of the
    package and other files.

    Parameters
    ----------
    project_filepath : str | Path, default: `PROJECT_DIRECTORY`
        The path of the project. The default is the current working directory.

    .. tip::

        You can add extra values to store in the `.env` file by adding
        them to the `env_configs` dictionary defined inside the `create_dotenv`
        function. When defining variables to store paths information, try to
        name the variable, ending with the "_DIRECTORY" suffix. This function
        uses this suffix to determine which values represent directories, and
        creates them if they don't exist. Another way to do this is to
        change the `if 'DIRECTORY' in config_name:...` condition, replacing
        the word “DIRECTORY” to the desired one. If you use the later option,
        don't forget to change the suffix used in the `env_configs` keys
        names.
    """
    project_filepath = Path(project_filepath)
    env_filepath = project_filepath.joinpath('.env')
    env_filepath.touch(exist_ok=True)
    env_configs = {
        'PROJECT_NAME': '{{ cookiecutter.project_name }}',
        'PACKAGE_NAME': '{{ cookiecutter.package_name }}',
        'PROJECT_DIRECTORY': str(project_filepath.resolve()),
        'PACKAGE_DIRECTORY': str(
            project_filepath.joinpath(
                f'src{os.path.sep}{"{{ cookiecutter.package_name }}"}'
            )
        ),
        'LOGS_DIRECTORY': str(project_filepath.joinpath('logs')),
        'DATA_DIRECTORY': str(project_filepath.joinpath('data')),
        'DATA_RAW_DIRECTORY': str(project_filepath.joinpath(f'data{os.path.sep}raw')),
        'DATA_OUTPUT_DIRECTORY': str(project_filepath.joinpath(f'data{os.path.sep}outputs')),
        'OUTPUTS_DIRECTORY': str(project_filepath.joinpath('outputs')),
    }
    with open(str(env_filepath), 'w', encoding='utf-8') as fp:
        for config_name, config_value in env_configs.items():
            if 'DIRECTORY' in config_name:
                Path(config_value).mkdir(parents=True, exist_ok=True)
            fp.write(f'{config_name}="{config_value}"\n')
            os.environ.setdefault(config_name, config_value)
        fp.close()


if __name__ == "__main__":

    reindent_cookiecutter_json()

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.md')
        remove_file('docs/authors.md')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.package_name }}', 'cli.py')
        remove_file(cli_file)

    create_dotenv()
    sys.path.insert(0, os.environ.get('PROJECT_DIRECTORY'))
    if '{{ cookiecutter.use_poetry|lower }}' in {'y', 1, True}:
        try:
            import poetry  # noqa
        except ImportError:
            os.system('pip install -U poetry')
        finally:
            os.system('poetry update')
            requirements_output = Path(PROJECT_DIRECTORY).joinpath('requirements.txt')
            if requirements_output.exists():
                remove_file(requirements_output)
            os.system(f'poetry export --output {requirements_output} --without-hashes --ansi')
