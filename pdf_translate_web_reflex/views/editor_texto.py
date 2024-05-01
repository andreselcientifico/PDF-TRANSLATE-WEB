import reflex as rx 
from pdf_translate_web_reflex.componentes import Editor_Texto
from pdf_translate_web_reflex.componentes import navbar
from pdf_translate_web_reflex.state import Translate
from ..componentes.react_pdf import react_pdf 

@rx.page("/editor")
def editor() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.box(
            rx.grid(
                rx.hstack(
                    react_pdf(stream=Translate.text),
                    Editor_Texto(Translate.text, rx.EditorButtonList.COMPLEX.value),
                    max_width="80%",
                    margin="auto",
                    padding="1rem",
                )
            )
        )
    )