import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome()

# Add implicit wait
driver.implicitly_wait(2)

# Open the website
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

# Find the search box and input text
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

# Wait for results to load
time.sleep(2)  # This is needed because of the find_elements method that returns a list, implicit wait does not apply

# Find all result elements
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

# Click each add to cart button
for result in results:
    result.find_element(By.XPATH, "div/button").click()

expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
time.sleep(2)
product_names = driver.find_elements(By.CSS_SELECTOR, ".product-name")
page_product_name = []
for name in product_names:
    if name.text != "":
        page_product_name.append(name.text)
print(page_product_name)
assert page_product_name == expected_list
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# Close the browser after operations are complete
#driver.quit()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
prices = driver.find_elements(By.XPATH, "//td[5]/p")
total = 0
for price in prices:
    total += int(price.text)
print(total)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)  # Explicit wait to target certain element only. Over-rides implicit wait.
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
amt_total = float(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
# assert total == amt_total
total_after_discount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
assert amt_total > total_after_discount
