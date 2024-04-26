import reflex as rx
from pdf_translate_web_reflex.componentes.navbar import *
from pdf_translate_web_reflex.styles.styles import *

color = "rgb(107,99,246)"

@rx.page('/translate')
def traductor_pdf() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.upload(
            rx.chakra.vstack(
                rx.button(
                    "Seleccione Archivo", 
                    color=color, 
                    bg="white", 
                    border=f"1px solid {color}",
                    cursor = 'pointer',
                ),
                rx.text(
                    "Arrastre y suelte archivos aquí o haga clic para seleccionar archivos"
                ),
            ),
            id="upload_pdf",
            border=f"1px dotted {color}",
            margin_top = MARGIN_TOP_BODY,
            padding="3em",
            cursor = 'pointer',
        ),
    )