import reflex as rx


def navbar() ->rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(src="/favicon.ico", width="2em"),
            rx.heading("COMMUMIND", font_size="1em"),
        ),
        rx.spacer(),
        rx.input(placeholder="Search here...", max_length="20"),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Menu"),
            ),
            rx.menu.content(
                rx.menu.item("item 1"),
                rx.menu.separator(),
                rx.menu.item("Item 2"),
                rx.menu.item("Item 3"),
                width="10rem",
            ),
        ),
        position="fixed",
        top="0px",
        padding="1em",
        height="4em",
        width="100%",
        z_index="999",
    )
