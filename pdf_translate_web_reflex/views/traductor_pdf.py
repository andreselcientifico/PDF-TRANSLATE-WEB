import reflex as rx
from pdf_translate_web_reflex.componentes import *
from pdf_translate_web_reflex.styles import *
from .editor_texto import AI_SELECT

@rx.page('/traductor_texto')
def traductor_pdf() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.chakra.vstack(
            rx.heading(
                "¡Bienvenido!",
                size="9",
            ),
            rx.text(
                "¿Necesitas traducir un archivo PDF, HTML o TXT? ¡Estás en el lugar correcto!",
                font_size="lg",
                color="gray.700",
                margin_bottom="1rem",
            ),
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
                padding="3em",
                cursor = 'pointer',
            ),
            rx.button(
                "Subir Archivo", 
                on_click= AI_SELECT.extract_text_from_pdf(rx.upload_files(upload_id="upload_pdf")),
                color=Color.PRIMARY.value, 
                bg="white", 
                border=f"1px solid {Color.SECONDARY.value}",
                cursor = 'pointer',
                margin_top = "1rem",
            ),
            rx.text(
                "Recuerda: El texto traducido estará en formato plano y perderá el formato original del PDF, pero podrás editarlo fácilmente en el editor.",
                margin_top="1rem",
                Color="gray.700",
            ),
            margin_top = MARGIN_TOP_BODY,
        )
    )