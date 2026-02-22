# app/core

Camada central com contratos compartilhados pelo projeto.

## Responsabilidades

- Consolidar constantes globais da aplicacao.
- Definir hierarquia de excecoes de dominio.
- Reduzir acoplamento entre servicos por meio de contratos estaveis.

## Arquivos

- `constants.py`: modelos padrao, variaveis de ambiente e caminhos principais.
- `exceptions.py`: excecoes customizadas para configuracao, audio e geracao de escopo.
- `__init__.py`: reexporta constantes e excecoes para imports mais simples.
