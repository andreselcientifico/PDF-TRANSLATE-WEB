import reflex as rx 
import re
import requests
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import time
import fitz

from io import BytesIO
from bs4 import BeautifulSoup
from ..componentes import *
from ..styles import *

nltk.download('punkt')

url_data = ["Hugginface" ]

class AI_SELECT(rx.State):
    text: str = ""
    api_key: str = ""
    url: str = url_data[0]
    processing: bool = False
    content: str = ""
    content_data: str = ""

    async def extract_text_from_pdf(self, file: list[rx.UploadFile]):
        for f in file:
            try:
                if f.filename.endswith('.pdf'):
                    pdf_reader = fitz.open(stream=BytesIO(await f.read()))
                    for page_num in range(pdf_reader.page_count):
                        self.text += pdf_reader.load_page(page_num).get_text("html")
                        AI_SELECT.text = self.text
                elif f.filename.endswith('.html') or f.filename.endswith('.htm'):
                    html_data = await f.read()
                    soup = BeautifulSoup(html_data.decode('utf-8'), 'html.parser')
                    self.text = soup.get_text()
                    AI_SELECT.text = self.text
                elif f.filename.endswith('.txt'):
                    text_data = await f.read()
                    self.text = text_data.decode('utf-8')
                    AI_SELECT.text = self.text
            except Exception as e:
                self.error_message = str(e)
        return rx.redirect("/editor")
    
    def message_error(self):
        return self.error_message    
    
    def set_text(self, new_text: str):
        self.text += "\n" + new_text

    # Función para dividir el corpus en trozos de oraciones con un máximo de 400 tokens por trozo
    async def dividir_corpus_en_oraciones_maximo_tokens(self, corpus, max_tokens):
        # Dividir el texto en párrafos de aproximadamente 'limite_tokens' de longitud
        corpus = BeautifulSoup(corpus, "html.parser").get_text()
        parrafos = []
        tokens_actuales = 0
        parrafo_actual = ""
        for palabra in re.findall(r'\b\w+\b', corpus):
            # Agregar la palabra al párrafo actual
            parrafo_actual += palabra + " "
            tokens_actuales += 1
            # Si se alcanza el límite de tokens, agregar el párrafo actual a la lista de párrafos y reiniciar
            if tokens_actuales >= max_tokens:
                parrafos.append(parrafo_actual.strip())
                parrafo_actual = ""
                tokens_actuales = 0
        # Agregar el último párrafo si es necesario
        if parrafo_actual:
            parrafos.append(parrafo_actual.strip())
        return parrafos
        
    def query(self, headers, payload):
        output = requests.post(url=self.url, headers=headers, json=payload)
        return output.json()
    
    @rx.background
    async def get_texto(self):
        if self.api_key == "":
            yield rx.window_alert("Debe ingresar una API")
        elif self.url == {}:
            yield rx.window_alert("Debe Seleccionar una URL")
        else:
            async with self:
                self.content_data  += self.content
                self.text = ""
            text = await self.dividir_corpus_en_oraciones_maximo_tokens(self.content, 100)
            max_intentos = 3  # Número máximo de intentos
            for parrafo in text:
                intento = 0
                while intento < max_intentos:
                    try:
                        async with self:
                            self.processing = True
                            if self.url == url_data[0]:
                                self.url = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-es"
                        headers = {"Authorization": f"Bearer {self.api_key}",}
                        payload= { "inputs" : parrafo, }
                        output = self.query(headers, payload)
                        async with self:
                            self.text += " " + output[0]['translation_text']
                        break  # Salimos del bucle while si no se produce ningún error
                    except Exception as e:
                        intento += 1
                        if intento == max_intentos:
                            async with self:
                                self.processing = False
                                self.error_message = str(e)
                            yield rx.window_alert(f"Error después de {max_intentos} intentos ('Error'): {e}, se recomienda Verificar el API")
                            break # Detenemos el programa si el error persiste después de tres intentos
                        else:
                            time.sleep(2)
                if intento == max_intentos:
                        break
            async with self:
                self.text +=  f"""
                                
                
                    Texto anterior:
                    {self.content_data}
                    """  
                self.content_data = ""
                self.processing = False

    def text_editor(self, content: str):
        self.content = content

def options() -> rx.Component:
    return rx.select(
        url_data,
        size="3",
        variant="classic",
        radius="large",
        default_value=url_data[0],
        on_change=AI_SELECT.set_url,
    )

