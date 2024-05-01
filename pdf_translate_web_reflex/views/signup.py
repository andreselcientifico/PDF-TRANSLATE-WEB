import reflex as rx
from pdf_translate_web_reflex.state import AuthState
from pdf_translate_web_reflex.componentes import navbar


@rx.page('/signup')
def SignUp() -> rx.Component:
    return rx.chakra.vstack(
        navbar(), 
        rx.box(   
            rx.chakra.vstack(
                rx.input(
                    placeholder="User Name",
                    on_blur=AuthState.set_username,
                    size="3",
                ),
                rx.input(
                    placeholder="Full Name",
                    on_blur=AuthState.set_fullname,
                    size="3",
                ),
                rx.input(
                    placeholder="Email",
                    on_blur=AuthState.set_email,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Confirm password",
                    on_blur=AuthState.set_confirm_password,
                    size="3",
                ),
                rx.button(
                    "Sign up",
                    on_click=AuthState.signup,
                    size="3",
                    width="6em",
                ),
                spacing="4",
            ),
            rx.text(
                "Already have an account? ",
                rx.link("Sign in here.", href="/login"),
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