import reflex as rx 
import re
import requests
import nltk
import time
from pdf_translate_web_reflex.componentes import Editor_Texto
from pdf_translate_web_reflex.componentes import navbar
from pdf_translate_web_reflex.state import Translate
from ..componentes.react_pdf import react_pdf 
from ..styles import *

url = { "Hugginface" : 'https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-es'}

class AI_SELECT(rx.State):
    api_key: str = ""
    url: dict = url['Hugginface']
    content: str = ""

    # Función para dividir el corpus en trozos de oraciones con un máximo de 400 tokens por trozo
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
    
    async def query(self, api_url, headers, payload):
        payload = {
                    "inputs": payload,
                }
        headers = {
            "Authorization": f"Bearer {api_url['Hugginface']}" 
        }
        return await requests.post(api_url, headers=headers, json=payload).json()
    
    @rx.background
    async def get_texto(self, url_hug: dict = {}, api_hub = ""):
        if api_hub == "":
            yield rx.window_alert("Debe ingresar una API")
        if url_hug == {}:
            yield rx.window_alert("Debe Seleccionar una URL")
        else:
            text = await self.dividir_corpus_en_oraciones_maximo_tokens(self.content, 400)
            max_intentos = 3  # Número máximo de intentos
            for trozo in text:
                for oracion in trozo:
                    intento = 0
                    while intento < max_intentos:
                        try:
                            output = self.query(url_hug, api_hub, oracion)
                            self.content += output[0]['translation_text']
                            yield rx.window_alert("Traducido :)")
                            break  # Salimos del bucle while si no se produce ningún error
                        except Exception as e:
                            intento += 1
                            if intento == max_intentos:
                                self.error_message = str(e)
                                yield rx.window_alert(f"Error después de {max_intentos} intentos Error: {e}")
                                exit()  # Detenemos el programa si el error persiste después de tres intentos
                            else:
                                time.sleep(1)
                                
    def handler_change(self):
        self.get_texto(self.url, self.api_key)
    
    def text_editor(self, content: str):
        self.content = content

def options() -> rx.Component:
    return rx.select(
        url,
        size="3",
        variant="classic",
        radius="large",
        default_value=url['Hugginface'],
        on_change=AI_SELECT.set_url,
    )

@rx.page("/editor")
def editor() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.flex(
            Editor_Texto(Translate.text, AI_SELECT.text_editor, rx.EditorButtonList.COMPLEX.value),
            react_pdf(
                stream=Translate.text,
                aling='center',
            ),
            direction='row',
            style={
                'justifyContent': 'space-evenly !important'
            },
            padding="1rem",
            width = '100% !important',
        ),
        rx.hstack(
            rx.el.h2("Selecciona",),
            options(),
            rx.el.h2("API_Hugginface",),
            rx.text_area(
                'API Key',
                value=AI_SELECT.api_key,
                on_change=AI_SELECT.set_api_key,
            ),
        ),
        rx.button(
                'Traducir todo el texto', 
                on_click=AI_SELECT.handler_change,
                color=Color.PRIMARY.value, 
                bg="white", 
                border=f"1px solid {Color.SECONDARY.value}",
                cursor = 'pointer',
                margin_top = "1rem",
        ),
        height = '100vh',
    )