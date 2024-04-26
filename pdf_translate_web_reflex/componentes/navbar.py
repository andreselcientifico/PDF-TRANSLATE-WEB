import reflex as rx
from pdf_translate_web_reflex.styles.styles import *

def navbar() ->rx.Component:
    return rx.hstack(
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
                on_click=rx.redirect("/"),
                cursor="pointer",
            ),
        ),
        rx.spacer(),
        rx.input(placeholder="Search here...", max_length="30"),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Menu"),
                cursor = 'pointer',
            ),
            rx.menu.content(
                rx.menu.item(
                    "Traductor PDF",
                    on_click=rx.redirect("/translate"),
                    cursor = 'pointer',
                ),
                rx.menu.item(
                    "Traducir Audio Tiempo Real",
                    cursor = 'pointer',
                ),
                rx.menu.separator(),
                rx.menu.item(
                    rx.button(
                        "Log in",
                        width="100%",
                        cursor = 'pointer',
                    ),
                ),
                width="15rem",
            ),
        ),
        position="sticky",
        top="0px",
        padding="1em",
        height="4em",
        width="100%",
        z_index="999",
    )
