import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Initialize WebDriver
driver = webdriver.Chrome()

# Add implicit wait
driver.implicitly_wait(10)

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

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# Close the browser after operations are complete
#driver.quit()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

