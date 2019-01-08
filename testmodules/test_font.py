import os
import sys
import docx

# Add the absolute path of the parent path into PYTHONPATH
from shutil import copyfile
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import docxhelper
from docx import Document
from docx.table import Table

class TestFontModule(unittest.TestCase):
    def test_SetEastAsianFont_ToStyle(self):
        srcFileName = "test_SetEastAsianFont_ToStyle_before.docx"
        dstFileName = "test_SetEastAsianFont_ToStyle_after.docx"
        doc = Document(srcFileName)
        style = doc.styles["Normal"]
        docxhelper.SetEastAsianFont_ToStyle(style, "맑은고딕")
        doc.save(dstFileName)

if __name__ == '__main__':
    print("Check output word files.")
    unittest.main()



