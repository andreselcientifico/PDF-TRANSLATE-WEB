import reflex as rx
    

def Editor_Texto(contenido: str, funciones,opciones, **prop) -> rx.Component:
    return rx.flex(
        rx.editor(
            lang='es',
            set_contents=contenido,
            on_change=funciones,
            set_options=rx.EditorOptions(button_list=opciones),
            set_all_plugins=True,
            **prop
        ),
    )