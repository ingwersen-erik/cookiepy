#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from setuptools import setup
from pathlib import Path


requirements_path = Path('requirements.txt').resolve()
if requirements_path.is_file():
    with open(
        requirements_path,
        errors='ignore',
        encoding='utf-8',
        buffering=1,
        mode='r',
    ) as fp:
        requirements = fp.read().splitlines()
        fp.close()
else:
    print('No requirements.txt found. Skipping.')
    # Empty requirements list to avoid error
    requirements = []

setup(
    name='{{ cookiecutter.project_name }}',
    { % - if cookiecutter.setup_py_uses_setuptools_scm == 'y' %}
    use_scm_version = {
        'local_scheme': 'dirty-tag',
        'write_to': 'src/{{ cookiecutter.package_name }}/_version.py',
        'fallback_version': '{{ cookiecutter.version }}',
    },
    { % - else %}
    version = '{{ cookiecutter.version }}',
    { % - endif %}
    description="{{ cookiecutter.short_description }}",
    license="{{ cookiecutter.license }}",
    author="{{ cookiecutter.author }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    package_dir={'': 'src'},
    packages=['{{ cookiecutter.package_name }}'],
    {% if cookiecutter.command_line_interface != "n" -%}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.cli:main'
        ]
    },
    {%- endif %}
    install_requires=requirements,
    keywords='{{ cookiecutter.project_name }}',
)