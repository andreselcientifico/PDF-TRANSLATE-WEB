import reflex as rx
from pdf_translate_web_reflex.styles import *
import datetime

def footer() -> rx.Component:
    return rx.box(
            rx.tablet_and_desktop(
                    rx.chakra.divider(
                        style={
                                "width": "96%",
                                "margin": "0 auto",
                            }
                ),
                rx.chakra.hstack(
                    rx.chakra.vstack(
                        rx.box(
                            rx.hstack(
                                rx.box(
                                    rx.heading(
                                        'PYRU', 
                                        color_scheme = 'cyan',
                                        font_size = '1rem', 
                                        high_contrast=True,
                                    ),
                                    background_color="var(--accent-4)",
                                    border_radius="0.2rem",
                                ),
                                rx.heading(
                                    'MIND', 
                                    color_scheme='indigo',
                                    font_size = "1rem",
                                    style={
                                        "text_shadow": "1px 1px 2px rgba(255, 255, 255, 0.5)",
                                    }
                                ),
                                font_family=Font.LOGO.value,
                                gap = "inherit",
                            ),
                            on_click=rx.redirect("/"),
                            cursor="pointer",
                        ),
                        rx.chakra.link(
                                f'© 2024-{datetime.date.today().year}',
                                href= '/#',
                                font_size = Size.MEDIUM.value,
                        ),
                        rx.text(
                                'This website is made with ❤️ and ☕ by Andres Perez.', 
                                font_size = Size.MEDIUM.value,
                                margin_top = Size.NONE.value,
                        ),
                        align_items="start"
                    ),
                    rx.spacer(
                        direction="column",
                        spacing="2",
                    ),
                    links(
                        margin_right = Size.XLARGE.value + "!important",
                    ),
                    color = TextColor.FOOTER.value,
                    padding = Size.XLARGE.value,
                ),
            ),
            rx.mobile_only(
                rx.chakra.divider(
                    style={
                            "width": "96%",
                            "margin": "0 auto",
                        }
                ),
                rx.chakra.hstack(
                    rx.chakra.vstack(
                        rx.box(
                            rx.hstack(
                                rx.box(
                                    rx.heading(
                                        'PYRU', 
                                        color_scheme = 'cyan',
                                        font_size = '1rem', 
                                        high_contrast=True,
                                    ),
                                    background_color="var(--accent-4)",
                                    border_radius="0.2rem",
                                ),
                                rx.heading(
                                    'MIND', 
                                    color_scheme='indigo',
                                    font_size = "1rem",
                                    style={
                                        "text_shadow": "1px 1px 2px rgba(255, 255, 255, 0.5)",
                                    }
                                ),
                                font_family=Font.LOGO.value,
                                gap = "inherit",
                            ),
                            on_click=rx.redirect("/"),
                            cursor="pointer",
                        ),
                        rx.chakra.link(
                                f'© 2024-{datetime.date.today().year}',
                                href= '/#',
                                font_size = Size.MEDIUM.value,
                        ),
                        rx.text(
                                'This website is made with ❤️ and ☕ by Andres Perez.', 
                                font_size = Size.MEDIUM.value,
                                margin_top = Size.NONE.value,
                        ),
                        align_items="start"
                    ),
                    rx.spacer(),
                    links(),
                    padding= Size.MEDIUM.value,
                ),
                height = "11em"
            ),
            style={
                "position": "fixed",
                "bottom": "0",
                "width": "100%",
            }
        )
    

def links(**kwargs)-> rx.Component:
    return rx.vstack(
        rx.heading(
            "Enlaces",
            font_size = Size.MEDIUM.value,
        ),
        rx.chakra.link(
            rx.hstack(
                rx.icon(
                    "github",
                    style={
                        "color" : "white",
                    }
                ),
                "Github",
            ),
            href="https://github.com/andreselcientifico/PDF-TRANSLATE-WEB",
            is_external=True, 
        ),
        rx.chakra.link(
            rx.hstack(
                rx.icon(
                    "library",
                    style={
                        "color" : "white",
                    }
                ),
                "Curso Reflex",
            ),
            href="https://github.com/mouredev/python-web",
            is_external=True, 
        ),
        **kwargs,
    )