import reflex as rx 
from pdf_translate_web_reflex.componentes import Editor_Texto
from pdf_translate_web_reflex.componentes import navbar
from pdf_translate_web_reflex.state import Translate
from ..componentes.react_pdf import react_pdf 
from ..styles import *

url = { "Hugginface" : 'https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-es'}

class AI_SELECT(rx.State):
    api_key: str = ""
    url: dict = url['Hugginface']

    def handler_change(self):
        rx.window_alert("Translating...")
        rx.window_alert('Este proceso puede tardar un poco dependiendo la cantidad de texto, sea paciente')
        Translate.get_texto(self.url, self.api_key),

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
            Editor_Texto(Translate.text, Translate.text_editor, rx.EditorButtonList.COMPLEX.value),
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