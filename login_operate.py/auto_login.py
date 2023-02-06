from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
 
# webdriverのpathを指定する 
driverpath = "C:\\Users\\st200\\Downloads\\chromedriver_win32\\chromedriver.exe"

# chrome driverとchromeのversionが一致する必要がある.2023/2/6時点では地王していないためすぐに落ちる
 
# ドライバー指定でChromeブラウザを開く
# serviceメソッドが推奨のよう
chrome_service = fs.Service(executable_path=driverpath)
browser = webdriver.Chrome(service=chrome_service)
 
# Googleをエンジンとして用いている。
browser.get('https://www.google.com/')
 
 
# 検索ボックスを指定.
elem = browser.find_element(By.NAME, 'q')

# 「九大moodle」と入力して、「Enter」を押す
elem.send_keys('九大moodle' + Keys.RETURN)

#検索結果1位をクリック
g = browser.find_elements(By.CLASS_NAME,"g")[0]
# print(g)
r = g.find_element(By.CLASS_NAME,"r")
r.click()

# version非対応につき確認できたのはここまで

# ログイン操作を実行する.
# browser.find_element(By.属性,その中身) で要素の中身を取得
username = browser.find_element(By.ID,'username') 
password=browser.find_element(By.ID,'password') 

# 指定したフォームのクリア
username.clear()
password.clear()

# send_keysでキーボード入力
username.send_keys("具体的な文字列")
password.send_keys("パスワード")

# それぞれ送信
username.submit()
password.submit()

# もしくは最初に文字列を入力
# username.send_keys('具体的な文字列')
# パスワード入力後にenter keyを押すようにする　とよいか?

# password.send_keys('パスワード'+ Keys.RETURN)
# ブラウザを閉じる
# browser.quit()

# 参考:https://self-development.info/selenium-4%E3%81%A7%E3%80%8Cdeprecationwarning%E3%80%8D%E3%81%8C%E5%87%BA%E3%82%8B%E5%A0%B4%E5%90%88%E3%81%AE%E5%AF%BE%E7%AD%96/
# https://yaspage.com/yasunolog/python-selenium1/
# 自動ログイン:https://qiita.com/wejhhv/items/59d739b40dc6f7f5aabc
# version更新:https://bluegoat.jp/blog/chrome-driver/