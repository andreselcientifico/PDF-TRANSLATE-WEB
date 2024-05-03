import reflex as rx
import pathlib
import os
from bs4 import BeautifulSoup
import fitz
from io import BytesIO

class Translate(rx.State):
    
    text: str
    error_message: str

    async def extract_text_from_pdf(self, file: list[rx.UploadFile]):
        for f in file:
            try:
                if f.filename.endswith('.pdf'):
                    pdf_reader = fitz.open(stream=BytesIO(await f.read()))
                    for page_num in range(pdf_reader.page_count):
                        self.text += pdf_reader.load_page(page_num).get_text()
                elif f.filename.endswith('.html') or f.filename.endswith('.htm'):
                    html_data = await f.read()
                    soup = BeautifulSoup(html_data.decode('utf-8'), 'html.parser')
                    self.text = soup.get_text()
                elif f.filename.endswith('.txt'):
                    text_data = await f.read()
                    self.text = text_data.decode('utf-8')
            except Exception as e:
                self.error_message = str(e)
        return rx.redirect("/editor")
    
    def message_error(self):
        return self.error_message    
    
    def set_text(self, new_text: str):
        self.text += "\n" + new_text