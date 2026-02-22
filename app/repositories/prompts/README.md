# app/repositories/prompts

Repositorio de prompts usados para construir o documento de escopo.

## Responsabilidades

- Definir instrucoes de cada secao do escopo.
- Garantir consistencia de formato entre respostas geradas.
- Controlar a etapa de normalizacao final para exportacao Word.

## Arquivos

- `(1) Prompt_visao-geral.txt`: secao de visao geral do produto.
- `(2) Prompt_requisitos-funcionais.txt`: requisitos funcionais (RF).
- `(3) Prompt_telas-escopos.txt`: escopo de UI/UX.
- `(4) Prompt_requisitos-nao-funcionais.txt`: requisitos nao funcionais (RNF).
- `(5) Prompt_regra-negocio.txt`: regras de negocio (RB).
- `(6) Prompt_integracoes-comp-tecnico.txt`: integracoes e componentes tecnicos.
- `_prompt_normalizacao_word.txt`: normalizacao de texto consolidado para documento Word.

## Observacao

Os prompts numerados sao executados em ordem para permitir dependencias entre secoes.
