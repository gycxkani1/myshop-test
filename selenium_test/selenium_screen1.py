from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
cur_path=os.path.dirname(__file__)
filename=os.path.join(cur_path, "chromedriver.exe")
savefilename=os.path.join(cur_path,'screen01.png')
service = Service(filename)
browser = webdriver.Chrome(service=service)#声明浏览器
browser.get("http://www.jd.com")
# 将当前网页窗口保存为screen01.png文件，保存在当前目录
browser.save_screenshot(savefilename)
browser.quit()