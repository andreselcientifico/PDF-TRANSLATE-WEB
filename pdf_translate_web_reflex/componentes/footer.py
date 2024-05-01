import reflex as rx
from pdf_translate_web_reflex.styles import *
import datetime

def footer() -> rx.Component:
    return rx.box(
            rx.chakra.vstack(
                rx.chakra.divider(
                    style={"width": "90%"}
                ),
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.heading(
                                'PYRU', 
                                color_scheme = 'cyan',
                                font_size = '1rem', 
                                high_contrast=True,
                            ),
                            background_color="var(--accent-2)",
                            border_radius="0.2rem",
                        ),
                        rx.heading(
                            'MIND', 
                            color_scheme = 'indigo',
                            font_size = '1rem', 
                            high_contrast=True,
                        ),
                        gap = "inherit",
                    ),
                    on_click=rx.redirect("/"),
                    cursor="pointer",
                ),
                rx.link(
                        f'© 2024-{datetime.date.today().year}',
                        href= 'https://moure.dev/',
                        is_external=True,
                        font_size = Size.MEDIUM.value,
                ),
                rx.text(
                        'This website is made with ❤️ and ☕ by Andres Perez.', 
                        font_size = Size.MEDIUM.value,
                        margin_top = Size.NONE.value,
                ),
                bottom = "0px",
                color = TextColor.FOOTER.value,
                margin = Size.SMALL.value,
        ),
        style={
            "position": "fixed",
            "bottom": "0",
            "width": "100%",
            "text_align": "center",
        }
    )
    