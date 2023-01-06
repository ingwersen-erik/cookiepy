.. Logo EY

.. raw:: html

   <p align="center"><img align="left" style="object-fit: none; object-position: -120px 120px; width: 100px; height: 120px" src="./docs/_static/EY_logo_1.gif" alt="EY Logo"></p><br><h1>  cookiepy</h1><br>

.. badges-begin

| |Status| |Python Version| |License| |Read the Docs| |Codecov|
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

.. raw:: html

   <br>

.. Project authors:
.. _Erik Ingwersen: https://github.com/ingwersen-erik

.. Project Wiki:
.. _EY DDA: https://www.ey.com/en_gl/big-data-analytics

.. bibliographic fields:

:Author: `Erik Ingwersen`_
:Contact: erik.ingwersen@br.ey.com
:organization: `EY DDA`_
:date: 2022-09-09 (Thu, 09 Sep 2022)
:status: Pre-Alpha
:version: 0.1.0
:copyright: Copyright (c) EY Brazil, Inc. and its affiliates. All Rights Reserved.

.. meta::
   :keywords: Cookiecutter, cookiepy, Acelerador DDA
   :description lang=pt: Readme do pacote cookiepy.

:abstract:
    Cookiecutter para o Acelerador de projetos EY DDA.

-----

Descrição
=========

Cookiecutter para automação da criação de repositório Python para projetos.

**:warning: Importante:** Esta ferramenta assume que você tenha um conhecimento
prévio de como criar pacotes em Python e, como usar ferramentas de
versionamento de código (GitHub, Bitbucket, Gitlab, etc.).


Documentação do Projeto
=======================

✨📚✨ `Link para documentação`__

__ https://cookiepy.readthedocs.io/

-----

Quickstart
----------

O ``cookiepy`` requer instalação prévia do pacote `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_.
Execute o seguinte comando para instalar o ``cookiecutter``:

.. code-block:: console

    $ pip install cookiecutter


**:bulb: Observação:** caso você não consiga executar o comando acima,
tente executar novamente,
incluindo a opçao ``-U``, ou ``--user``:

.. code-block:: console

    $ pip install -U cookiecutter
    # Mesmo que:
    $ pip install --user cookiecutter

Alguns sistemas operacionais restringem a instalação de certos pacotes.
A opção ``--user`` força a instalação do pacote somente para o seu usuário.
Em geral, aplicações que são instaladas dentro do diretório de usuário requerem
um nível menor de permissões. Muitas vezes, erros de falta de permissão são
solucionados, quando você realiza a instalação de aplicações a nível de usuário,
ao invés de global. Esse tipo de bloqueio ocorre com bastante frequência no Windows,
especialmente em ambientes corporativos.

Com o `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_ instalado,
basta executar o seguinte comando:

.. code-block:: console

   $ cookiecutter gh:ingwersen-erik/cookiepy


Exemplo de Uso do ``cookiepy``
------------------------------

O vídeo abaixo mostra o processo de criação de um novo projeto, utilizando o ``cookiepy``:

.. raw:: html

   <p align="center"><img src="./docs/_static/demo-acelerador-dda.gif" alt="Demo"/></p>
   <br>


Funcionalidades
===============

O pacote gerado pelo ``cookiepy`` possui as seguintes funcionalidades pré-configuradas:

.. features-begin

- Gerenciamento e empacotamento de pacotes, usando Poetry_
- Automação de testes unitários, usando Nox_
- Avaliação de qualidade do seu código durante o commit_, usando Flake8_
- Serviços de CI/CD, com ações pré-configuradas, usando `GitHub Actions`_
- Automação do processo de geração de documentação do seu código-fonte usando `Sphinx`_, MyST_, e `Read the Docs`_
- Criação automática de change-logs, usando `Release Drafter`_
- Atualização automática de dependências com Dependabot_
- Formatação do código usando `Black`_ e Prettier_
- Ordenação e validação de imports dos módulos do seu código, com o isort_
- Relatório de cobertura de código (coverage), usando Codecov_
- Análise estática e type-hints com mypy_
- Análise dinâmica de type-hints, com Typeguard_
- Mudanças de sintaxe, de acordo com a versão do Python configurada pelo usuário, usando pyupgrade_
- Análise estática de segurança com Bandit_ e Safety_
- Validação de exemplos de código escritos na documentação com xdoctest_
- Gerenciamento de labels de repositório com `GitHub Labeler`_


**Esta ferramenta foi testada nas seguintes versões do Python:** Python 3.7, 3.8, 3.9, e 3.10.

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


----

Informações Adicionais
======================


Estrutura do repositório
------------------------

O ``cookiepy`` possui a seguinte estrutura de pastas:

.. code-block:: text

    cookiepy
    ├── CODE_OF_CONDUCT.rst             <- Código de conduta (copiado de outros templates).
    ├── CONTRIBUTING.rst                <- Guia de contribuição. Está em inglês.
    ├── LICENSE.rst                     <- Licença do projeto (por enquanto está como MIT)
    ├── README.rst                      <- Este arquivo que você está lendo.
    ├── cookiecutter.json               <- Arquivo com os parâmetros utilizado pelo cookiepy para gerar novos repositórios
    ├── docs                            <- Diretório com a documentação da ferramenta.
    ├── noxfile.py                      <- Arquivo nox com as configurações de testes unitários.
    ├── pycharm.sh                      <- Comando Mac/Linux para inicialização do PyCharm (se instalado).
    ├── pyproject.toml                  <- Arquivos com as configurações e dependencias da ferramenta.
    ├── tools                           <- scripts para automação CI/CD.
    │   ├── dependencies_table.py       <- Script analisa os scripts Python do projeto e gera uma tabela de dependências.
    │   ├── prepare_github_release.py   <- Script de preparação de novas releases.
    │   └── publish_github_release.py   <- Script de publicação de releases em repositório do GitHub.
    ├── hooks                           <- Diretório com os arquivos utilizados para criação do repositório.
    │   ├── post_gen_project.py         <- Script executado após a geração do repositório.
    │   └── pre_gen_project.py          <- Script executado antes da geração do repositório.
    └── {{cookiecutter.project_name}}   <- Template do pacote que será criado.


TO-DO :construction: 
--------------------

- [ ] Traduzir o template para português :brazil:.
  Inicialmente, a minha ideia era criar o cookiecutter em inglês,
  já que a maioria das empresas preferem que o código seja escrito em inglês.
- [ ] Melhorar os tutoriais de como instalar/usar o ``cookiepy``. :basecamp:
- [ ] Adicionar tutoriais, com melhores práticas, dicas e casos-de-uso da ferramenta. :bulb:
