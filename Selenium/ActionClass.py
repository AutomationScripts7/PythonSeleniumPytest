import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

action = ActionChains(driver)
time.sleep(2)
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).click() #Click using ActionChains
action.perform()

action.send_keys_to_element(driver.find_element(By.CSS_SELECTOR, "#mouseover"),"Python").perform()  #Sendkeys values using actionchains

#Keyboard actions
action = ActionChains(driver)
time.sleep(2)
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover"))
action.send_keys(Keys.ENTER)    #ENTER
action.send_keys(Keys.SPACE)
action.send_keys(Keys.TAB)
action.send_keys(Keys.ARROW_DOWN)
action.send_keys(Keys.ARROW_UP)
action.send_keys(Keys.ARROW_LEFT)
action.send_keys(Keys.ARROW_RIGHT)

#Peform select all
action.key_down(Keys.CONTROL)           #key_down means hold that key
action.send_keys("a")
action.key_up(Keys.CONTROL)             #key_up means release that key
action.perform()



#Perform delete all
action.key_down(Keys.CONTROL)
action.send_keys("a")       # select all
action.key_up(Keys.CONTROL)
action.send_keys(Keys.DELETE)  # delete
action.perform()

