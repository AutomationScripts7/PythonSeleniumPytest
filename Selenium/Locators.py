import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

# service_Object =  Service(executable_path="path of chrome driver")
# driver = webdriver.Edge(service=service_Object)

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
driver.maximize_window()

#ID Locator
driver.find_element(By.ID, 'openwindow').click()

#-----------------------------------------
print(driver.current_window_handle)
currentWindow = driver.window_handles
driver.switch_to.window(currentWindow[1])
print(driver.title)
driver.switch_to.window(currentWindow[0])
time.sleep(5)
#-----------------------------------------

#NAME Locator
driver.find_element(By.NAME, 'checkBoxOption1').click()
time.sleep(2)

#CLASS NAME Locator
driver.find_element(By.CLASS_NAME, "inputs").click()
time.sleep(2)

#TAGNAME Locator
inputs = driver.find_elements(By.TAG_NAME, "input")
print(f"Number of input fields: {len(inputs)}")

#LINKTEXT Locator
driver.find_element(By.LINK_TEXT, "All Access plan").click()
time.sleep(2)

#PARTIAL LINK TEXT Locator
driver.find_element(By.PARTIAL_LINK_TEXT, "Mentor").click()
time.sleep(5)

#-------------------------------------------

element = driver.find_element(By.CSS_SELECTOR, "#autocomplete")
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)

#-------------------------------------------

#CSS SELECTOR Locator
driver.find_element(By.CSS_SELECTOR, "#autocomplete").send_keys("Python")

#XPATH Locator
driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
time.sleep(5)


