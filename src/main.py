from docling.document_converter import DocumentConverter

pdf_source = "data/pdf/2309.13057v3.pdf"
xls_source = "data/xlsx/test-01.xlsx"
converter = DocumentConverter()
pdf_result = converter.convert(pdf_source)
xls_result = converter.convert(xls_source)
print(pdf_result.document.export_to_markdown())
print(xls_result.document.export_to_dict())
