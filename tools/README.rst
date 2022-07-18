Cookiepy Tools
==============

.. Links:


.. Project authors:
.. _Erik Ingwersen: https://github.com/ingwersen-erik

.. Project Wiki:
.. _EY DDA: https://www.ey.com/en_gl/big-data-analytics

.. bibliographic fields:

:Author: `Erik Ingwersen`_
:Contact: erik.ingwersen@br.ey.com
:organization: `EY DDA`_
:date: 2022-06-18 (Mon, 18 Jul 2022)
:status: Pre-Alpha
:version: 1.0
:copyright: Copyright (c) EY Brazil, Inc. and its affiliates. All Rights Reserved.

.. meta::
   :keywords: Cookiecutter, cookiepy, Acelerador DDA
   :description lang=en: Readme das ferramentas do pacote cookiepy.

:abstract:
    Cookiecutter para o Acelerador de projetos EY DDA.

-------

Overview
--------

Ferramentas extras para o Acelerador de Projetos EY DDA.

Ferramentas
-----------

- `dependencies-table.py <./dependencies-table.py>`_: Gerador de tabela de dependências.
- `prepare-github-release.py <./prepare-github-release.py>`_: Prepara o release para ser publicado no GitHub.
- `publish-github-release.py <./publish-github-release.py>`_: Publica o release para o repositório do projeto no GitHub.


`dependencies-table.py`
~~~~~~~~~~~~~~~~~~~~~

Para usar a ferramenta, basta executar o comando abaixo:

.. code-block:: console

    $ python tools/dependencies-table.py

Ou, se quiser salvar o output em um arquivo, basta executar o comando abaixo:

.. code-block:: console

    $ python tools/dependencies-table.py --save True

O comando acima irá salvar a tabela como um arquivo no formato ".rst" dentro da
pasta `cookiepy <../>`_, com o nome `dependencies_YYYY-MM-DD.rst`.

**Exemplo de output:**

====================== ====================================================================================
black_                 The uncompromising code formatter.
click_                 Composable command line interface toolkit
coverage__             Code coverage measurement for Python
darglint_              A utility for ensuring Google-style docstrings stay up to date with the source code.
flake8_                the modular source code checker: pep8 pyflakes and co
flake8-annotations_
flake8-bandit_         Automated security testing with bandit and flake8.
flake8-bugbear_        A plugin for flake8 finding likely bugs and design problems in your program.
flake8-docstrings_     Extension for flake8 which uses pydocstyle to check docstrings
flake8-rst-docstrings_ Python docstring reStructuredText (RST) validator
furo_                  A clean customisable Sphinx documentation theme.
isort_                 A Python utility / library to sort Python imports.
mypy_                  Optional static typing for Python
myst-parser_           An extended commonmark compliant parser, with bridges to docutils & sphinx.
pep8-naming_           Check PEP-8 naming conventions, plugin for flake8
pre-commit_            A framework for managing and maintaining multi-language pre-commit hooks.
pre-commit-hooks_      Some out-of-the-box hooks for pre-commit.
pygments_              Pygments is a syntax highlighting package written in Python.
pytest_                pytest: simple powerful testing with Python
python-dotenv_
pyupgrade_             A tool to automatically upgrade syntax for newer versions.
safety_                Checks installed dependencies for known vulnerabilities.
sphinx_                Python documentation generator
sphinx-autobuild_      Rebuild Sphinx documentation on changes, with live-reload in the browser.
sphinx-click_          Sphinx extension that automatically documents click applications
typeguard_             Run-time type checker for Python
xdoctest_              A rewrite of the builtin doctest module
====================== ====================================================================================
