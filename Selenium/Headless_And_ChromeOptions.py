import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Calling CHROME OPTIONS/EdgeOptions class to run headless mode

headless_options = webdriver.EdgeOptions()
headless_options.add_argument("--headless")


#To ignore SSL cerfication like (CERTIFICATE ERRORS, CONNECTION IS SECURE, CONTINUE ADVANCE, ETC..), we can ignore my using this method

headless_options.add_argument("--ignore-certificate-errors")

#Running in headless as parameterize the options

driver = webdriver.Edge(options=headless_options)
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

#Scroll using range
driver.execute_script("window.scroll(0,500)")
time.sleep(2)

#Scroll into end
driver.execute_script("window.scroll(0,document.body.scrollHeight);")
time.sleep(2)
