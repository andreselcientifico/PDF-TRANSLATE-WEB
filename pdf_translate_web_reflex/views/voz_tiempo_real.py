import reflex as rx
from ..componentes import *

@rx.page(title="Traductor de voz", route="/traductor_voz")
def traductor_voz() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        rx.chakra.vstack(
            rx.heading(
                "EN CONSTRUCCION",
                size='9'
            ),
            rx.text(
                "Traductor de voz"
            ),
            rx.text(
                "Pronto se agregara esta funcion, es cuestion de tiempo que se vea en la pagina."
            )
            ,rx.text(
                "Se agradece el interez"
            ),
            margin_top = MARGIN_TOP_BODY,
        ),
        footer(),
    )