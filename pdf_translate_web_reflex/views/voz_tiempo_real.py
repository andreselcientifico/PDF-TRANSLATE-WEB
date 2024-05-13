import reflex as rx
from ..componentes import *

@rx.page(title="Traductor de voz", route="/traductor_voz")
def traductor_voz() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.desktop_only(
            rx.chakra.vstack(
                rx.text(
                    "Traductor de voz",
                    align="center",
                ),
                rx.text(
                    "Esta Funcion se pretende agregar Sin el reglamento de Meta, se encuentra en construccion",
                    align="center",
                ),
                rx.text(
                    "Puedes usar cualquier sala :)",
                    align="center",
                ),
            ),
            rx.chakra.box(
                element="iframe",
                src="https://facebook-seamless-streaming.hf.space",
                width="680px",
                height="550px",
                frameborder="0",
            ),
        ),
        rx.tablet_only(
           rx.chakra.vstack(
                rx.chakra.vstack(
                    rx.text(
                        "Traductor de voz",
                        align="center",
                    ),
                    rx.text(
                        "Esta Funcion se pretende agregar Sin el reglamento de Meta, se encuentra en construccion",
                        align="center",
                    ),
                    rx.text(
                        "Puedes usar cualquier sala :)",
                        align="center",
                    ),
                ),
                rx.chakra.box(
                    element="iframe",
                    src="https://facebook-seamless-streaming.hf.space",
                    width="530px",
                    height="530px",
                    frameborder="0",
                ),
           )
        ),
        rx.mobile_only(
            rx.chakra.vstack(
                rx.text(
                    "Traductor de voz",
                    align="center",
                ),
                rx.text(
                    "Esta Funcion se pretende agregar Sin el reglamento de Meta, se encuentra en construccion",
                    align="center",
                ),
                rx.text(
                    "Puedes usar cualquier sala :)",
                    align="center",
                ),
            ),
            rx.chakra.box(
                element="iframe",
                src="https://facebook-seamless-streaming.hf.space",
                width="380px",
                height="350px",
                frameborder="0",
            ),
        ),
    )