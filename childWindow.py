import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.CSS_SELECTOR, "a[href='/windows/new']").click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windows[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
# time.sleep(4)