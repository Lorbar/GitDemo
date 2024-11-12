import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\tajao\\Documents\\chromedriver.exe")

#driver = webdriver.Chrome()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Testing")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Tobi")

# XPATH ->//tagname[@attribute="value"]
# CSS -> tagname[attribute="value"]

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("HelloAgain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


assert "Success" in message








time.sleep(6)