import reflex as rx 
from pdf_translate_web_reflex.componentes import Editor_Texto
from pdf_translate_web_reflex.componentes import navbar
from pdf_translate_web_reflex.state import Translate

@rx.page("/editor")
def editor() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        Editor_Texto(Translate.text, rx.EditorButtonList.COMPLEX.value)
    )