import reflex as rx
from dotenv import load_dotenv
import os

load_dotenv('.env')

config = rx.Config(
    app_name="pdf_translate_web_reflex",
    db_url=f"postgresql+psycopg://pyrumind:{os.getenv('PASSWORD_DB')}@localhost:5432/dbpyrumind",
)