import reflex as rx
from pdf_translate_web_reflex.styles import *

def body() -> rx.Component:
    return rx.vstack(
    rx.tablet_and_desktop(
        rx.logo(),
        rx.hstack(
            rx.box(
                rx.heading(
                    'PYRU', 
                    color_scheme='cyan',
                    high_contrast=True,
                    size='9'
                ),
                align_items="center",
                background_color="var(--accent-4)",
                border_radius="0.5rem",
            ),
            rx.heading(
                'MIND', 
                color_scheme='indigo',
                size='9',
                style={
                    "text_shadow": "1px 1px 2px rgba(255, 255, 255, 0.5)",
                }
            ),
            font_family=Font.LOGO.value,
            border_radius="1rem",
            justify="center",
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
        max_width = MAX_WIDTH,
        margin_top=MARGIN_TOP_BODY,
        align_items="center",
    ),
    rx.mobile_only(
        rx.logo(),
        rx.hstack(
            rx.box(
                rx.heading(
                    'PYRU', 
                    color_scheme='cyan',
                    high_contrast=True,
                    size='9'
                ),
                align_items="center",
                background_color="var(--accent-4)",
                border_radius="0.5rem",
            ),
            rx.heading(
                'MIND', 
                color_scheme='indigo',
                size='9',
                style={
                    "text_shadow": "1px 1px 2px rgba(255, 255, 255, 0.5)",
                }
            ),
            font_family=Font.LOGO.value,
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
        max_width = "306px !important",
        margin_top="-1em !important",
        align_items="start",
    ),
)