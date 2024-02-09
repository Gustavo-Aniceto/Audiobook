import pyttsx3
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import warnings

# Suprimir o aviso relacionado ao ignore_ncx
warnings.filterwarnings("ignore", message="In the future version we will turn default option ignore_ncx to True.")

engine = pyttsx3.init()
voices = engine.getProperty('voices')


def extrair_primeira_pagina(epub_path):
    print("Lendo o arquivo EPUB:", epub_path)
    book = epub.read_epub(epub_path)

    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        try:
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            text = soup.get_text().strip()
            if text:  # Verifica se há texto na página
                print("Texto extraído da página:", text)
                engine.say(text)
                engine.runAndWait()
                print("Texto lido em voz alta.")
                break  # Pare após ler a primeira página com texto
            else:
                print("Página não contém texto.")
        except Exception as e:
            print("Erro ao processar a página:", e)


# Exemplo de uso:
epub_path = 'C:\\Users\\guuha\\PycharmProjects\\Audiobook\\smashwords-epub-435be8cd-720e-4480-9ca4-db1481ce70bd.epub'
extrair_primeira_pagina(epub_path)
