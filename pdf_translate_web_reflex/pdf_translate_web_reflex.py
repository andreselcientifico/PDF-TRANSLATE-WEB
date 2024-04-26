"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .styles.styles import *
from rxconfig import config
from .componentes.navbar import navbar

import reflex as rx


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.container(
            rx.chakra.vstack(
                rx.audio(
                    url='',
                    controls=True,
                    width="100%",
                ),
                rx.button(
                    "Translate",
                    width="100%",
                    height="3rem",
                    margin_top="5rem",
                ),
                margin_top="5rem",
            ),
        ),
        rx.theme_panel(),
    )

app = rx.App(
    theme=rx.theme(
        appearance="light", 
        has_background=True, 
        radius="large", 
        accent_color="teal", 
        scaling='110%',
    ),
    style= BASE_STYLES,
)
app.add_page(index)
