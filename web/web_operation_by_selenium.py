import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path ="c:\\users\\st200\\appdata\\local\\programs\\python\\Python311\\"

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.co.jp/")

time.sleep(3)
driver.quit()


# 参考:https://tech-blog.rakus.co.jp/entry/20221222/selenium#%E8%A6%81%E7%B4%A0%E3%81%AE%E5%8F%96%E5%BE%97
# https://reffect.co.jp/python/selenium#chromedriver