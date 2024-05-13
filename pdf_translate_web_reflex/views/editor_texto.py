import reflex as rx 
import re
import requests
import nltk
import time
import fitz
import os

from io import BytesIO
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from ..componentes import *
from ..styles import *
from nltk.tokenize import sent_tokenize, word_tokenize
from deep_translator import GoogleTranslator
import google.generativeai as genai


nltk.download('punkt')
url_data = ["español", "ingles"] 
type_data = ["Traductor de google (recomendado) ", "IA (Lento) "]
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
generation_config = {
  "temperature": 0.5,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

class AI_SELECT(rx.State):
    text: str = ""
    idioma: str = url_data[0]
    type: str = type_data[0]
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
        # Tokenizador específico para HTML
        tokenizer = RegexpTokenizer('<[^>]+>|[\w]+')
        
        # Convertir el HTML en texto plano y tokenizar
        corpus_tokens = tokenizer.tokenize(corpus)
        
        # Inicializar la lista de párrafos y variables de conteo
        parrafos = []
        tokens_actuales = 0
        parrafo_actual = ""
        
        # Iterar sobre cada token
        for token in corpus_tokens:
            # Si el token es una etiqueta HTML, lo agregamos directamente al párrafo actual
            if token.startswith('<') and token.endswith('>'):
                parrafo_actual += token + " "
            else:
                # Si el token es texto, lo agregamos al párrafo actual y contamos los tokens
                parrafo_actual += token + " "
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

    @rx.background
    async def get_texto(self):
        if self.type == type_data[0]:
            async with self:
                self.content_data  += self.content
                self.text = ""
            text = await self.dividir_corpus_en_oraciones_maximo_tokens(self.content, 300)
            max_intentos = 3  # Número máximo de intentos
            for parrafo in text:
                intento = 0
                while intento < max_intentos:
                    try:
                        async with self:
                            self.processing = True
                        if self.idioma == url_data[0]:
                            output = GoogleTranslator(target='es').translate(parrafo)
                        else:
                            output = GoogleTranslator().translate(parrafo)
                        async with self:
                            self.text += " " + output
                        break  # Salimos del bucle while si no se produce ningún error
                    except Exception as e:
                        intento += 1
                        if intento == max_intentos:
                            async with self:
                                self.processing = False
                                self.error_message = str(e)
                            yield rx.window_alert(f"Error después de {max_intentos} intentos ('Error'): {e}")
                            break # Detenemos el programa si el error persiste después de tres intentos
                        else:
                            print(e)
                            time.sleep(2)
                if intento == max_intentos:
                        break
            async with self:
                self.text +=  f"""\n
                    ----------------------------------------------------------------------------------------------------------------------------
                    {self.content_data}
                    """  
                self.content_data = ""
                self.content = ""
                self.processing = False 
        else:
            async with self:
                self.content_data  += self.content
                self.text = ""
            text = await self.dividir_corpus_en_oraciones_maximo_tokens(self.content, 300)
            max_intentos = 3  # Número máximo de intentos
            for parrafo in text:
                intento = 0
                while intento < max_intentos:
                    try:
                        async with self:
                            self.processing = True
                        system =  f"You are a Google html translator. You have to translate from Auto to {self.idioma}. If the language is Auto, you must detect the language. Simply translate the text, don't worry about the context, you must return the text in html with the same format that was passed to you."
                        prompt = system + parrafo
                        prompt_parts = [
                                        prompt
                                    ]
                        output = model.generate_content(prompt_parts)
                        print(output.text)
                        async with self:
                            self.text += " " + output.text
                        break  # Salimos del bucle while si no se produce ningún error
                    except Exception as e:
                        intento += 1
                        if intento == max_intentos:
                            async with self:
                                self.processing = False
                                self.error_message = str(e)
                            yield rx.window_alert(f"Error después de {max_intentos} intentos ('Error'): {e}")
                            break # Detenemos el programa si el error persiste después de tres intentos
                        else:
                            time.sleep(2)
                if intento == max_intentos:
                    break
            async with self:
                self.text +=  f"""\n
                    ----------------------------------------------------------------------------------------------------------------------------
                    {self.content_data}
                    """  
                self.content_data = ""
                self.content = ""
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
        on_change=AI_SELECT.set_idioma,
    )

@rx.page("/editor")
def editor() -> rx.Component:
    return rx.chakra.vstack(
        rx.desktop_only(
            rx.chakra.vstack(
                navbar(),
                Editor_Texto(
                    AI_SELECT.text, AI_SELECT.text_editor, 
                    rx.EditorButtonList.COMPLEX.value,
                    width = '1080px !important',
                    height = "55vh"
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
                    rx.hstack(
                        rx.hstack(
                            rx.el.h2("Metodo:"),
                        ),
                        rx.select(
                            type_data,
                            size="3",
                            variant="classic",
                            radius="large",
                            default_value=type_data[0],
                            on_change=AI_SELECT.set_type,
                        ),
                        rx.hstack(
                            rx.el.h2("Idioma al que se traducira:"),
                        ),
                        options(),
                        rx.button(
                            'Traducir todo el texto', 
                            on_click=AI_SELECT.get_texto,
                            color=Color.PRIMARY.value, 
                            bg="white", 
                            border=f"1px solid {Color.SECONDARY.value}",
                            cursor = 'pointer',
                        ),
                        align="center"
                    ),
                ),
            ),
            width = "100%"
        ),
        rx.tablet_only(
            rx.chakra.vstack(
                navbar(),
                Editor_Texto(
                    AI_SELECT.text, AI_SELECT.text_editor, 
                    rx.EditorButtonList.COMPLEX.value,
                    width = '650px !important',
                    height = "55vh"
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
                    rx.hstack(
                        rx.hstack(
                            rx.el.h2("Metodo:"),
                        ),
                        rx.select(
                            type_data,
                            size="3",
                            variant="classic",
                            radius="large",
                            default_value=type_data[0],
                            on_change=AI_SELECT.set_type,
                        ),
                        rx.hstack(
                            rx.el.h2("Idioma al que se traducira:"),
                        ),
                        options(),
                        rx.button(
                            'Traducir todo el texto', 
                            on_click=AI_SELECT.get_texto,
                            color=Color.PRIMARY.value, 
                            bg="white", 
                            border=f"1px solid {Color.SECONDARY.value}",
                            cursor = 'pointer',
                        ),
                        align="center"
                    ),
                ),
            ),
            width = "100%"
        ),
        rx.mobile_only(
            rx.chakra.vstack(
                navbar(),
                Editor_Texto(
                    AI_SELECT.text, AI_SELECT.text_editor, 
                    rx.EditorButtonList.COMPLEX.value,
                    width = '360px !important',
                    height = "35vh"
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
                    rx.hstack(
                        rx.hstack(
                            rx.el.h2("Metodo:"),
                        ),
                        rx.select(
                            type_data,
                            size="3",
                            variant="classic",
                            radius="large",
                            default_value=type_data[0],
                            on_change=AI_SELECT.set_type,
                        ),
                        rx.hstack(
                            rx.el.h2("Idioma al que se traducira:"),
                        ),
                        options(),
                        rx.button(
                            'Traducir todo el texto', 
                            on_click=AI_SELECT.get_texto,
                            color=Color.PRIMARY.value, 
                            bg="white", 
                            border=f"1px solid {Color.SECONDARY.value}",
                            cursor = 'pointer',
                        ),
                        align="center"
                    ),
                ),
            ),
            width = "100%"
        ),
    )