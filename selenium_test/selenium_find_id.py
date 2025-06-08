from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
cur_path=os.path.dirname(__file__)
filename=os.path.join(cur_path, "chromedriver.exe")
service = Service(filename)
browser = webdriver.Chrome(service=service)                                   # 声明浏览器
url = 'https://www.jd.com/'
browser.get(url)                                                              # 打开浏览器预设网址
cata_text = browser.find_element(By.ID, "J_cate")
print(cata_text.text)
print('*********')
cata_names = browser.find_elements(By.CLASS_NAME, "cate_menu_item")
for x in cata_names:
    print(x.text)
# browser.close()                                                               # 关闭浏览器
