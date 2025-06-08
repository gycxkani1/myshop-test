from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
cur_path=os.path.dirname(__file__)
filename=os.path.join(cur_path, "chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
service = Service(filename)
driver = webdriver.Chrome(service=service, options=chrome_options)          #声明浏览器
url = 'https://www.baidu.com'
driver.get(url)                                                             #打开浏览器预设网址
print(driver.page_source)                                                   #打印网页源代码
driver.close()                                                              #关闭浏览器
