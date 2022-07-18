"""
Print restructuredText ('.rst') table of dependencies.
"""
from __future__ import absolute_import, division, print_function
import argparse
import datetime
import os
import re
from pathlib import Path

try:
    import tomli
except ImportError:
    print('Installing `tomli` package, required to run this script.')
    os.system('pip install -U tomli')
    import tomli  # noqa


PROJECT = Path('{{cookiecutter.project_name}}')
max_tries = 1


# If you're running from the “tools” directory.
while not PROJECT.is_dir() and max_tries > 0:
    PROJECT = Path('..').joinpath(PROJECT)
    max_tries -= 1

# If the script can't find the project directory.
if max_tries == 0 and not PROJECT.is_dir():
    raise FileNotFoundError(f'Could not find project directory: {PROJECT}')

JINJA_PATTERN = re.compile(r'{%.*%}')
JINJA_PATTERN2 = re.compile(r'{{[^{]*}}')
LINE_FORMAT = '   {name:{width}} {description}'
CANONICALIZE_PATTERN = re.compile(r'[-_.]+')
DESCRIPTION_PATTERN = re.compile(r'\. .*')

args_parser = argparse.ArgumentParser()
args_parser.add_argument('--save', default=False, type=bool)
args = args_parser.parse_args()


def canonicalize_name(name: str) -> str:
    # From ``packaging.utils.canonicalize_name`` (PEP 503)
    return CANONICALIZE_PATTERN.sub('-', name).lower()


def truncate_description(description: str) -> str:
    """Truncate the description to the first sentence."""
    return DESCRIPTION_PATTERN.sub('.', description)


def format_dependency(dependency: str) -> str:
    """Format the dependency for the table."""
    return 'coverage__' if dependency == 'coverage' else f'{dependency}_'


def main(save: bool = False) -> None:
    """Print restructuredText table of dependencies.

    Parameters
    ----------
    save : bool, default=False
        Save the table to a file. If `True`, saves contents to a file named
        "dependencies_YYYY-MM-DD.rst".

    Examples
    --------
    >>> main()
    '''
    ====================== ====================================================================================
    black_                 The uncompromising code formatter.
    click_                 Composable command line interface toolkit
    coverage__             Code coverage measurement for Python
    darglint_              A utility for ensuring Google-style docstrings stay up to date with the source code.
    ====================== ====================================================================================
    '''

    Notes
    -----
    If a description to a dependency doesn't exist, function will leave it  blank.
    """
    path = Path(f'{PROJECT}{os.path.sep}pyproject.toml')
    text = path.read_text()
    text = JINJA_PATTERN.sub('', text)
    text = JINJA_PATTERN2.sub('x', text)
    data = tomli.loads(text)

    dependencies = {
        canonicalize_name(dependency)
        for section in ['dependencies', 'dev-dependencies']
        for dependency in data['tool']['poetry'][section].keys()
        if dependency != 'python'
    }

    path = Path(f'{PROJECT}{os.path.sep}poetry.lock')
    text = path.read_text()
    data = tomli.loads(text)

    descriptions = {
        canonicalize_name(package['name']): truncate_description(package['description'])
        for package in data['package']
        if package['name'] in dependencies
    }

    table = {
        format_dependency(dependency): descriptions.get(dependency, '')
        for dependency in sorted(dependencies)
    }

    width = max(len(name) for name in table)
    width2 = max(len(description) for description in table.values())
    separator = LINE_FORMAT.format(
        name='=' * width, width=width, description='=' * width2
    )
    
    dependecies_table: str = separator + '\n'
    print(separator)

    for name, description in table.items():
        line = LINE_FORMAT.format(name=name, width=width, description=description)
        dependecies_table += line + '\n'
        print(line)
    dependecies_table += separator + '\n'
    print(separator)
    
    if save:
        now = datetime.datetime.now()
        filename = f'dependencies_{now.strftime("%Y-%m-%d")}.rst'
        path = PROJECT.joinpath('..').joinpath(filename).resolve()
        path.write_text(dependecies_table)
        print(f'Saved dependecies table to \"{path}\"')


if __name__ == '__main__':
    SAVE_TABLE = args.save  # Change to True to save the table to a file.
    main(SAVE_TABLE)
