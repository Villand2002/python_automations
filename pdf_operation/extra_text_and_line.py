# pip install pdfminer.six
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_text_to_fp
import re
import requests
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError


# lineのアクセストークンを発行した
LINE_ACCESS_TOKEN = "LG1JJenumeNg48nEaEOL8ttX5p2jOo69ujh3i+ckeSaUf5DU1sL9z57qEnNVVoT7Cc67Lkd5m6Rf9gINgurrToRdONtqFzrF4WGIen7+EuAVf1ZVDfYwjgnHzG+rph7DMa4HbMOHmhsuG7OKz4+/kwdB04t89/1O/w1cDnyilFU="

# line apiの設定画面にあるuser idを使用　参考:https://developers.line.biz/ja/docs/messaging-api/getting-user-ids/#getting-user-ids

LINE_USER_ID = "U4cd4cb0169a09ed3c12fe53438ff3943"
line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)

# コンマをなくし成形
pdf_path=(input("ファイルパスを指定:")).replace('"','').replace("ファイルパスを指定:",'')

#pdfからテクスト抽出    
extract_text = extract_text(pdf_path)
# print(extract_text)　デバック用


if(len(extract_text)<=400):
    # lineで本文を送る
    line_bot_api.push_message(LINE_USER_ID, TextSendMessage(text=extract_text))
else:
    # おそらく文字数正弦波400字なのでそれを通達
    extract_text="文字列が多いんだよ!\n教えはどうしたんだ教えは!\n"+pdf_path
    # lineで送る
    line_bot_api.push_message(LINE_USER_ID, TextSendMessage(text=extract_text))
            


# 参考:https://office54.net/python/module/pdf-pdfminer-six#section1-2
# https://dev.classmethod.jp/articles/export-text-data-from-pdf-using-python/