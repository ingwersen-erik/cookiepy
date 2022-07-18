.. raw:: html

   <p align="center"><img align="left" width="120" height="120" src="./docs/_static/EY_logo_1.gif" alt="EY Logo"></p>


========
cookiepy
========

.. badges-begin

| |Status| |Python Version| |License|
| |Read the Docs| |Codecov|
| |pre-commit| |Black| |Contributor Covenant|

.. |Status| image:: https://badgen.net/badge/status/alpha/d8624d
   :target: https://badgen.net/badge/status/alpha/d8624d
   :alt: Project Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/cookiepy-instance
   :target: https://github.com/ingwersen-erik/cookiepy
   :alt: Python Version
.. |License| image:: https://img.shields.io/github/license/ingwersen-erik/cookiepy
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/cookiepy/latest.svg?label=Read%20the%20Docs
   :target: https://cookiepy.readthedocs.io/
   :alt: Read the documentation at https://cookiepy.readthedocs.io/
.. |Codecov| image:: https://codecov.io/gh/ingwersen-erik/cookiepy-instance/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/ingwersen-erik/cookiepy-instance
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black
.. |Contributor Covenant| image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
   :target: https://github.com/ingwersen-erik/cookiepy/blob/main/CODE_OF_CONDUCT.rst
   :alt: Contributor Covenant

.. badges-end


✨📚✨ `Read the full documentation`__

__ https://cookiepy.readthedocs.io/


Descrição
=========

Template para a criação e configuração de novos repositórios Python para aplicações de
ciência de dados.


Instruções de uso
-----------------

Para usar esse template, você precisa instalar o pacote `cookiecutter
<https://cookiecutter.readthedocs.io/en/latest/>`_ no seu ambiente de desenvolvimento
Python:

.. code-block:: console

    pip install cookiecutter


**Observação:** caso um erro ocorra, ao executar o comando acima, inclua a opçao `-U`, ou
`--user` ao comando anterior:

.. code-block:: console

    pip install -U cookiecutter

ou:

.. code-block:: console

    pip install --user cookiecutter

Alguns sistemas bloqueiam a instalação de pacotes de terceiros.
A opção `--user` informa o Python que o pacote deve ser instalado
somente para o seu usuário. Esse tipo de bloqueio ocorre com bastante
frequência no Windows.

Após a instalação do `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_,
execute o seguinte comando:

.. code-block:: console

   $ cookiecutter gh:ingwersen-erik/cookiepy


Exemplo do `cookiepy` em ação
-----------------------------

.. raw:: html

   <img align="left" width="540" height="540" src="./docs/_static/demo-acelerador-dda
.gif" alt="Demo">



Funcionalidades
===============

Este template possui as seguintes funcionalidades, que são automaticamente inclusas:

.. features-begin

- Gerenciamento e empacotamento de pacotes usando Poetry_
- Automatização de testes usando Nox_
- Avaliação de qualidade de código durante a etapa de pre-commit_, usando Flake8_
- Integração contínua através do uso de `GitHub Actions`_
- Documentação de código usando `Sphinx`_, MyST_, e `Read the Docs`_
- Geração automatizada de resumo das alterações e novas implementações da release com `Release Drafter`_
- Atualização automatizada de dependências com Dependabot_
- Formatação do código usando `Black`_ e Prettier_
- Ordenação dos imports do pacote com isort_
- Framework de testes unitários pytest_
- Geração de relatórios de coverage com Codecov_
- Análise estática de código com mypy_
- Type-checking durante a execução com Typeguard_
- Atualização automatizada de sintaxe com pyupgrade_
- Análise de segurança com Bandit_ e Safety_
- Verificação dos exemplos da documentação com xdoctest_
- Gerenciamento de labels de repositório com `GitHub Labeler`_


**Versões Python suportadas:** Python 3.7, 3.8, 3.9, e 3.10.

.. features-end

.. references-begin

.. _Bandit: https://github.com/PyCQA/bandit
.. _Black: https://github.com/psf/black
.. _Click: https://click.palletsprojects.com/
.. _Codecov: https://codecov.io/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Coverage.py: https://coverage.readthedocs.io/
.. _Dependabot: https://dependabot.com/
.. _Flake8: http://flake8.pycqa.org
.. _GitHub Actions: https://github.com/features/actions
.. _Hypermodern Python: https://medium.com/@ingwersen-erik/hypermodern-python-d44485d9d769
.. _isort: https://pycqa.github.io/isort/
.. _MyST: https://myst-parser.readthedocs.io/
.. _Nox: https://nox.thea.codes/
.. _Poetry: https://python-poetry.org/
.. _Prettier: https://prettier.io/
.. _PyPI: https://pypi.org/
.. _Read the Docs: https://readthedocs.org/
.. _Release Drafter: https://github.com/release-drafter/release-drafter
.. _Safety: https://github.com/pyupio/safety
.. _Sphinx: http://www.sphinx-doc.org/
.. _TestPyPI: https://test.pypi.org/
.. _Typeguard: https://github.com/agronholm/typeguard
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _furo: https://pradyunsg.me/furo/
.. _mypy: http://mypy-lang.org/
.. _napoleon: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/latest/
.. _pyupgrade: https://github.com/asottile/pyupgrade
.. _sphinx-click: https://sphinx-click.readthedocs.io/
.. _xdoctest: https://github.com/Erotemic/xdoctest
.. _GitHub Labeler: https://github.com/marketplace/actions/github-labeler

.. references-end


Estrutura do repositório
========================

.. raw: txt

    .
    ├── CODE_OF_CONDUCT.rst             <- Código de conduta (copiado de outros templates).
    ├── CONTRIBUTING.rst                <- Guia de contribuição. Está em inglês.
    ├── LICENSE.rst                     <- Licença do projeto (por enquanto está como MIT)
    ├── README.rst                      <- Este arquivo que você está lendo.
    ├── cookiecutter.json               <- Instruções para a geração do template.
    ├── docs                            <- Diretório com arquivos da documentação.
    ├── hooks                           <- Diretório contêm os hooks pré e pós execução do comando cookiecutter.
    ├── noxfile.py                      <-
    ├── poetry.lock                     <- Dependências do projeto.
    ├── pycharm.sh                      <- Arquivo para inicializar o PyCharm.
    ├── pyproject.toml
    ├── tools                           <- ferramentas extras para o desenvolvimento do cookiepy.
    └── {{cookiecutter.project_name}}   <- Template do pacote que será criado.



TO-DO
=====

- [ ] Traduzir o template para português. A minha intenção inicial era criar o
cookiecutter em inglês, por uma facilidade minha em escrever em inglês e também porque
a maioria dos projetos requrem código escrito em inglês.
