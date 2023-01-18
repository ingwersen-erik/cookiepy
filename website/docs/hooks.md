***

sidebar\_position: 1
title: Cookiepy Hooks
authors: \[ingwersen]
---------------------

## Overview

Hooks que são executados pré e pós execução do comando `cookiecutter cookiepy`.

:::tip

Você pode alterar esses arquivos Python para customizar o processo que o
`cookiecutter cookiepy` executa pré e pós a criação do projeto.

:::

### `hooks/pre_gen_project.py`

O código abaixo é um exemplo de código Python que será executado antes da
criação do projeto.

```python

import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.module_name }}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: %s is not a valid Python module name!' % module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)
```

O código acima verifica o nome do pacote Python que o usuário informou no
`cookiecutter cookiepy` e, caso não seja válido, exibe uma mensagem de erro e
interrompe o processo de criação do projeto.

:::note

Certifique-se de que seus hook scripts funcionem de maneira robusta.
Se um script do diretório `hooks` falhar, ou seja, se terminar com um status de saída diferente de zero,
a geração do projeto será interrompida e o diretório gerado será limpo.

:::
