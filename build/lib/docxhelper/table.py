from docx import Document

def AlignAllCellsVerticallyCenter(table):
    n_row = len(table.rows)
    n_col = len(table.columns)

    for r in range(n_row):
        for c in range(n_col):
            tc = table.cell(r,c)._tc
            tcPr = tc.get_or_add_tcPr()
            tcVAlign = OxmlElement('w:vAlign')
            tcVAlign.set(qn('w:val'), "center")
            tcPr.append(tcVAlign)

