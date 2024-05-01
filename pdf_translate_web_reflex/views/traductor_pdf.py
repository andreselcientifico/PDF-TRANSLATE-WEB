import reflex as rx
from pdf_translate_web_reflex.componentes import *
from pdf_translate_web_reflex.state import Translate
from pdf_translate_web_reflex.styles import *

@rx.page('/translate')
def traductor_pdf() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.upload(
            rx.chakra.vstack(
                rx.button(
                    "Seleccione Archivo", 
                    color=Color.PRIMARY.value, 
                    bg="white", 
                    border=f"1px solid {Color.SECONDARY.value}",
                    cursor = 'pointer',
                ),
                rx.text(
                    "Arrastre y suelte archivos aquí o haga clic para seleccionar archivos"
                ),
            ),
            accept = {
                "application/pdf": [".pdf"],
                "text/html": [".html", ".htm"],
                "text/plain": [".txt"],
            },
            max_files=1,
            id="upload_pdf",
            border=f"1px dotted {Color.SECONDARY.value}",
            margin_top = MARGIN_TOP_BODY,
            padding="3em",
            cursor = 'pointer',
        ),
        rx.button(
                    "Subir Archivo", 
                    on_click= Translate.extract_text_from_pdf(rx.upload_files(upload_id="upload_pdf")),
                    color=Color.PRIMARY.value, 
                    bg="white", 
                    border=f"1px solid {Color.SECONDARY.value}",
                    cursor = 'pointer',
                    margin_top = "1rem",
        ),
    )