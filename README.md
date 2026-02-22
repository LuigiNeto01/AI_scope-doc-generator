# POC IA Document

Aplicacao para transformar uma reuniao gravada em um documento tecnico de escopo.

## Objetivo

Automatizar o fluxo de descoberta de requisitos a partir de audio/video, com geracao estruturada de texto e exportacao para Word.

## Fluxo Funcional

1. Extracao de audio do video de entrada.
2. Transcricao do audio com modelo de speech-to-text.
3. Geracao das secoes de escopo com prompts especializados.
4. Normalizacao final do texto consolidado para layout de documento.
5. Geracao dos artefatos finais (`.txt` normalizado + `.docx`).
6. Arquivamento da execucao em pasta `processada_DD-MM-AAAA_HH-MM-SS`.

## Arquitetura (Resumo)

- `main.py`: ponto de entrada com tratamento de erro padronizado.
- `app/pipeline/`: orquestracao de alto nivel da pipeline.
- `app/services/`: regras de dominio (audio, IA, escopo, arquivamento).
- `app/repositories/`: artefatos est?ticos (prompts e template Word).
- `app/core/`: constantes e excecoes de dominio.
- `app/config/`: paths e convencoes de organizacao de arquivos.
- `scripts/`: utilitarios para reprocessar escopo sem rerodar pipeline completa.

## Requisitos

- Python 3.10+
- Dependencias listadas em `requirements.txt`
- `OPENAI_API_KEY` configurada em `.env`
- `ffmpeg` disponivel no PATH (ou fallback com `imageio-ffmpeg`)

## Configuracao

1. Instale as dependencias:

```bash
pip install -r requirements.txt
```

2. Crie o arquivo `.env`:

```env
OPENAI_API_KEY=seu_token_aqui
```

## Execucao

Pipeline completa:

```bash
python main.py
```

## Scripts de Apoio

Gerar DOCX usando secoes `.txt` ja existentes:

```bash
python scripts/gerar_docx_escopo.py
```

Teste de normalizacao final com saida TXT + DOCX (sem gerar secoes novamente):

```bash
python scripts/teste_normalizacao_existentes.py
```

## Convencoes Importantes

- A pasta `data/` esta ignorada no Git para evitar versionamento de artefatos de execucao.
- Erros de dominio usam excecoes customizadas em `app/core/exceptions.py`.
- Paths e nomes padrao ficam centralizados em `app/config/paths.py`.
