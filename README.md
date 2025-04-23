# 🌍 Tradutor Inteligente com IA

Projeto desenvolvido como parte do Trabalho 1 da disciplina de **Inteligência Artificial 2025/02** do curso de **Sistemas de Informação** – Faculdade Antonio Meneghetti (AMF).

## 🎯 Objetivo

Criar uma aplicação prática que integre modelos de Inteligência Artificial para traduzir conteúdos de diferentes mídias: **texto, imagem e áudio**. A solução usa injeção de prompts personalizados e permite interação via linha de comando (CLI).

---

## 🧠 Tecnologias e Modelos Utilizados

| Tipo de Dado | Biblioteca/Modelo | Fonte |
|--------------|-------------------|-------|
| Texto        | Gemini Flash 2.0  | Google Generative AI (via API) |
| Imagem       | `lerImagens.py` com OCR (Tesseract ou similar) | Local |
| Áudio        | Whisper (modelo base) | OpenAI Whisper |

---

## 🔧 Funcionalidades

1. **Tradução de texto digitado**
2. **Tradução de arquivos `.txt`**
3. **Extração de texto de imagens e posterior tradução**
4. **Transcrição e tradução de áudio `.mp3`**

---

## 🧩 Injeção de Prompt

A aplicação adiciona automaticamente contexto ao prompt enviado ao modelo de IA, como:

> "Você é um tradutor especializado. Traduza para o idioma _X_ o texto _Y_"

Esse controle melhora a qualidade da resposta e a adequação ao idioma alvo.

---

## 📋 Requisitos

- Python 3.9+
- API Key da Google AI Studio (Gemini)
- Dependências:

```bash
pip install google-generativeai
pip install openai-whisper
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install pytesseract pillow
