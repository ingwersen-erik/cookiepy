EY-ML-Template Hooks
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
   :keywords: Cookiecutter, EY-ML-Template, Acelerador DDA
   :description lang=en: Readme dos hooks do pacote EY-ML-Template.

:abstract:
    Cookiecutter para o Acelerador de projetos EY DDA.

-------

Overview
--------

Os scripts `pre_gen_project.py` e `post_gen_project.py` são hooks utilizados pelo cookiecutter
para criação do repositório. Estes scripts definem o fluxo de geração de novos repositórios de acordo com os valores
que você definiu durante a execução do comando `cookiecutter EY-ML-Template.`.

Eles são responsáveis por:
Hooks que são executados pré e pós execução do comando `cookiecutter EY-ML-Template`.

Você pode alterar esses arquivos Python para customizar o processo que o `cookiecutter EY-ML-Template` executa
pré e pós a criação do projeto.
