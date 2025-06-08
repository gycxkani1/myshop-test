from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
cur_path=os.path.dirname(__file__)
print(cur_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
filename=os.path.join(cur_path, "chromedriver.exe")
service = Service(filename)
browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get("https://www.jd.com/")

width=browser.execute_script("return document.body.scrollWidth")
height=browser.execute_script("return document.body.scrollHeight")
browser.set_window_size(width,height)
time.sleep(10)
# 将当前网页窗口保存为screen01.png文件，保存在当前目录
browser.save_screenshot(os.path.join(cur_path,"screen02.png"))
browser.quit()