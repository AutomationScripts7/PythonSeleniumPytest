import time
from selenium import webdriver


#webdriver.ChromeOptions
chrome_options = webdriver.ChromeOptions()

#Running in headless
chrome_options.add_argument("--headless")

#Ignore SSL Certifications errors
chrome_options.add_argument("--ignore-certificate-errors")

#Launching maximize window while launching itself
chrome_options.add_argument("--start-maximized")



driver = webdriver.Edge(options=chrome_options)
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
