from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
cur_path=os.path.dirname(__file__)
filename=os.path.join(cur_path, "chromedriver.exe")
service = Service(filename)
browser = webdriver.Chrome(service=service)                             #声明浏览器
url = 'https://www.baidu.com'
browser.get(url)                                                        #打开浏览器预设网址
#获取页面的文本框id
input_tag = browser.find_element(By.ID,'kw')
input_tag.send_keys('python')
# 键盘回车
input_tag.send_keys(Keys.ENTER)
#休息2秒
time.sleep(2)
print(browser.page_source)                                              #打印网页源代码
browser.close()                                                         #关闭浏览器
