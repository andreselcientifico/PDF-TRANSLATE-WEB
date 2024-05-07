import reflex as rx
import reflex_google_auth

from .entry import *
from ..styles import *
# from ..state import State


# def menu_state() ->rx.Component:
#     return rx.cond(
#                     reflex_google_auth.GoogleAuthState.token_is_valid
#                     & State.user_info.enabled,
#                     avatar(),
#                     rx.flex(
#                         auth_error_callout(),
#                         rx.spacer(),
#                         google_auth_button(),
#                         on_click=State.set_form_error(""),
#                     ),
#                 )

def menu() ->rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.button(
                "Menu",
                background_color="var(--accent-2)",
                color= "indigo",
            ),
        ),
        rx.hover_card.content(
            rx.grid(
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Navegación",
                            size="5",
                            color_scheme="cyan",
                            align="left",
                            margin_bottom = "1.58rem",
                        ),
                        rx.link(
                            rx.hstack(
                                rx.icon("layout-grid"),
                                "Home",
                            ),
                            on_click=rx.redirect("/"),
                            cursor='pointer',
                            margin_top="1rem",
                        ),
                    ),
                ),
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Herramientas de Traducción",
                            size="5",
                            color_scheme="cyan",
                            align="left"
                        ),
                        rx.link(
                            rx.hstack(
                                rx.icon("languages"),
                                "Traductor",
                            ),
                            on_click=rx.redirect("/traductor_texto"),
                            cursor='pointer',
                            margin_top="1rem",
                        ),
                        rx.link(
                            rx.hstack(
                                rx.icon("audio-lines"),
                                "Traductor de Audio Tiempo Real",
                            ),
                            on_click=rx.redirect("/traductor_voz"),
                            cursor='pointer',
                            margin_top="1rem",
                        ),
                    ),
                ),
                columns="1fr 1fr",  # Aquí se divide en dos columnas de igual tamaño
                gap="0rem",
            ),
            style={"width": 340},
        )
    )


def navbar() ->rx.Component:
    return rx.hstack(
        rx.box(
            rx.chakra.hstack(
                rx.hstack(
                    rx.box(
                        rx.heading(
                            'PYRU', 
                            color_scheme='cyan',
                            font_size='1rem', 
                            high_contrast=True,
                        ),
                        background_color="var(--accent-2)",
                        border_radius="0.2rem",
                    ),
                    rx.heading(
                        'MIND', 
                        color_scheme='indigo',
                        font_size='1rem', 
                        high_contrast=True,
                    ),
                    on_click=rx.redirect("/"),
                    gap="initial",
                    cursor="pointer",
                ),
            ),
        ),
        rx.spacer(),
        menu(),
        # rx.input(placeholder="Buscar aquí...", max_length="30"),
        # menu_state(),
        position="sticky",
        top="0px",
        padding="1em",
        height="4em",
        width="100%",
        z_index="999",
    )