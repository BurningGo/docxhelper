from docx import Document
from docx.oxml import OxmlElement
from docx.shared import Pt, Inches
from docx.oxml.ns import qn
from docx.enum.text import WD_COLOR_INDEX


#   SetEastAsianFont_ToStyle
#   Function : Set 'eastasian font' to a style of word
#   Parameter
#       - style    : e.g. doc.styles['Normal']
#       - fontName (type str): Font Name of an East Asian font, e.g. 맑은고딕
def SetEastAsianFont_ToStyle(style, fontName : str):
    r = style._element
    r.rPr.rFonts.set(qn('w:eastAsia'), fontName)



