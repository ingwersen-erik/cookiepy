"""Sphinx configuration."""
from datetime import datetime


project = "Cookiepy Python Project Cookiecutter"
project_name = "cookiepy"
author = "Erik Ingwersen"
github_user = 'ingwersen-erik'
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.intersphinx"]
intersphinx_mapping = {"mypy": ("https://mypy.readthedocs.io/en/stable/", None)}
language = "en"
html_theme = "furo"
html_logo = "_static/EY_logo_1.gif"
linkcheck_ignore = [
    "codeofconduct.html",
    "https://github.com/PyCQA/flake8-bugbear#",
    "https://github.com/peterjc/flake8-rst-docstrings#",
    "https://github.com/pre-commit/pre-commit-hooks#",
    "https://github.com/pycqa/pep8-naming#",
    "https://github.com/terrencepreilly/darglint#",
    "https://github.com/PyCQA/mccabe#",
    f"https://github.com/{github_user}/{project_name}/releases/tag/",
    f"https://{project_name}.readthedocs.io",
]
