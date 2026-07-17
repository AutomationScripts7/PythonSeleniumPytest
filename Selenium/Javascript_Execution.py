import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

#JS scroll into view element
element = driver.find_element(By.ID, "submitBtn")
driver.execute_script("argument[0].scrollIntoView();", element)

#NOTE:
#button1 = argument[0]
#button2 = argument[1]
#if argument[0] clicks the first button, argument[1] clicks the second button

#JS click
element = driver.find_element(By.ID, "submitBtn")
driver.execute_script("argument[0].click();", element)

#Scroll using range
driver.execute_script("window.scroll(0,500)")
time.sleep(2)
driver.get_screenshot_as_file("screenshot.png")

#Scroll into end
driver.execute_script("window.scroll(0,document.body.scrollHeight);")
time.sleep(2)

#Capture screenshot
driver.get_screenshot_as_file("screenshot.png")