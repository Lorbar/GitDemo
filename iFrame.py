import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Edited by selenium")
# NOTE: This would not work because the herokuapp web have placed the iFrame in read-only mode.