from reflex.components.component import NoSSRComponent
from reflex.vars import Var

class react_pdf_lib(NoSSRComponent):
    """componente pdf react"""

    library = 'react-pdf'
    tag = 'pdfjs, Page, Text, View, Document, StyleSheet, Image, PDFViewer, ReactPDF'
    lib_dependencies: list[str] = ['@react-pdf/renderer']

    def _get_custom_code(self) -> str:
        return """
        import 'react-pdf/dist/Page/AnnotationLayer.css';
        import 'react-pdf/dist/Page/TextLayer.css';
        """

class react_pdf(react_pdf_lib):
    """componente pdf react"""

    tag: Var[str] = 'Document'
    page: Var[str] = 'page'
    text: list[str] = 'Text'
    view: list[str] = 'View'
    stylesheet: list[str] = 'StyleSheet'
    image: list[str] = 'Image'
    stream: Var[str] = 'ReactPDF'
    viewer: Var[str] = 'PDFViewer'

react_pdf = react_pdf.create