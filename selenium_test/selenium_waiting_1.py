from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
cur_path=os.path.dirname(__file__)
filename=os.path.join(cur_path, "chromedriver.exe")
service = Service(filename)
browser = webdriver.Chrome(service=service)                       #声明浏览器 
 #隐式等待:在查找所有元素时，如果尚未被加载，则等10秒
browser.implicitly_wait(10)
browser.get('https://www.baidu.com')
input_tag=browser.find_element(By.ID,'kw')
input_tag.send_keys('python')
input_tag.send_keys(Keys.ENTER)
#content_left属性在搜索结果页面，没有等待环节而直接查找，找不到则会报错
contents=browser.find_element(By.ID,'content_left') 
print(contents.text)
browser.close()

