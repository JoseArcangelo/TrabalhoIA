# 🌍 Tradutor Inteligente com IA

📘 Projeto da disciplina de Inteligência Artificial - AMF

Este projeto foi desenvolvido como parte da disciplina de **Inteligência Artificial** do curso de **Sistemas de Informação da Faculdade Antonio Meneghetti (AMF)**. O objetivo é demonstrar a aplicação prática de **Inteligência Artificial** no cotidiano, criando uma solução que realiza **traduções automáticas** a partir de diferentes formatos de entrada, como texto, arquivos, áudio e imagens.

A aplicação utiliza a **API Gemini** da Google para tradução inteligente de conteúdo, além de integrar outras tecnologias, como o **Whisper** da OpenAI (para transcrição de áudio) e o **Pytesseract** (para extração de texto de imagens).

---

## 📚 Funcionalidades

- 🔤 Tradução de texto digitado manualmente  
- 📄 Tradução de arquivos `.txt`  
- 🖼️ Extração de texto de imagens e tradução  
- 🔊 Transcrição de áudio e tradução do conteúdo  

---

## 🧠 Tecnologias e Inteligência Artificial Utilizadas

- **Gemini (Google Generative AI):** utilizado para gerar traduções inteligentes em linguagem natural.
- **Whisper (OpenAI):** realiza a transcrição de áudio em texto.
- **Pytesseract (OCR):** extrai texto de imagens.

---

## 🔧 Instalação das Dependências

### 📦 Bibliotecas Python

```bash
pip install google-generativeai
pip install openai-whisper
pip install pytesseract
````
Além disso, o projeto requer o FFmpeg para manipulação de arquivos de áudio.
https://ffmpeg.org/
