import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ni")
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")

for country in countries:
    if country.text == "Nigeria":
        country.click()
        break

time.sleep(6)
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Nigeria"
