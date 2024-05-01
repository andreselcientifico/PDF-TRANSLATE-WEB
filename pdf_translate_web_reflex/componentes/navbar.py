import reflex as rx
from pdf_translate_web_reflex.styles import *
from pdf_translate_web_reflex.state import Base
from pdf_translate_web_reflex.state import HomeState

def avatar(HomeState) ->rx.Component:
    # username = HomeState.user.username if HomeState.user else None
    # if username:
    #     return rx.menu.root(
    #         rx.menu.trigger(
    #             rx.button('Menu'),
    #             cursor = 'pointer',
    #         ),
    #         rx.menu.content(
    #             rx.menu.item(
    #                 "Traductor PDF",
    #                 on_click=rx.redirect("/translate"),
    #                 cursor = 'pointer',
    #             ),
    #             rx.menu.item(
    #                 "Traducir Audio Tiempo Real",
    #                 cursor = 'pointer',
    #             ),
    #             rx.menu.separator(),
    #             rx.menu.item(
    #                 rx.button(
    #                     "login",
    #                     on_click=rx.redirect("/login"),
    #                     width="100%",
    #                     cursor = 'pointer',
    #                 ),
    #             ),
    #             width="15rem",
    #         ),
    #     )
    # else:
        return rx.menu.root(
            rx.menu.trigger(
                rx.flex(
                    rx.chakra.avatar(name=Base.user.username, size='sm'),  # Avatar
                    rx.text(Base.user.username),  # Texto adicional al lado del avatar
                    align="center",  # Alinea el avatar y el texto verticalmente
                    spacing="2",  # Espacio entre el avatar y el texto
                ),
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
                        "logout",
                        on_click=Base.logout(),
                        width="100%",
                        cursor = 'pointer',
                    ),
                ),
                width="15rem",
            ),
        )


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
        avatar(HomeState),
        position="sticky",
        top="0px",
        padding="1em",
        height="4em",
        width="100%",
        z_index="999",
    )
