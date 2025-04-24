# 🌍 Tradutor Inteligente com IA (Trabalho da disciplina de Inteligência Artificial - AMF)

Este projeto foi desenvolvido como parte da disciplina de **Inteligência Artificial** do curso de **Sistemas de Informação da Faculdade Antonio Meneghetti (AMF)**. O objetivo é demonstrar a aplicação prática de IA no cotidiano por meio de uma solução que realiza **traduções automáticas** a partir de diferentes formatos de entrada.

Para isso, o sistema utiliza a **API do Gemini**, uma poderosa ferramenta da Google de geração de conteúdo com IA, além de recursos de reconhecimento de texto e voz.

---

## 📚 Funcionalidades

- 🔤 Tradução de texto digitado manualmente
- 📄 Tradução de arquivos `.txt`
- 🖼️ Extração de texto de imagens e tradução
- 🔊 Transcrição de áudio e tradução do conteúdo

---

## 🧠 Inteligência Artificial utilizada

O projeto usa a **API do Gemini** da Google para gerar traduções de forma inteligente. O modelo entende o contexto e fornece respostas em linguagem natural com alta precisão.

Além disso, também são utilizadas:

- **Whisper** da OpenAI: para transcrição de áudios em texto.
- **Pytesseract**: para extração de texto de imagens via OCR.

---

## 🔧 Bibliotecas necessárias

Execute os comandos abaixo para instalar as bibliotecas utilizadas:

```bash
pip install google-generativeai
pip install openai-whisper
pip install pytesseract

