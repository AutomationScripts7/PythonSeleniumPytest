
import time
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
url = "https://rahulshettyacademy.com/seleniumPractise/#/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

product_list = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(product_list))

assert len(product_list) > 0

for product in product_list:
    product.find_element(By.XPATH, "div/button").click()


#validating items are added as expected list


expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_list = []

total_item = driver.find_elements(By.XPATH, "//div[@class='products']/div/h4")

for item in total_item:
    # actual_list.append(item.text)
    iterate_item = item.text
    print(iterate_item)
    actual_list.append(iterate_item)
assert expected_list == actual_list


#Validating total discount amount less than total amount

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
driver.implicitly_wait(10)
WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)


Total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(Total_amount)

Total_after_Discount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(Total_after_Discount)

assert Total_amount > Total_after_Discount