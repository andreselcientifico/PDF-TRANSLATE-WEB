from enum import Enum
import reflex as rx
from ..state import SwitchState1

MAX_WIDTH = "550PX"

MARGIN_TOP_BODY = "7rem ! important"

#Colores
class Color_light(Enum):
        PRIMARY = "#14A1F0"
        SECONDARY = "#087EC4"
        BACKGROUND = "#3B6991"
        CONTENT = "#4D677E"
        PURPLE = "#9146ff"
        
class Color(Enum):
        PRIMARY = "#0A527B"
        SECONDARY = "#03334F"
        BACKGROUND = "#0C151D"
        CONTENT = "#171F26",
        PURPLE = "#4E258A"

THEME = rx.theme(
        appearance="dark",
        has_background=True,
        radius="large", 
        accent_color="sky", 
        scaling='100%',
    )

#Fuentes
class Font(Enum):
    DEFAULT = "Poppins"
    TITLE = "Poppins"
    LOGO = "Roboto"

class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"

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
    "height" : "100vh"
}