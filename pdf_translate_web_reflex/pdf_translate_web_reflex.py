"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .styles import *
from rxconfig import config
from .componentes import navbar, body, footer
from .views import traductor_pdf, editor
from .state import UserInfoState, State
import reflex as rx

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
app.add_page(traductor_pdf, route='/translate', on_load=State.check_login())
app.add_page(editor, route='/editor', on_load=State.check_login())