from reflex.components.component import NoSSRComponent
from reflex.vars import Var
from typing import Union, List,Dict, Optional
class react_pdf_lib(NoSSRComponent):
    """componente pdf react"""

    library = 'react-pdf'
    tag = 'PDFViewer'
    lib_dependencies: list[str] = ['@react-pdf/renderer']

    def _get_custom_code(self) -> str:
        return """
        import 'react-pdf/dist/Page/AnnotationLayer.css';
        import 'react-pdf/dist/Page/TextLayer.css';
        """

class react_pdf(react_pdf_lib):
    """componente pdf react"""
    children: Optional[Union[Var[str], str]] = None
    style: Var[Dict[str, List[str]]] = None
    class_Name: str = None
    width: Var[Union[str, float]] = None
    height: Var[Union[str,int]]  = None
    show_toolbar: Var[bool] = True

react_pdf = react_pdf.create