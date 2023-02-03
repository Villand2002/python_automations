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
# lineのアクセストークンを発行した
LINE_ACCESS_TOKEN = "m/9mwPtYtq0QO9wdKbGxJRugOAqBNrYvrLJla9iKu+D19NMPi+irlHat8uG1R32oZ/nC3O8EkV5VKktHdyGZjoCfieM7YUelsrN75Pc8p9rjPFEIrCos39d9VNT6WwG54yTsOFb6wM1t9wO+/FBQmwdB04t89/1O/w1cDnyilFU="
# line apiの設定画面にあるuser idを使用　参考:https://developers.line.biz/ja/docs/messaging-api/getting-user-ids/#getting-user-ids
LINE_USER_ID = "Uba3820ea2244f41dcaf50075ef614449"
line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)

# UA偽装用
my_header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko"
}
# 入荷待ち用のurl
amazon_url = [
    "https://store.m-78.jp/collections/all/products/4573102651419",
    "https://store.m-78.jp/collections/recommend/products/4562294006657"
]

# LINE通知時の文字列
result_str = "入荷\n"


# Joshin用
# result_str = "Joshin\n"
# for i in range(len(joshin_url)):
#     data = requests.get(joshin_url[i], headers = my_header)
#     data.encoding = data.apparent_encoding
#     data = data.text
#     soup = BeautifulSoup(data, "html.parser")
#     try:
#         detail = soup.find("form",{"name":"cart_button"}).text.encode("UTF-8")
#         print(detail) # デバッグ
#         if ("販売" in detail) == False: # 販売休止中ですとなっていなければ在庫あり
#             if(i == 0) : result_str += "ネオン在庫あり\n"
#             if(i == 1) : result_str += "グレー在庫あり\n"
#     except AttributeError:
#             print("Error")

# # Joshin用LINE通知
# if result_str != "Joshin\n":
#     try:
#         line_bot_api.push_message(LINE_USER_ID, TextSendMessage(text=result_str))
#     except LineBotApiError as e:
#         print(e)

# Amazon用
# result_str = "円谷store\n"
for i in range(len(amazon_url)):
    # print(len(amazon_url))
    data = requests.get(amazon_url[i], headers = my_header)
    data.encoding = data.apparent_encoding
    data = data.text
    soup = BeautifulSoup(data, "html.parser")
    # 販売情報の取得
    # saleがhiddenなら通達しない
    #     <span class="price__badge price__badge--sale" aria-hidden="true">
    #       <span>SALE</span>
    #     </span>
    # 在庫があるかテキスト抽出

    detail = soup.find("span",class_='price__badge price__badge--sale')
        
    # print(f['aria-label'])->属性の取得    参考:https://pytutorial.com/get-aria-label-beautifulsoup/
    # 参考2:https://store.m-78.jp/collections/recommend/products/4562294006657
    # print(detail['aria-hidden']) # 一応デバッグ
    # もしsaleがhiddenなら通知しない
    
    if ("true" in detail['aria-hidden']): 
        # aria-hidden=trueなら在庫なしとする
        result_str = "在庫なし"
        # それ以外は通知
    elif("true" in detail['aria-hidden'] and ):
        result_str = "在庫あり,今すぐ購入\n"+amazon_url[i]
    line_bot_api.push_message(LINE_USER_ID, TextSendMessage(text=result_str))    
        # print(result_str)    

#参考として価格を得るコード 
# def get_price(amazon_url):
#     res = requests.get(amazon_url)
#     soup = bs4.BeautifulSoup(res.text, features="lxml")
#     selected_html = soup.select('.a-span12 span.a-color-price')

#     if not selected_html:
#         selected_html = soup.select('.a-color-base span.a-color-price')

#     pattern = r'\d*,?\d*,?\d*\d'
#     regex = re.compile(pattern)
#     matches = re.findall(regex, selected_html[0].text)
#     price = matches[0].replace(',', '')
#     return int(price)
        

# Amazon用LINE通知
# if result_str != "在庫あり,今すぐ購入\n" :
#     try:
#         line_bot_api.push_message(LINE_USER_ID, TextSendMessage(text=result_str))
#     except LineBotApiError as e:
#         print(e)



# 参考文献
# https://qiita.com/haifuri/items/98137c23feff90f12af2
# announce

# https://qiita.com/kawa-Kotaro/items/f417e7a5776a8ece0d0b
# get price