"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[671],{9881:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>r,contentTitle:()=>n,default:()=>l,frontMatter:()=>i,metadata:()=>s,toc:()=>p});var o=a(7462),A=(a(7294),a(3905));const i={sidebar_position:1,title:"Getting Started",authors:["erik"]},n=void 0,s={unversionedId:"intro",id:"intro",title:"Getting Started",description:"Project Status",source:"@site/docs/intro.md",sourceDirName:".",slug:"/intro",permalink:"/cookiepy/docs/intro",draft:!1,editUrl:"https://github.com/ingwersen-erik/cookiepy/docs/intro.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1,title:"Getting Started",authors:["erik"]},sidebar:"tutorialSidebar"},r={},p=[{value:"Descri\xe7\xe3o",id:"descri\xe7\xe3o",level:2},{value:"Instru\xe7\xf5es de uso",id:"instru\xe7\xf5es-de-uso",level:2},{value:"Exemplo do<code>cookiepy</code> em a\xe7\xe3o",id:"exemplo-docookiepy-em-a\xe7\xe3o",level:2},{value:"Funcionalidades",id:"funcionalidades",level:2},{value:"Estrutura do reposit\xf3rio",id:"estrutura-do-reposit\xf3rio",level:2}],c={toc:p};function l(e){let{components:t,...i}=e;return(0,A.kt)("wrapper",(0,o.Z)({},c,i,{components:t,mdxType:"MDXLayout"}),(0,A.kt)("p",null,(0,A.kt)("img",{src:a(3870).Z,width:"204",height:"239"})),(0,A.kt)("p",null,(0,A.kt)("a",{parentName:"p",href:"https://badgen.net/badge/status/alpha/d8624d"},(0,A.kt)("img",{parentName:"a",src:"https://badgen.net/badge/status/alpha/d8624d",alt:"Project Status"})),"\n",(0,A.kt)("a",{parentName:"p",href:"https://github.com/ingwersen-erik/cookiepy"},(0,A.kt)("img",{parentName:"a",src:"https://img.shields.io/pypi/pyversions/cookiepy-instance",alt:"Python Version"})),"\n",(0,A.kt)("a",{parentName:"p",href:"https://opensource.org/licenses/MIT"},(0,A.kt)("img",{parentName:"a",src:"https://img.shields.io/github/license/ingwersen-erik/cookiepy",alt:"License"})),"\n",(0,A.kt)("a",{parentName:"p",href:"https://cookiepy.readthedocs.io/"},(0,A.kt)("img",{parentName:"a",src:"https://img.shields.io/readthedocs/cookiepy/latest.svg?label=Read%20the%20Docs",alt:"Read the documentation at https://cookiepy.readthedocs.io/"})),"\n",(0,A.kt)("a",{parentName:"p",href:"https://codecov.io/gh/ingwersen-erik/cookiepy-instance"},(0,A.kt)("img",{parentName:"a",src:"https://codecov.io/gh/ingwersen-erik/cookiepy-instance/branch/main/graph/badge.svg",alt:"Codecov"})),"\n",(0,A.kt)("a",{parentName:"p",href:"https://github.com/pre-commit/pre-commit"},(0,A.kt)("img",{parentName:"a",src:"https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white",alt:"pre-commit"})),"\n",(0,A.kt)("a",{parentName:"p",href:"https://github.com/psf/black"},(0,A.kt)("img",{parentName:"a",src:"https://img.shields.io/badge/code%20style-black-000000.svg",alt:"Black"})),"\n",(0,A.kt)("a",{parentName:"p",href:"https://github.com/ingwersen-erik/cookiepy/blob/main/CODE_OF_CONDUCT.rst"},(0,A.kt)("img",{parentName:"a",src:"https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg",alt:"Contributor Covenant"}))),(0,A.kt)("hr",null),(0,A.kt)("h2",{id:"descri\xe7\xe3o"},"Descri\xe7\xe3o"),(0,A.kt)("p",null,"Template para a cria\xe7\xe3o e configura\xe7\xe3o de novos reposit\xf3rios Python para\naplica\xe7\xf5es de ci\xeancia de dados."),(0,A.kt)("hr",null),(0,A.kt)("h2",{id:"instru\xe7\xf5es-de-uso"},"Instru\xe7\xf5es de uso"),(0,A.kt)("p",null,"Para usar esse template, voc\xea precisa instalar o pacote\n",(0,A.kt)("a",{parentName:"p",href:"https://cookiecutter.readthedocs.io/en/latest/"},"cookiecutter")," no seu\nambiente de desenvolvimento Python:"),(0,A.kt)("pre",null,(0,A.kt)("code",{parentName:"pre",className:"language-console"},"pip install cookiecutter\n")),(0,A.kt)("p",null,(0,A.kt)("strong",{parentName:"p"},"Observa\xe7\xe3o:")," caso um erro ocorra, ao executar o comando acima, inclua\na op\xe7ao ","[-U]","{.title-ref}, ou ","[-","-user]","{.title-ref} ao comando anterior:"),(0,A.kt)("pre",null,(0,A.kt)("code",{parentName:"pre",className:"language-console"},"pip install -U cookiecutter\n")),(0,A.kt)("p",null,(0,A.kt)("strong",{parentName:"p"},"ou:")),(0,A.kt)("pre",null,(0,A.kt)("code",{parentName:"pre",className:"language-console"},"pip install --user cookiecutter\n")),(0,A.kt)("p",null,"Alguns sistemas bloqueiam a instala\xe7\xe3o de pacotes de terceiros.\nA op\xe7\xe3o ",(0,A.kt)("inlineCode",{parentName:"p"},"--user")," informa o Python que o pacote deve ser instalado\nsomente para o seu usu\xe1rio. Esse tipo de bloqueio ocorre com bastante\nfrequ\xeancia no Windows."),(0,A.kt)("p",null,"Ap\xf3s a instala\xe7\xe3o do ",(0,A.kt)("a",{parentName:"p",href:"https://cookiecutter.readthedocs.io/en/latest/"},"cookiecutter"),", execute\no seguinte comando:"),(0,A.kt)("pre",null,(0,A.kt)("code",{parentName:"pre",className:"language-console"},"$ cookiecutter gh:ingwersen-erik/cookiepy\n")),(0,A.kt)("h2",{id:"exemplo-docookiepy-em-a\xe7\xe3o"},"Exemplo do",(0,A.kt)("inlineCode",{parentName:"h2"},"cookiepy")," em a\xe7\xe3o"),(0,A.kt)("p",null,(0,A.kt)("img",{src:a(1974).Z,width:"640",height:"480"})),(0,A.kt)("h2",{id:"funcionalidades"},"Funcionalidades"),(0,A.kt)("p",null,"Este template possui as seguintes funcionalidades, que s\xe3o\nautomaticamente inclusas:"),(0,A.kt)("ul",null,(0,A.kt)("li",{parentName:"ul"},"Gerenciamento e empacotamento de pacotes usando\n",(0,A.kt)("a",{parentName:"li",href:"https://python-poetry.org/"},"Poetry")),(0,A.kt)("li",{parentName:"ul"},"Automatiza\xe7\xe3o de testes usando ",(0,A.kt)("a",{parentName:"li",href:"https://nox.thea.codes/"},"Nox")),(0,A.kt)("li",{parentName:"ul"},"Avalia\xe7\xe3o de qualidade de c\xf3digo durante a etapa de\n",(0,A.kt)("a",{parentName:"li",href:"https://pre-commit.com/"},"pre-commit"),", usando\n",(0,A.kt)("a",{parentName:"li",href:"http://flake8.pycqa.org"},"Flake8")),(0,A.kt)("li",{parentName:"ul"},"Integra\xe7\xe3o cont\xednua atrav\xe9s do uso de ",(0,A.kt)("a",{parentName:"li",href:"https://github.com/features/actions"},"GitHub\nActions")),(0,A.kt)("li",{parentName:"ul"},"Documenta\xe7\xe3o de c\xf3digo usando ",(0,A.kt)("a",{parentName:"li",href:"http://www.sphinx-doc.org/"},"Sphinx"),",\n",(0,A.kt)("a",{parentName:"li",href:"https://myst-parser.readthedocs.io/"},"MyST"),", e ",(0,A.kt)("a",{parentName:"li",href:"https://readthedocs.org/"},"Read the\nDocs")),(0,A.kt)("li",{parentName:"ul"},"Gera\xe7\xe3o automatizada de resumo das altera\xe7\xf5es e novas implementa\xe7\xf5es\nda release com ",(0,A.kt)("a",{parentName:"li",href:"https://github.com/release-drafter/release-drafter"},"Release\nDrafter")),(0,A.kt)("li",{parentName:"ul"},"Atualiza\xe7\xe3o automatizada de depend\xeancias com\n",(0,A.kt)("a",{parentName:"li",href:"https://dependabot.com/"},"Dependabot")),(0,A.kt)("li",{parentName:"ul"},"Formata\xe7\xe3o do c\xf3digo usando ",(0,A.kt)("a",{parentName:"li",href:"https://github.com/psf/black"},"Black")," e\n",(0,A.kt)("a",{parentName:"li",href:"https://prettier.io/"},"Prettier")),(0,A.kt)("li",{parentName:"ul"},"Ordena\xe7\xe3o dos imports do pacote com\n",(0,A.kt)("a",{parentName:"li",href:"https://pycqa.github.io/isort/"},"isort")),(0,A.kt)("li",{parentName:"ul"},"Framework de testes unit\xe1rios\n",(0,A.kt)("a",{parentName:"li",href:"https://docs.pytest.org/en/latest/"},"pytest")),(0,A.kt)("li",{parentName:"ul"},"Gera\xe7\xe3o de relat\xf3rios de coverage com ",(0,A.kt)("a",{parentName:"li",href:"https://codecov.io/"},"Codecov")),(0,A.kt)("li",{parentName:"ul"},"An\xe1lise est\xe1tica de c\xf3digo com ",(0,A.kt)("a",{parentName:"li",href:"http://mypy-lang.org/"},"mypy")),(0,A.kt)("li",{parentName:"ul"},"Type-checking durante a execu\xe7\xe3o com\n",(0,A.kt)("a",{parentName:"li",href:"https://github.com/agronholm/typeguard"},"Typeguard")),(0,A.kt)("li",{parentName:"ul"},"Atualiza\xe7\xe3o automatizada de sintaxe com\n",(0,A.kt)("a",{parentName:"li",href:"https://github.com/asottile/pyupgrade"},"pyupgrade")),(0,A.kt)("li",{parentName:"ul"},"An\xe1lise de seguran\xe7a com ",(0,A.kt)("a",{parentName:"li",href:"https://github.com/PyCQA/bandit"},"Bandit")," e\n",(0,A.kt)("a",{parentName:"li",href:"https://github.com/pyupio/safety"},"Safety")),(0,A.kt)("li",{parentName:"ul"},"Verifica\xe7\xe3o dos exemplos da documenta\xe7\xe3o com\n",(0,A.kt)("a",{parentName:"li",href:"https://github.com/Erotemic/xdoctest"},"xdoctest")),(0,A.kt)("li",{parentName:"ul"},"Gerenciamento de labels de reposit\xf3rio com ",(0,A.kt)("a",{parentName:"li",href:"https://github.com/marketplace/actions/github-labeler"},"GitHub\nLabeler"))),(0,A.kt)("p",null,(0,A.kt)("strong",{parentName:"p"},"Vers\xf5es Python suportadas:")," Python 3.7, 3.8, 3.9, e 3.10."),(0,A.kt)("h2",{id:"estrutura-do-reposit\xf3rio"},"Estrutura do reposit\xf3rio"),(0,A.kt)("pre",null,(0,A.kt)("code",{parentName:"pre",className:"language-text"},"cookiepy\n\u251c\u2500\u2500 CODE_OF_CONDUCT.rst             <- C\xf3digo de conduta (copiado de outros templates).\n\u251c\u2500\u2500 CONTRIBUTING.rst                <- Guia de contribui\xe7\xe3o. Est\xe1 em ingl\xeas.\n\u251c\u2500\u2500 LICENSE.rst                     <- Licen\xe7a do projeto (por enquanto est\xe1 como MIT)\n\u251c\u2500\u2500 README.rst                      <- Este arquivo que voc\xea est\xe1 lendo.\n\u251c\u2500\u2500 cookiecutter.json               <- Instru\xe7\xf5es para a gera\xe7\xe3o do template.\n\u251c\u2500\u2500 docs                            <- Diret\xf3rio com arquivos da documenta\xe7\xe3o.\n\u251c\u2500\u2500 hooks                           <- Diret\xf3rio cont\xeam os hooks pr\xe9 e p\xf3s execu\xe7\xe3o do comando cookiecutter.\n\u251c\u2500\u2500 noxfile.py                      <- Arquivo nox\n\u251c\u2500\u2500 poetry.lock                     <- Depend\xeancias do projeto.\n\u251c\u2500\u2500 pycharm.sh                      <- Arquivo para inicializar o PyCharm.\n\u251c\u2500\u2500 pyproject.toml                  <- Configura\xe7\xf5es do projeto.\n\u251c\u2500\u2500 tools                           <- ferramentas extras para o desenvolvimento do cookiepy.\n\u2514\u2500\u2500 {{cookiecutter.project_name}}   <- Template do pacote que ser\xe1 criado.\n")),(0,A.kt)("h1",{id:"to-do"},"TO-DO"),(0,A.kt)("ul",{className:"contains-task-list"},(0,A.kt)("li",{parentName:"ul",className:"task-list-item"},(0,A.kt)("input",{parentName:"li",type:"checkbox",checked:!1,disabled:!0})," ","Traduzir o template para portugu\xeas. A minha inten\xe7\xe3o inicial\nera criar o cookiecutter em ingl\xeas, por uma facilidade minha em\nescrever em ingl\xeas e tamb\xe9m porque a maioria dos projetos requrem\nc\xf3digo escrito em ingl\xeas."),(0,A.kt)("li",{parentName:"ul",className:"task-list-item"},(0,A.kt)("input",{parentName:"li",type:"checkbox",checked:!1,disabled:!0})," ","Melhorar tutoriais de como usar."),(0,A.kt)("li",{parentName:"ul",className:"task-list-item"},(0,A.kt)("input",{parentName:"li",type:"checkbox",checked:!1,disabled:!0})," ","Criar tutoriais, explicando a functionalidade de cada ferramenta.")))}l.isMDXComponent=!0},3870:(e,t,a)=>{a.d(t,{Z:()=>o});const o="data:image/gif;base64,R0lGODlhzADvAPcAAGJiaf/6w1FRWv/rK//yc//qI9XV1//uSpGRll1dZf/wZP/vU/Ly8//4tP/83P/zg//rMtLS1NjY2v/oEszMziQkL//1k1paYrq6vf/2otDQ0v/lAKamqtra3M7O0dzc3mlpcPb29sbGyURETf/xa//3qv/zfDQ0Pm5udTIyPP/nCf/tRKyssP/+9HZ2fP/+8Y+PlIiIjv/2nP/0jP//+MLCxWZmbv///8jIyh0dKJKSmMrKzN7e4KmprYSEinx8gv/6yzw8Ro2Nk4aGjBoaJdbW2P/sOTAwOqSkqOXl5rCwtP/pGbe3uoKCiP/94VdXX/Dw8f/96qqqrv/+7bW1uP/oDv/nBPT09u7u7yAgK3p6gKCgpExMVf/70f/95v/5ucTEx//5vnJyef/mAq6usufn6H5+hP/vWVRUXLOztv/sPjg4QoqKkHR0e/Hx8v/71D8/SOnp6pmZnurq6yEhLJWVmk5OVr29wJ6eozc3QJeXnL+/wpycoUpKU0hIUf///EFBSpiYnO3t7v/pHCIiLm9vdp2doi4uOKKipv/6xzs7RHh4fv/4r0NDTCgoNCUlMP/wXoCAhkZGTxYWIf/mABMTHysrNSwsNi0tNyoqNCIiLJaWm5qan+vr7CkpMyIiLSgoMjo6QycnMS8vOSMjLigoMyYmMCcnMvPz9CYmMf39/eDg4pqanklJUkBASfn5+isrNktLVObm5y0tOPT09fr6+yoqNfn5+WhobywsN/7+/nFxeOPj5OPj5fX19vv7++Hh48fHyfz8/E9PWOzs7ZOTmcnJzEJCS3Nzevv7/Li4u8DAw/f3+M/P0e/v8E1NVejo6c3Nzzg4Qfj4+Gxsc7y8v8XFyL6+wcvLza+vs5uboPr6+i4uOfT09OLi5FNTW+Li4+Tk5fj4+aGhpp+fpP7+/y8vOLa2ufz8/V9fZ9nZ29vb3f39/v///v/812Nja6OjqP/7zpubn+Hh4tHR0//mAd/f4d3d37GxtScnMKWlqaurr62tsbOzt9PT1VVVXSH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxMzggNzkuMTU5ODI0LCAyMDE2LzA5LzE0LTAxOjA5OjAxICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxNyAoV2luZG93cykiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6RDJDMkIzMjY1M0VGMTFFODgyRUM5OTU0MUU5NEVENEQiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6RDJDMkIzMjc1M0VGMTFFODgyRUM5OTU0MUU5NEVENEQiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpEMkMyQjMyNDUzRUYxMUU4ODJFQzk5NTQxRTk0RUQ0RCIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDpEMkMyQjMyNTUzRUYxMUU4ODJFQzk5NTQxRTk0RUQ0RCIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PgH//v38+/r5+Pf29fTz8vHw7+7t7Ovq6ejn5uXk4+Lh4N/e3dzb2tnY19bV1NPS0dDPzs3My8rJyMfGxcTDwsHAv769vLu6ubi3trW0s7KxsK+urayrqqmop6alpKOioaCfnp2cm5qZmJeWlZSTkpGQj46NjIuKiYiHhoWEg4KBgH9+fXx7enl4d3Z1dHNycXBvbm1sa2ppaGdmZWRjYmFgX15dXFtaWVhXVlVUU1JRUE9OTUxLSklIR0ZFRENCQUA/Pj08Ozo5ODc2NTQzMjEwLy4tLCsqKSgnJiUk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"},1974:(e,t,a)=>{a.d(t,{Z:()=>o});const o=a.p+"assets/images/demo-acelerador-dda-ecbdeb64d20d8bec538d6e5fafb6c877.gif"}}]);