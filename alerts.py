import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Tobi")
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
# To switch to alert mode so as to catch javascript pop-ups:
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()
assert "Tobi" in alert_text





time.sleep(5)