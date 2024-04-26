import reflex as rx

class TextareaState(rx.State):
    text: str = "BIENVENIDO!"

def textarea() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.heading(TextareaState.text, size= '4xl'),
        rx.chakra.text_area(
            value=TextareaState.text,
            on_change=TextareaState.set_text,
        ),
    )