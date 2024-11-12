import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
texts = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
split_text = texts.split(" ")
email = split_text[4]
driver.close()
driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "#terms").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
# error = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-danger col-md-12'] strong").text
# Explicit wait is required because error message only shows up briefly after a few seconds
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
error = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
# alert = driver.switch_to.alert
# error = alert.text
print(error)
time.sleep(3)
