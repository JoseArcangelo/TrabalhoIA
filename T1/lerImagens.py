import pytesseract

#Extraindo o texto de imagens
def lerImg(caminho):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    texto = pytesseract.image_to_string(caminho)

    return texto
