<h1 align="center">🤖 AI Scope Doc Generator</h1>
<p align="center">
  Geração automática de documentos de escopo de projeto utilizando Inteligência Artificial.
</p>
<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="python-docx" src="https://img.shields.io/badge/python--docx-✓-2C7FEB?style=for-the-badge"/>
  <img alt="Status" src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
</p>

---

## 📋 Sobre

O **AI Scope Doc Generator** é uma ferramenta Python que automatiza a criação de documentos de escopo de projetos (`.docx`) usando IA. Basta descrever o projeto e a ferramenta gera a documentação estruturada pronta para uso.

## ✨ Funcionalidades

- 📄 Geração automática de documentação `.docx`
- 🧠 Processamento via IA (Gemini / LLM)
- 📁 Suporte a logs e scripts auxiliares
- 🔧 Configuração simples via `.env`

## 🚀 Tecnologias

| Tecnologia | Versão |
|---|---|
| Python | 3.10+ |
| python-docx | ≥ 1.1.2 |
| python-dotenv | ≥ 1.0.1 |
| imageio-ffmpeg | ≥ 0.5.1 |

## 📦 Instalação

```bash
git clone https://github.com/LuigiNeto01/AI_scope-doc-generator.git
cd AI_scope-doc-generator

pip install -r requirements.txt

cp .env.example .env
# Edite o .env com sua API key
```

## 🔧 Uso

```bash
python main.py
```

O documento gerado será salvo na pasta de saída configurada.

## 📁 Estrutura

```
AI_scope-doc-generator/
├── app/            # Lógica principal
├── scripts/        # Scripts auxiliares
├── logs/           # Logs de execução
├── tests/          # Testes
├── main.py         # Ponto de entrada
└── requirements.txt
```

## 📝 Licença

Este projeto está sob licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">Feito com ❤️ por <a href="https://github.com/LuigiNeto01">LuigiNeto01</a></p>
