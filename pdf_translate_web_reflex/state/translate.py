import reflex as rx
import pathlib
import os
import time
from bs4 import BeautifulSoup
import re
import requests
import nltk
import fitz
from io import BytesIO

class Translate(rx.State):
    
    text: str
    content_text: str = ""
    error_message: str

    # Función para dividir el corpus en trozos de oraciones con un máximo de 400 tokens por trozo
    @rx.background
    async def dividir_corpus_en_oraciones_maximo_tokens(self, corpus, max_tokens):
        oraciones = nltk.sent_tokenize(corpus)  # Tokenizar el corpus en oraciones
        divisiones = []
        trozo_actual = []
        tokens_acumulados = 0
        for oracion in oraciones:
            tokens_oracion = nltk.word_tokenize(oracion)
            if tokens_acumulados + len(tokens_oracion) <= max_tokens:
                oracion = re.sub(r'[^a-zA-Z0-9\s]', '', oracion) 
                oracion = oracion.replace("\n", " ").replace("\r", "") . replace("\t", "").replace("\\", "")
                trozo_actual.append(oracion)
                tokens_acumulados += len(tokens_oracion)
            else:
                divisiones.append(trozo_actual)
                trozo_actual = [oracion]
                tokens_acumulados = len(tokens_oracion)
        # Añadir el último trozo si no se ha añadido ya
        if trozo_actual:
            divisiones.append(trozo_actual)
        return divisiones
    
    @rx.background
    async def query(self, api_url, headers, payload):
        payload = {
                    "inputs": payload,
                }
        headers = {
            "Authorization": f"Bearer {api_url['Hugginface']}" 
        }
        return await requests.post(api_url, headers=headers, json=payload).json()

    async def extract_text_from_pdf(self, file: list[rx.UploadFile]):
        for f in file:
            try:
                if f.filename.endswith('.pdf'):
                    pdf_reader = fitz.open(stream=BytesIO(await f.read()))
                    for page_num in range(pdf_reader.page_count):
                        self.text += pdf_reader.load_page(page_num).get_text()
                elif f.filename.endswith('.html') or f.filename.endswith('.htm'):
                    html_data = await f.read()
                    soup = BeautifulSoup(html_data.decode('utf-8'), 'html.parser')
                    self.text = soup.get_text()
                elif f.filename.endswith('.txt'):
                    text_data = await f.read()
                    self.text = text_data.decode('utf-8')
            except Exception as e:
                self.error_message = str(e)
        return rx.redirect("/editor")
    
    @rx.background
    async def get_texto(self, url_hug: dict = {}, api_hub = ""):
        if api_hub == "":
            yield rx.window_alert("Debe ingresar una API")
        if url_hug == {}:
            yield rx.window_alert("Debe Seleccionar una URL")
        else:
            text = await self.dividir_corpus_en_oraciones_maximo_tokens(self.text, 400)
            self.text = ""
            # Imprimir las divisiones
            max_intentos = 3  # Número máximo de intentos
            for trozo in text:
                for oracion in trozo:
                    intento = 0
                    while intento < max_intentos:
                        try:
                            print(api_hub)
                            output = self.query(url_hug, api_hub, oracion)
                            self.text += output[0]['translation_text']
                            break  # Salimos del bucle while si no se produce ningún error
                        except Exception as e:
                            intento += 1
                            if intento == max_intentos:
                                self.error_message = str(e)
                                yield rx.window_alert(f"Error después de {max_intentos} intentos Error: {e}")
                                exit()  # Detenemos el programa si el error persiste después de tres intentos
                            else:
                                time.sleep(1)

    def text_editor(self, content: str):
        self.content_editor = content
    
    def message_error(self):
        return self.error_message    
    
    def set_text(self, new_text: str):
        self.text += "\n" + new_text