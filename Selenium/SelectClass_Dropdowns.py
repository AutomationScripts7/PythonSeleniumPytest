import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

#Static Dropdown
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)
#dropdown.select_by_value("value")
time.sleep(2)

#Dynamic Dropdown
url1 = "https://rahulshettyacademy.com/dropdownsPractise/"
driver.get(url1)
time.sleep(2)
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
# dropdown_values = driver.find_elements(By.CSS_SELECTOR, "a[class='ui-corner-all']")
#Another Option for CCS
dropdown_values = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(dropdown_values))

for values in dropdown_values:
    if values.text == "India":
        values.click()
        break

time.sleep(5)

#.text → for visible text content of non-input elements
# text = driver.find_element(By.ID, "autosuggest").text


#.get_attribute("value") → for the current value of input fields


text = driver.find_element(By.ID, "autosuggest").get_attribute("value")
print(text)
assert text == "India"
driver.quit()

#Note:
# element.get_attribute("value")       # "India"
# element.get_attribute("type")        # "text"
# element.get_attribute("class")       # "inputs"
# element.get_attribute("placeholder") # "Type to search"
# element.get_attribute("id")          # "autosuggest"
# element.get_attribute("href")        # for links
# element.get_attribute("src")         # for images
# element.get_attribute("innerHTML")   # inner HTML content
# element.get_attribute("outerHTML")   # full element HTML
