# 必要なライブラリをインストール
# pip install requests
# pip install beautifulsoup4
# pip install line-bot-sdk

# ライブラリを用意
import re
import requests
from bs4 import BeautifulSoup
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

LINE_ACCESS_TOKEN = "LINEのアクセストークンをペースト"
LINE_USER_ID = "LINEのユーザーIDをペースト"
line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)

# UA偽装用
my_header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko"
}
# 入荷待ち用のurl
amazon_url = [
    "https://www.amazon.co.jp/S-H-%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2%E3%83%BC%E3%83%84-%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%9E%E3%83%B3%E3%83%A1%E3%83%93%E3%82%A6%E3%82%B9-%E7%B4%84150mm-PVC%E8%A3%BD-%E5%A1%97%E8%A3%85%E6%B8%88%E3%81%BF%E5%8F%AF%E5%8B%95%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2/dp/B0BTH9R3T5/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=1I8TFWS4CXR4B&keywords=%E3%83%A1%E3%83%93%E3%82%A6%E3%82%B9+%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2%E3%83%BC%E3%83%84&qid=1675329143&sprefix=%E3%83%A1%E3%83%93%E3%82%A6%E3%82%B9+%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2%E3%83%BC%E3%83%84%2Caps%2C253&sr=8-1"
]

# LINE通知時の文字列
result_str = "入荷価格:str(get_price(amazon_url))"

def get_price(page_url):
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    selected_html = soup.select('.a-span12 span.a-color-price')

    if not selected_html:
        selected_html = soup.select('.a-color-base span.a-color-price')

    pattern = r'\d*,?\d*,?\d*\d'
    regex = re.compile(pattern)
    matches = re.findall(regex, selected_html[0].text)
    price = matches[0].replace(',', '')
    return int(price)


def get_title(page_url):
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    selected_html = soup.select('#productTitle')
    title = selected_html[0].text
    title = title.replace(' ', '')
    title = title.replace('\n', '')
    return title