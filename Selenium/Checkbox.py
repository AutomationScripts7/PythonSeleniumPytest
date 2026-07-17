import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

#Checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    iterate_value = checkbox.get_attribute("value")
    if iterate_value == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break



#Radio Button and is_selected to validate whether checkbox or radiobutton is clicked or not

radioButtons = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
print(len(radioButtons))

for radiobutton in radioButtons:
    if radiobutton.get_attribute("value") == "radio1":
        radiobutton.click()
        time.sleep(2)
        assert radiobutton.is_selected()
        break



#Fixed radio button it won't change the position in future

radioButtons = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
radioButtons[2].click()
time.sleep(2)
assert radioButtons[2].is_selected()


#is_displayed

assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()

assert not driver.find_element(By.ID, "displayed-text").is_displayed()  #reverse the condition



driver.close()
