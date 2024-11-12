import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("Password1")
driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("Password1")
time.sleep(4)
driver.find_element(By.XPATH, "//button[@type='submit']").click()


time.sleep(10)


