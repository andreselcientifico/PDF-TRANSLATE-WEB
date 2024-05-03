from enum import Enum
import reflex as rx

MAX_WIDTH = "550PX"

MARGIN_TOP_BODY = "10rem ! important"

THEME = rx.theme(
        appearance="light", 
        has_background=True, 
        radius="large", 
        accent_color="teal", 
        scaling='110%',
    )

#Fuentes
class Font(Enum):
    DEFAULT = "Poppins"
    TITLE = "Poppins"
    LOGO = "Roboto"

class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"

#Colores
class Color(Enum):
    PRIMARY = "#14A1F0"
    SECONDARY = "#087ec4"
    BACKGROUND = "#0C151D"
    CONTENT = "#171F26",
    PURPLE = "#9146ff"

class TextColor(Enum):
    HEADER = "#F1F2F4"
    BODY = "#C3C7CB"
    FOOTER = "#A3ABB2"

#tamaños
class Size(Enum):
    NONE = "0px"
    SMALL = "0.5rem"
    MEDIUM = "0.8rem"
    LARGE = "1.5rem"
    XLARGE = "3rem"
    XXLARGE = "5rem"

#estilos
BASE_STYLES = {
    "font_family" : Font.DEFAULT.value,
    "background_color" : Color.BACKGROUND.value, 
    "color" : TextColor.BODY.value,
    "height" : "100vh",
    rx.chakra.button : {
        "color": "white",
        "background_color": "blue",
    }
}