import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Add implicit wait
driver.implicitly_wait(5)
driver.maximize_window()

# Open the website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.CSS_SELECTOR, "a[href='#top']")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//a[normalize-space()='Reload']")).click().perform()