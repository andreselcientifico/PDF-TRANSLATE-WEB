import reflex as rx

def Editor_Texto(contenido: str, opciones) -> rx.Component:
    return rx.chakra.vstack(
        rx.editor(
            set_contents=contenido,
            set_options=rx.EditorOptions(button_list=opciones),
            set_all_plugins=True,
            lib_dependencies = ["template"],
            margin_top="10rem",
        ),
    )