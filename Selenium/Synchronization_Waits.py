#time.sleep - suspends execution of the current thread for a specified number of seconds.
#Implicit Wait  - global, time-based setting
#Explicit Wait  - dynamic, condition-based pause
#Fluent Wait    - polling frequency interval - highly customizable variant of an explicit wait that allows you to define
# the exact polling frequency interval and configure an exclusion list for specific exceptions to ignore while polling.

#wait = WebDriverWait(driver,timeout=30,poll_frequency=2,ignored_exceptions=[NoSuchElementException]
#element = wait.until(EC.presence_of_element_located((By.ID, "myElement")))

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

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
driver.implicitly_wait(10)
WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)


#sum of validation of price


total_values = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p") #way of writing CCS for index ( nth-child(index) )
sum = 0
for total in total_values:
    Grand_Total_Price = total.text
    sum = sum + int(Grand_Total_Price)
print(sum)

Total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == Total_amount


driver.close()




