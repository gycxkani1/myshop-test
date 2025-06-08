from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
cur_path = os.path.dirname(__file__)
filename = os.path.join(cur_path, "chromedriver.exe")
service = Service(filename)
browser = webdriver.Chrome(service=service)                    # 声明浏览器
url = 'https://www.baidu.com'
browser.get(url)                                               # 打开浏览器预设网址
print(browser.page_source)                                     # 打印网页源代码
# browser.close()                                                # 关闭浏览器
