import reflex as rx

class SwitchState1(rx.State):
    checked: bool = False
    theme: str = "Tema Claro"

    def change_theme(self, checked: bool):
        self.checked = checked
        if self.checked:
            self.theme = "Tema Oscuro"
        else:
            self.theme = "Tema Claro"
    
    def tema(self):
        if self.theme == "Tema Oscuro":
            return False
        else:
            return True

def switch():
    return rx.chakra.vstack(
        rx.chakra.heading(SwitchState1.theme),
        rx.chakra.switch(
            is_checked=SwitchState1.checked,
            on_change=SwitchState1.change_theme,
        ),
    )