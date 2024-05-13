import reflex as rx
from dotenv import load_dotenv
import os

load_dotenv('.env')

config = rx.Config(
    app_name="pdf_translate_web_reflex",
    api_url="http://localhost:8000",
    # db_url=f"postgresql+psycopg://pyrumind:{os.getenv('PASSWORD_DB')}@{os.getenv('IP_DB')}:5432/pyrumind",
)