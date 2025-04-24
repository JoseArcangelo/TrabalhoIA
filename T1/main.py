import google.generativeai as genai
import whisper
import lerImagens

API_KEY = ""  
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])


def generate_prompt(prompt):
    idioma = input("Informe para qual idioma deseja traduzir: ")
    return f"Você é um tradutor especializado. Traduza para o idioma {idioma} o texto {prompt}"  # Corrigido

# Traduzindo texto normal
def traduzirTexto(texto):
    response = chat.send_message(generate_prompt(texto), stream=True)
    for s in response:
        if s.text:
            print(s.text, end='', flush=True)

#Traduzindo texto que está em um arquivo
def traduzirArquivo(caminho):
    idioma = input("Informe para qual idioma deseja traduzir: ")

    with open(caminho, 'rb') as arquivo:
        conteudo_arquivo = arquivo.read()

    resposta = model.generate_content(
        contents=[
            {"role": "user", "parts": [
                {"text": f"Você é um tradutor especializado. Traduza esse arquivo para o {idioma}:"},
                {"inline_data": {
                    "mime_type": "text/plain",  
                    "data": conteudo_arquivo
                }}
            ]}
        ]
    )

    print("\n📝 Tradução do arquivo:\n")
    print(resposta.text)

def traduzirAudio(caminho):
    modelo = whisper.load_model("base")
    resposta = modelo.transcribe(caminho)
    
    print(resposta["text"])
    print("\n\nTradução")
    traduzirTexto(resposta["text"])
    print("\nTradução do áudio finalizada!")

def main():
    while True:
        print("\n" + "="*40)
        print("🌍  MENU DE TRADUÇÃO INTELIGENTE  🌍")
        print("="*40)
        print("1️⃣  Copiar e colar o texto")
        print("2️⃣  Ler texto de um arquivo")
        print("3️⃣  Extrair texto de imagem")
        print("4️⃣  Traduzir audio")
        print("5️⃣  🚪 Sair")
        print("="*40)

        opc = input("🔹 Escolha uma opção: ")
        if opc == "1":
            texto = input("Informe o texto: ")
            traduzirTexto(texto)

        elif opc == "2":
            traduzirArquivo(input("Informe o caminho do arquivo: "))
            
        elif opc == "3":
            texto = lerImagens.lerImg(input("Informe o caminho da imagem: "))
            traduzirTexto(texto)
        
        elif opc == "4":
            traduzirAudio(input("Informe o caminho do audio: "))

        elif opc == "5":
            print("Saindo...")
            break

        else:
            print("Opção Inválida!!!")

main()
