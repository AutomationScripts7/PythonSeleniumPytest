import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
time.sleep(2)
driver.maximize_window()

products_list = driver.find_elements(By.XPATH, "//h4[@class='card-title']")

for product in products_list:
    product_text = product.text
    print(product_text)
    driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[1]").click()
    break
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'#country').send_keys("ind")
time.sleep(5)

dropdown_values = driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul/li/a")

for value in dropdown_values:
    print(value)
    if value.text == "India":
        value.click()
        break

time.sleep(5)
checkbox = driver.find_element(By.XPATH, "//input[@id='checkbox2']")
driver.execute_script("arguments[0].click();", checkbox)
time.sleep(5)
driver.close()
