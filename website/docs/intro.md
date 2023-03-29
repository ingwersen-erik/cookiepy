***

sidebar_position: 1
title: Getting Started
authors: [ingwersen]
---------------------

![](../../docs/_static/EY_logo_5.gif)

[![Project Status](https://badgen.net/badge/status/alpha/d8624d)](https://badgen.net/badge/status/alpha/d8624d)
[![License](https://img.shields.io/github/license/ingwersen-erik/cookiepy)](https://opensource.org/licenses/MIT)
[![Read the documentation at https://cookiepy.readthedocs.io/](https://img.shields.io/readthedocs/cookiepy/latest.svg?label=Read%20the%20Docs)](https://cookiepy.readthedocs.io/)
[![Codecov](https://codecov.io/gh/ingwersen-erik/cookiepy-instance/branch/main/graph/badge.svg)](https://codecov.io/gh/ingwersen-erik/cookiepy-instance)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit\&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/ingwersen-erik/cookiepy/blob/main/CODE_OF_CONDUCT.rst)

***

## Descrição

Cookiecutter para automação da criação de repositório Python para projetos.

:::important

Esta ferramenta assume que você tenha um conhecimento prévio de como criar
pacotes em Python e, como usar ferramentas de versionamento de código
(GitHub, Bitbucket, Gitlab, etc.).

:::

***

## Quickstart

O `cookiepy` requer instalação prévia do pacote [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/).
Execute o seguinte comando para instalar o [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/):

```console

$ pip install cookiecutter
    
```

:::warning

Caso você não consiga executar o comando acima,
tente executar novamente, incluindo uma das opções `-U`, ou `--user`:

```console

$ pip install -U cookiecutter
# Mesmo que:
$ pip install --user cookiecutter

```

Alguns sistemas operacionais restringem a instalação de certos pacotes.
A opção `--user` força a instalação do pacote somente para o seu usuário.
Em geral, aplicações instaladas no diretório de usuário requerem
um nível menor de permissões. Muitas vezes, erros de falta de permissão são
solucionados, quando você realiza a instalação de aplicações ao nível de usuário,
ao invés de global. Esse bloqueio ocorre com bastante frequência no Windows,
especialmente em ambientes corporativos.

:::

Com o [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) instalado,
basta executar o seguinte comando:

```console

$ cookiecutter gh:ingwersen-erik/cookiepy

```

## Exemplo de Uso do `cookiepy`

O vídeo abaixo exemplifica o processo de criação de um novo projeto, utilizando o `cookiepy`:

![](../../docs/_static/demo-acelerador-dda.gif)

## Funcionalidades

O pacote `cookiepy` gera um pacote que configura automaticamente as seguintes funcionalidades:

*   Gerenciamento e empacotamento de pacotes usando [Poetry](https://python-poetry.org/)
*   Automatização de testes usando [Nox](https://nox.thea.codes/)
*   Avaliação de qualidade de código durante a etapa de
    [pre-commit](https://pre-commit.com/), usando
    [Flake8](http://flake8.pycqa.org)
*   Integração contínua através do uso de [GitHub Actions](https://github.com/features/actions)
*   Documentação de código usando [Sphinx](http://www.sphinx-doc.org/),
    [MyST](https://myst-parser.readthedocs.io/), e [Read the Docs](https://readthedocs.org/)
*   Geração automatizada de resumo das alterações e novas implementações
    da release com [Release Drafter](https://github.com/release-drafter/release-drafter)
*   Atualização automatizada de dependências com [Dependabot](https://dependabot.com/)
*   Formatação do código usando [Black](https://github.com/psf/black) e [Prettier](https://prettier.io/)
*   Ordenação dos imports do pacote com [isort](https://pycqa.github.io/isort/)
*   Framework de testes unitários [pytest](https://docs.pytest.org/en/latest/)
*   Geração de relatórios de coverage com [Codecov](https://codecov.io/)
*   Análise estática de código com [mypy](http://mypy-lang.org/)
*   Type-checking durante a execução com [Typeguard](https://github.com/agronholm/typeguard)
*   Atualização automatizada de sintaxe com [pyupgrade](https://github.com/asottile/pyupgrade)
*   Mudanças de sintaxe, conforme a versão do Python configurada pelo usuário, usando [pyupgrade](https://github.com/asottile/pyupgrade)
*   Análise de segurança com [Bandit](https://github.com/PyCQA/bandit) e [Safety](https://github.com/pyupio/safety)
*   Verificação dos exemplos da documentação com [xdoctest](https://github.com/Erotemic/xdoctest)
*   Gerenciamento de labels de repositório com [GitHub Labeler](https://github.com/marketplace/actions/github-labeler)

**Esta ferramenta foi testada nas seguintes versões do Python:** Python 3.8, 3.9, e 3.10.

***

# Informações Adicionais

## Estrutura deste Repositório

O `cookiepy` possui a seguinte estrutura de pastas:

```

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

```

## Como o cookiepy define um modelo de repositório

O processo de automação de geração de repositórios basicamente utiliza internamente
o framework que definido pelo [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/).
Sendo assim, todas as regras do `cookiepy` foram definidas em somente 2 arquivos:

1.  `pre_gen_project.py`: roteiro de instruções que precisam serem executadas **antes** da geração do repositório.
2.  `post_gen_project.py`: roteiro de instruções que precisam serem executadas **após** da geração do repositório.

Internamente, o [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/)
reconhece a existência de tais arquivos dentro do seu repositório e executa estes
scripts Python, seguindo a ordem de execução definida abaixo:

    ┌1─────────────────────────┐  ┌2───────────────────────────┐
    │     pre_gen_project.py   │  │Configurações do repositório│
    └────────────┬─────────────┘  └──────────────┬─────────────┘
                 │      ┌────────────────────────┘
                 ▼      ▼
    ┌3───────────┴──────┴──────┐
    │   Cookiecutter + Poetry  │
    │   gerando o repositório  │
    └────────────┬─────────────┘
                 ▼     
    ┌4───────────┴─────────────┐
    │   post_gen_project.py    │
    └────────────┬─────────────┘
                 ▼
        ┌5───────┴─────────┐
        │Repositório Gerado│
        └──────────────────┘

### Customização de parâmetros

Para adicionar novas configurações, com perguntas feitas para o usuário
durante a execução, primeiro é necessário alterar o arquivo
[`.cookiecutter.json`](../../cookiecutter.json). Dentro deste arquivo JSON, são
definidas todas as perguntas que o usuário precisa responder ao executar o comando
`cookiecutter gh:ingwersen-erik/cookiepy`.
O JSON requer que o nome do seu novo parâmetro seja definido como chave
e possíveis valores que o usuário pode responder, ou um valor pré-definido comum
deverão ser os valores desta chave.

## TODO :construction:

*   [ ] Traduzir o modelo para português.
    Inicialmente, a minha ideia era criar o cookiecutter em inglês,
    já que a maioria das empresas prefere que o código seja escrito em inglês.
*   [ ] Melhorar os tutoriais de como instalar/usar o `cookiepy`.
*   [ ] Adicionar tutoriais, com melhores práticas, dicas e casos-de-uso da ferramenta.
*   [ ] Incluir módulos com funções helpers que podem ser úteis para o usuário.
