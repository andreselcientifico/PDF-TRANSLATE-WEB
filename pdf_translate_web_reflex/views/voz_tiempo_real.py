import reflex as rx
from ..componentes import *

@rx.page(title="Traductor de voz", route="/traductor_voz")
def traductor_voz() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.chakra.vstack(
            rx.text(
                "Traductor de voz"
            ),
            rx.text(
                "Esta Funcion se pretende agregar Sin el reglamento de Meta, se encuentra en construccion"
            ),
            rx.text(
                "Puedes usar cualquier sala :)"
            )
        ),
        rx.chakra.box(
            element="iframe",
            src="https://facebook-seamless-streaming.hf.space",
            width="650px",
            height="550px",
            frameborder="0",
        ),
        footer(),
    )