import pytesseract

#Extraindo o texto de imagens
def lerImg(caminho):
    # Caminho do executável do Tesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Abre a imagem
    texto = pytesseract.image_to_string(caminho)

    return texto
