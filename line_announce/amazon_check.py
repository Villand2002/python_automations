# 必要なライブラリをインストール
# pip install requests
# pip install beautifulsoup4 スクレイピング用
# pip install line-bot-sdk line用

# ライブラリを用意
import schedule
from time import sleep
# 定期実行ライブラリ

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
    # "https://store.m-78.jp/collections/all/products/4573102651419",
    "https://www.amazon.co.jp/S-H-%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2%E3%83%BC%E3%83%84-%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%9E%E3%83%B3%E3%83%A1%E3%83%93%E3%82%A6%E3%82%B9-%E7%B4%84150mm-PVC%E8%A3%BD-%E5%A1%97%E8%A3%85%E6%B8%88%E3%81%BF%E5%8F%AF%E5%8B%95%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2/dp/B0BTH9R3T5/ref=sr_1_2?gclid=Cj0KCQiA2-2eBhClARIsAGLQ2RnAM1R-LGrcdckTnBaribI1yfDS214QfHrfQ1vva3BYnUEuvV4ZY0gaAn7LEALw_wcB&keywords=%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%9E%E3%83%B3%E3%83%A1%E3%83%93%E3%82%A6%E3%82%B9+%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2%E3%83%BC%E3%83%84&qid=1675389208&sr=8-2",
    # "https://www.amazon.co.jp/BANDAI-SPIRITS-S-H-%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2%E3%83%BC%E3%83%84-%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%9E%E3%83%B3%E3%82%BC%E3%83%83%E3%83%88-%E5%A1%97%E8%A3%85%E6%B8%88%E3%81%BF%E5%8F%AF%E5%8B%95%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2/dp/B093BXKQDQ/ref=sr_1_7?adgrpid=141093636942&gclid=Cj0KCQiA2-2eBhClARIsAGLQ2Rn5c6thcvpurWIvjyWYcncxGgSAfvb5A8adWZuibj1TUVtJ_KIeXVsaAsFBEALw_wcB&hvadid=636933216914&hvdev=c&hvlocphy=1009717&hvnetw=g&hvqmt=b&hvrand=16450286563717984569&hvtargid=kwd-1398202071341&hydadcr=27641_14599319&jp-ad-ap=0&keywords=%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%9E%E3%83%B3%E3%83%A1%E3%83%93%E3%82%A6%E3%82%B9+%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2%E3%83%BC%E3%83%84&qid=1675390086&sr=8-7",
    # "https://www.amazon.co.jp/S-H-%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2%E3%83%BC%E3%83%84-%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%9E%E3%83%B3%E3%82%BF%E3%82%A4%E3%82%AC-%E7%B4%84150mm-ABS%E8%A3%BD-%E5%8F%AF%E5%8B%95%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2/dp/B07VSPMHM5/ref=sr_1_8?adgrpid=141093636942&gclid=Cj0KCQiA2-2eBhClARIsAGLQ2Rn5c6thcvpurWIvjyWYcncxGgSAfvb5A8adWZuibj1TUVtJ_KIeXVsaAsFBEALw_wcB&hvadid=636933216914&hvdev=c&hvlocphy=1009717&hvnetw=g&hvqmt=b&hvrand=16450286563717984569&hvtargid=kwd-1398202071341&hydadcr=27641_14599319&jp-ad-ap=0&keywords=%E3%82%A6%E3%83%AB%E3%83%88%E3%83%A9%E3%83%9E%E3%83%B3%E3%83%A1%E3%83%93%E3%82%A6%E3%82%B9+%E3%83%95%E3%82%A3%E3%82%AE%E3%83%A5%E3%82%A2%E3%83%BC%E3%83%84&qid=1675390086&sr=8-8"
]

# LINE通知時の文字列
# result_str = "入荷\n"


# Joshin用
# result_str = "Joshin\n"
# for i in range(len(joshin_url)):
#     data = requests.get(joshin_url[i], headers = my_header)
#     data.encoding = data.apparent_encoding
#     data = data.text
#     soup = BeautifulSoup(data, "html.parser")
#     try:
#         stock = soup.find("form",{"name":"cart_button"}).text.encode("UTF-8")
#         print(stock) # デバッグ
#         if ("販売" in stock) == False: # 販売休止中ですとなっていなければ在庫あり
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

def prices():
    # Amazon用
    for i in range(len(amazon_url)):

        data = requests.get(amazon_url[i], headers = my_header)
        data.encoding = data.apparent_encoding
        data = data.text
        soup = BeautifulSoup(data, "html.parser")
        
        # 在庫があるかテキスト抽出
        # stock= soup.find_all("div",class_='price__badges price__badges--listing')
        # 価格のテキスト抽出
        detail=soup.find("span",class_='a-price-whole').text
        
        # 数値データを整形
        detail2=detail.replace(',', '')
        # int型に変換
        price=int(detail2)
        
        # print(stock['aria-label'])->[]によって属性の取得が可能(参考:https://pytutorial.com/get-aria-label-beautifulsoup/)
        # 参考2:https://store.m-78.jp/collections/recommend/products/4562294006657
        
        # print(stock['aria-hidden']) # 一応デバッグ
        # もしsaleがhiddenなら通知しない
        if (price <= 8000): 
            # 価格が8000以上なら在庫なしとする
            result_str = f"様子見だし...\n価格は{price}円\n{amazon_url[i]}\n"
            # それ以外は通知
        # elif(previous>=price):
        #     result_str = "価格上昇だし...様子見だし...\n"+"価格は"+str(price)+"円\n"+amazon_url[i]+"\n"
        # if(price <= 7500 and previous<price):
        #     result_str = "価格上昇,けど買ってもよいし...\n"+"価格は"+str(price)+"円だし...\n"+amazon_url[i]+"\n"                
        else:
            result_str = "だめだし...\n"+"転売だし...\n価格は"+str(price)+"円だし...\n"+amazon_url[i]+"\n"
        
        line_bot_api.push_message(LINE_USER_ID, TextSendMessage(text=result_str))    
            # print(result_str)    
            
#関数実行 
prices()            
            
            

schedule.every(15).minutes.do(prices)
# 15分ごとに実行する

#03 イベント実行
while True:
    schedule.run_pending()
    sleep(1)            

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