@rx.page("/editor")
def editor() -> rx.Component:
    return rx.chakra.vstack(
        rx.desktop_only(
            rx.chakra.vstack(
                navbar(),
                rx.chakra.vstack(
                    rx.hstack(
                        rx.el.h2("API"),
                    ),
                    rx.hstack(
                        options(),
                        rx.input(
                            placeholder='API Key',
                            max_length=38,
                            type="text",
                            size="3",
                            value=AI_SELECT.api_key,
                            class_name="lg:w-[300px]",
                            on_change=AI_SELECT.set_api_key,
                        ),
                        align="center"
                    ),
                ),
                Editor_Texto(
                    AI_SELECT.text, AI_SELECT.text_editor, 
                    rx.EditorButtonList.COMPLEX.value,
                    width = '1080px !important',
                    height = "57vh"
                ),
                rx.cond(
                    AI_SELECT.processing,
                    rx.chakra.vstack(
                        rx.text('Procesando...'),
                        rx.chakra.spinner(
                            label="Cargando...",
                            color=Color.PRIMARY.value,
                            size="xl",
                        ),
                        rx.text('Por favor espere.., esto puede tardar un poco dependiendo del tamaño del texto'),
                        margin = "1rem",
                        padding = "1rem",
                    ),
                    rx.button(
                            'Traducir todo el texto', 
                            on_click=AI_SELECT.get_texto,
                            color=Color.PRIMARY.value, 
                            bg="white", 
                            border=f"1px solid {Color.SECONDARY.value}",
                            cursor = 'pointer',
                    ),
                ),
            ),
            width = "100%"
        ),
        rx.tablet_only(
            rx.chakra.vstack(
                navbar(),
                rx.chakra.vstack(
                    rx.hstack(
                        rx.el.h2("API"),
                    ),
                    rx.hstack(
                        options(),
                        rx.input(
                            placeholder='API Key',
                            max_length=38,
                            type="text",
                            size="3",
                            value=AI_SELECT.api_key,
                            class_name="lg:w-[300px]",
                            on_change=AI_SELECT.set_api_key,
                        ),
                        align="center"
                    ),
                ),
                Editor_Texto(
                    AI_SELECT.text, AI_SELECT.text_editor, 
                    rx.EditorButtonList.COMPLEX.value,
                    width = '680px !important',
                    height = "60vh"
                ),
                rx.cond(
                    AI_SELECT.processing,
                    rx.chakra.vstack(
                        rx.text('Procesando...'),
                        rx.chakra.spinner(
                            label="Cargando...",
                            color=Color.PRIMARY.value,
                            size="xl",
                        ),
                        rx.text('Por favor espere.., esto puede tardar un poco dependiendo del tamaño del texto'),
                        margin = "1rem",
                        padding = "1rem",
                    ),
                    rx.button(
                            'Traducir todo el texto', 
                            on_click=AI_SELECT.get_texto,
                            color=Color.PRIMARY.value, 
                            bg="white", 
                            border=f"1px solid {Color.SECONDARY.value}",
                            cursor = 'pointer',
                    ),
                ),
            ),
            width = "100%"
        ),
        rx.mobile_only(
            rx.chakra.vstack(
                navbar(),
                rx.chakra.vstack(
                    rx.hstack(
                        rx.el.h2("API"),
                    ),
                    rx.hstack(
                        options(),
                        rx.input(
                            placeholder='API Key',
                            max_length=38,
                            type="text",
                            size="3",
                            value=AI_SELECT.api_key,
                            class_name="lg:w-[300px]",
                            on_change=AI_SELECT.set_api_key,
                        ),
                        align="center"
                    ),
                ),
                Editor_Texto(
                    AI_SELECT.text, AI_SELECT.text_editor, 
                    rx.EditorButtonList.COMPLEX.value,
                    width = '380px !important',
                    height = "45vh"
                ),
                rx.cond(
                    AI_SELECT.processing,
                    rx.chakra.vstack(
                        rx.text('Procesando...'),
                        rx.chakra.spinner(
                            label="Cargando...",
                            color=Color.PRIMARY.value,
                            size="xl",
                        ),
                        rx.text('Por favor espere.., esto puede tardar un poco dependiendo del tamaño del texto'),
                        margin = "1rem",
                        padding = "1rem",
                    ),
                    rx.button(
                            'Traducir todo el texto', 
                            on_click=AI_SELECT.get_texto,
                            color=Color.PRIMARY.value, 
                            bg="white", 
                            border=f"1px solid {Color.SECONDARY.value}",
                            cursor = 'pointer',
                    ),
                ),
            ),
            width = "100%"
        ),
    )