import time

from selenium import webdriver


#chrome driver service - the ChromeDriver service acts as a middleman/bridge between your Selenium code and the Chrome browser
#if don't we have a browser or VPN restriction, we can download chrome webdriver file and call it as service class with path
# service_obj = Service("path of chrome webdriver zip/file.exe")

driver = webdriver.Edge()
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)
print(driver.title)
print(driver.current_url)


driver.close()

