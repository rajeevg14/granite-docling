from docling.document_converter import DocumentConverter
import pandas as pd

pdf_source = "data/pdf/2309.13057v3.pdf"
converter = DocumentConverter()
pdf_result = converter.convert(pdf_source)
md = pdf_result.document.export_to_markdown()

file_name = "data/xlsx/test-01.xlsx"
sheets = pd.read_excel(file_name, sheet_name=None)
for sheet in sheets:
    df = pd.read_excel(file_name, sheet_name=sheet)
    clms = df.columns.to_list()
    for clm in clms:
        print(clm)
