# -*- coding: utf-8 -*-
import sys
import pytesseract
from PIL import Image
from io import BytesIO
from localfile import session     

def get_image(url):
    return Image.open(BytesIO(session.get(url).content))

def std_print(s, end="\n"):
    sys.stdout.write("{}{}".format(s, end))

if __name__ == '__main__':
    """Ferramenta para testar a saída bruta do LTCFP.OCR base Tesseract utilizando uma determinada URL de entrada"""

    std_print("""
.##.......########..######..########.########.......#######...######..########.
.##..........##....##....##.##.......##.....##.....##.....##.##....##.##.....##
.##..........##....##.......##.......##.....##.....##.....##.##.......##.....##
.##..........##....##.......######...########......##.....##.##.......########.
.##..........##....##.......##.......##............##.....##.##.......##...##..
.##..........##....##....##.##.......##........###.##.....##.##....##.##....##.
.########....##.....######..##.......##........###..#######...######..##.....##
""")
    std_print("Um Simples OCR ")
    url = input("Informe a URL da imagem que você quer analisar:")
    image = get_image(url)
    std_print("A saída bruta do LTCFP sem processamento é:")
    std_print("-----------------BEGIN-----------------")
    std_print(pytesseract.image_to_string(image).encode('utf-8'))
    std_print("------------------END------------------")
