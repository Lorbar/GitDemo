import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.CSS_SELECTOR, "th[aria-label='Veg/fruit name: activate to sort column ascending']").click()
web_veggies = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
web_veggies_text = [item.text for item in web_veggies]
# veggies = ["Almond", "Apple", "Banana", "Beans", "Brinjal"]
veggies_sorted = sorted(web_veggies_text)
assert veggies_sorted == web_veggies_text
time.sleep(3)