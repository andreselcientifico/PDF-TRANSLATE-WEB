import reflex as rx 
from pdf_translate_web_reflex.componentes import Editor_Texto
from pdf_translate_web_reflex.componentes import navbar
from pdf_translate_web_reflex.state import Translate
from ..componentes.react_pdf import react_pdf 

@rx.page("/editor")
def editor() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.flex(
            Editor_Texto(Translate.text, Translate.text_editor(), rx.EditorButtonList.COMPLEX.value),
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
        rx.button(
            'Traducir todo el texto', 
        ),
        height = '100vh',
    )