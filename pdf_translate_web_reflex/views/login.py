import reflex as rx
from pdf_translate_web_reflex.state.autenticador import AuthState
from pdf_translate_web_reflex.componentes import navbar

@rx.page('/login')
def login() ->rx.Component:
    return rx.chakra.vstack(
        navbar(),
         rx.box(
            rx.chakra.vstack(
                rx.input(
                    placeholder="Username",
                    on_blur=AuthState.set_username,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                ),
                rx.button("Log in", on_click=AuthState.login, size="3", width="5em"),
                spacing="4",
            ),
            rx.text(
                "Don't have an account yet? ",
                rx.link("Sign up here.", href="/signup"),
                color="gray",
            ),
        align_items="left",
        background="white",
        border="1px solid #eaeaea",
        padding="16px",
        width="400px",
        border_radius="8px",
        ),
    )
