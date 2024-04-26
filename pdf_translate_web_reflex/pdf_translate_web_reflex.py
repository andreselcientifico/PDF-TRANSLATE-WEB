"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .styles.styles import *
from rxconfig import config
from .componentes.navbar import navbar
from .componentes.body import body
from .componentes.footer import footer
from .views.traductor_pdf import *

import reflex as rx


class State(rx.State):
    """The app state."""



@rx.page('/')
def index() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        body(),
        footer(),
        rx.theme_panel(default_open=False),
    )

app = rx.App(
    theme=THEME,
    style= BASE_STYLES,
)
app.add_page(index)
app.add_page(traductor_pdf)