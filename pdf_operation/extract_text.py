# pip install pdfminer.six
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_text_to_fp

pdf_path=(input("ファイルパスを指定:"))

text = extract_text(pdf_path)
print(text)

# 参考:https://office54.net/python/module/pdf-pdfminer-six#section1-2





# pip install PyPDF2
from PyPDF2 import PdfFileReader