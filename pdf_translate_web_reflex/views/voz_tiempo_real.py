import reflex as rx
from ..componentes import *

@rx.page(title="Traductor de voz", route="/traductor_voz")
def traductor_voz() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.chakra.vstack(
            rx.heading(
                "EN CONSTRUCCIÓN",
                size='9'
            ),
            rx.text(
                "Traductor de voz"
            ),
            rx.text(
                "Pronto se agregará esta función. Es cuestión de tiempo que se vea en la página."
            ),
            rx.text(
                "Se agradece el interés."
            ),
            margin_top=MARGIN_TOP_BODY,
        ),
        footer(),
    )