---
sidebar_position: 1
title: Getting Started
authors: [erik]
---

![](../../docs/_static/EY_logo_1.gif)


[![Project Status](https://badgen.net/badge/status/alpha/d8624d)](https://badgen.net/badge/status/alpha/d8624d)
[![Python Version](https://img.shields.io/pypi/pyversions/cookiepy-instance)](https://github.com/ingwersen-erik/cookiepy)
[![License](https://img.shields.io/github/license/ingwersen-erik/cookiepy)](https://opensource.org/licenses/MIT)
[![Read the documentation at https://cookiepy.readthedocs.io/](https://img.shields.io/readthedocs/cookiepy/latest.svg?label=Read%20the%20Docs)](https://cookiepy.readthedocs.io/)
[![Codecov](https://codecov.io/gh/ingwersen-erik/cookiepy-instance/branch/main/graph/badge.svg)](https://codecov.io/gh/ingwersen-erik/cookiepy-instance)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/ingwersen-erik/cookiepy/blob/main/CODE_OF_CONDUCT.rst)

------------------------------------------------------------------------

## Descrição

Template para a criação e configuração de novos repositórios Python para
aplicações de ciência de dados.


------------------------------------------------------------------------

## Instruções de uso

Para usar esse template, você precisa instalar o pacote
[cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) no seu
ambiente de desenvolvimento Python:

```console
pip install cookiecutter
```

**Observação:** caso um erro ocorra, ao executar o comando acima, inclua
a opçao [-U]{.title-ref}, ou [\--user]{.title-ref} ao comando anterior:

```console
pip install -U cookiecutter
```

**ou:**

```console
pip install --user cookiecutter
```

Alguns sistemas bloqueiam a instalação de pacotes de terceiros.
A opção `--user` informa o Python que o pacote deve ser instalado
somente para o seu usuário. Esse tipo de bloqueio ocorre com bastante
frequência no Windows.

Após a instalação do [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/), execute
o seguinte comando:

``` console
$ cookiecutter gh:ingwersen-erik/cookiepy
```

## Exemplo do`cookiepy` em ação


![](../../docs/_static/demo-acelerador-dda.gif)


## Funcionalidades

Este template possui as seguintes funcionalidades, que são
automaticamente inclusas:

-   Gerenciamento e empacotamento de pacotes usando
    [Poetry](https://python-poetry.org/)
-   Automatização de testes usando [Nox](https://nox.thea.codes/)
-   Avaliação de qualidade de código durante a etapa de
    [pre-commit](https://pre-commit.com/), usando
    [Flake8](http://flake8.pycqa.org)
-   Integração contínua através do uso de [GitHub
    Actions](https://github.com/features/actions)
-   Documentação de código usando [Sphinx](http://www.sphinx-doc.org/),
    [MyST](https://myst-parser.readthedocs.io/), e [Read the
    Docs](https://readthedocs.org/)
-   Geração automatizada de resumo das alterações e novas implementações
    da release com [Release
    Drafter](https://github.com/release-drafter/release-drafter)
-   Atualização automatizada de dependências com
    [Dependabot](https://dependabot.com/)
-   Formatação do código usando [Black](https://github.com/psf/black) e
    [Prettier](https://prettier.io/)
-   Ordenação dos imports do pacote com
    [isort](https://pycqa.github.io/isort/)
-   Framework de testes unitários
    [pytest](https://docs.pytest.org/en/latest/)
-   Geração de relatórios de coverage com [Codecov](https://codecov.io/)
-   Análise estática de código com [mypy](http://mypy-lang.org/)
-   Type-checking durante a execução com
    [Typeguard](https://github.com/agronholm/typeguard)
-   Atualização automatizada de sintaxe com
    [pyupgrade](https://github.com/asottile/pyupgrade)
-   Análise de segurança com [Bandit](https://github.com/PyCQA/bandit) e
    [Safety](https://github.com/pyupio/safety)
-   Verificação dos exemplos da documentação com
    [xdoctest](https://github.com/Erotemic/xdoctest)
-   Gerenciamento de labels de repositório com [GitHub
    Labeler](https://github.com/marketplace/actions/github-labeler)

**Versões Python suportadas:** Python 3.7, 3.8, 3.9, e 3.10.

## Estrutura do repositório

``` text
cookiepy
├── CODE_OF_CONDUCT.rst             <- Código de conduta (copiado de outros templates).
├── CONTRIBUTING.rst                <- Guia de contribuição. Está em inglês.
├── LICENSE.rst                     <- Licença do projeto (por enquanto está como MIT)
├── README.rst                      <- Este arquivo que você está lendo.
├── cookiecutter.json               <- Instruções para a geração do template.
├── docs                            <- Diretório com arquivos da documentação.
├── hooks                           <- Diretório contêm os hooks pré e pós execução do comando cookiecutter.
├── noxfile.py                      <- Arquivo nox
├── poetry.lock                     <- Dependências do projeto.
├── pycharm.sh                      <- Arquivo para inicializar o PyCharm.
├── pyproject.toml                  <- Configurações do projeto.
├── tools                           <- ferramentas extras para o desenvolvimento do cookiepy.
└── {{cookiecutter.project_name}}   <- Template do pacote que será criado.
```

# TO-DO

- [ ] Traduzir o template para português. A minha intenção inicial
    era criar o cookiecutter em inglês, por uma facilidade minha em
    escrever em inglês e também porque a maioria dos projetos requrem
    código escrito em inglês.
- [ ] Melhorar tutoriais de como usar.
- [ ] Criar tutoriais, explicando a functionalidade de cada ferramenta.
