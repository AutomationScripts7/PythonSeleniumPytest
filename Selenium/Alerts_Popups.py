import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Python")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

#switching to alert

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

assert "Python" in alert_text   #validating value should present in get text

alert.accept()      #Accept
#alert.dismiss()     #Reject

time.sleep(2)