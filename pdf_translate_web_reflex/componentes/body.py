import reflex as rx
from pdf_translate_web_reflex.styles import *

def body() -> rx.Component:
    return rx.vstack(
    rx.hstack(
        rx.box(
            rx.heading(
                'PYRU', 
                color_scheme='cyan',
                high_contrast=True,
                size='9'
            ),
            align_items="center",
            background_color="var(--accent-2)",
            border_radius="0.5rem",
        ),
        rx.heading(
            'MIND', 
            color_scheme='indigo',
            high_contrast=True,
            size='9'
        ),
        width="100%",
        gap="initial",
    ),
    rx.text(
        "Transforma textos y libros en otros idiomas.",
        size='6',
        margin_top="2rem",
    ),
    rx.text(
        "Conecta la información con la comunidad.",
        size='6',
    ),
    rx.text(
        "Comparte documentos de manera segura.",
        size='6',
    ),
    rx.text(
        "Haz que tu libro sea accesible para todos.",
        size='6',
    ),
    rx.text(
        "Traduce en tiempo real.",
        size='6',
    ),
    max_width=MAX_WIDTH,
    align_items="start",
    margin_top=MARGIN_TOP_BODY,
)