"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .styles import *
from .componentes import *
from .views import *
import reflex as rx

@rx.page('/')
def index() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        body(),
        footer(),
    )

app = rx.App(
    theme=THEME,
    style= BASE_STYLES,
)

app.add_page(index)
app.add_page(traductor_pdf)
app.add_page(editor)
app.add_page(traductor_voz)