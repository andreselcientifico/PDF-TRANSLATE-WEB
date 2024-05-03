import reflex as rx
import reflex_google_auth

from .entry import *
from ..styles import *
from ..state import State
from ..models import Entry,Author


def menu_state() ->rx.Component:
    return rx.cond(
                    reflex_google_auth.GoogleAuthState.token_is_valid
                    & State.user_info.enabled,
                    avatar(),
                    rx.flex(
                        auth_error_callout(),
                        rx.spacer(),
                        google_auth_button(),
                        on_click=State.set_form_error(""),
                    ),
                )


def navbar() ->rx.Component:
    return rx.hstack(
        rx.box(
            rx.chakra.hstack(
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
                rx.button(
                    "Traductor",
                    on_click=rx.redirect("/translate"),
                    color=Color.PRIMARY.value, 
                    bg="white", 
                    border=f"1px solid {Color.SECONDARY.value}",
                    cursor = 'pointer',
                    margin_top = "1rem",
                ),
                rx.button(
                        "Traducir Audio Tiempo Real",
                        color=Color.PRIMARY.value, 
                        bg="white", 
                        border=f"1px solid {Color.SECONDARY.value}",
                        cursor = 'pointer',
                        margin_top = "1rem",

                ),
                gap = "inherit",
                on_click=rx.redirect("/"),
                cursor="pointer",
            ),
            
        ),
        rx.spacer(),
        rx.input(placeholder="Search here...", max_length="30"),
        menu_state(),
        position="sticky",
        top="0px",
        padding="1em",
        height="4em",
        width="100%",
        z_index="999",
    )
