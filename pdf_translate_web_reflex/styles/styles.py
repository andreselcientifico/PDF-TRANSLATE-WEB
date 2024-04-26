from enum import Enum
import reflex as rx

MAX_WIDTH = "550PX"

MARGIN_TOP_BODY = "10rem"

THEME = rx.theme(
        appearance="light", 
        has_background=True, 
        radius="large", 
        accent_color="teal", 
        scaling='110%',
    )

#Fonts
class Font(Enum):
    DEFAULT = "Poppins"
    TITLE = "Poppins"
    LOGO = "Roboto"

class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"

#Colors
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

#Size
class Size(Enum):
    NONE = "0px"
    SMALL = "0.5rem"
    MEDIUM = "0.8rem"
    LARGE = "1.5rem"
    XLARGE = "3rem"
    XXLARGE = "5rem"

#Styles
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