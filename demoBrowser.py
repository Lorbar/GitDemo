import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("C:\\Users\\tajao\\Documents\\chromedriver.exe")

#driver = webdriver.Chrome()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://netflix.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)










time.sleep(2)