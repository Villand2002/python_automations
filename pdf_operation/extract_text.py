# pip install pdfminer.six
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

# pip install PyPDF2
from PyPDF2 import PdfFileReader

with open("2019-11-Chaos_Engineering_Whitepaper.pdf", "rb") as input:
    reader = PdfFileReader(input)

    # pdfの総ページ数は？
    print("2019-11-Chaos_Engineering_Whitepaper.pdf.pdf has %d pages.\n" % reader.getNumPages())

# 指定のページのデータを読み込む
    page = reader.getPage(0)

    # 読み込んだページのテキストを抽出
    print(page.extractText())