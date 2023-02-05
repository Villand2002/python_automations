import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path ="c:\\users\\st200\\appdata\\local\\programs\\python\\Python311\\"

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.co.jp/")

time.sleep(3)
driver.quit()