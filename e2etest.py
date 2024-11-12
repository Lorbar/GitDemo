import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[href*='/angularpractice/shop']").click()
items = driver.find_elements(By.XPATH, "//h4")
# item_text = [item.text for item in items]
for item in items:
    if item.text == "Blackberry":
        location = items.index(item) + 1
        driver.find_element(By.XPATH, f"(//button[@class='btn btn-info'])[{location}]").click()
        break
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
success = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
#print(success)
assert "Success! Thank you!" in success
time.sleep(3)