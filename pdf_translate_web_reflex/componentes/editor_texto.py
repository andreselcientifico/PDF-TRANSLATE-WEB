import reflex as rx

def Editor_Texto(contenido: str, funciones,opciones) -> rx.Component:
    return rx.flex(
        rx.box(
            rx.editor(
                lang='es',
                set_contents=contenido,
                on_change=funciones,
                set_options=rx.EditorOptions(button_list=opciones),
                set_all_plugins=True,
                width='700px !important',
                height='300px !important',
            ),
            padding='1em',
            border_radius='1em',
            border = "2px solid var(--mauve-3)",
        ),
    )