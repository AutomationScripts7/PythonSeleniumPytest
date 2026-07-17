#A frame (iframe) is a web page inside another web page
#Selenium cannot directly access elements inside a frame
#You must switch into the frame first


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
url = "https://the-internet.herokuapp.com/windows"
driver.get(url)
driver.maximize_window()
time.sleep(2)

#Switch iframe using index
driver.switch_to.frame(0)

#Switch iframe using ID alone
driver.switch_to.frame("mce_0_ifr")

#Switch iframe using find xpath and pass it switch frame
iframe = driver.find_element(By.XPATH, "//iframe[@id='mce_0_ifr']")
driver.switch_to.frame(iframe)

#Switching back to default content
driver.switch_to.default_content()

