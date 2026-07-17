#driver.current_window_handle   -   Returns current window ID
#driver.window_handles  -   Returns all window IDs (list)
#driver.switch_to.window(handle)    -   Switch to a window

#OPENING NEW TAB
#driver.execute_script("window.open('https://www.bing.com');")


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
url = "https://the-internet.herokuapp.com/windows"
driver.get(url)
driver.maximize_window()
time.sleep(2)

# driver.find_element(By.LINK_TEXT, "Click Here").click()

#Getting current window handle
parent_window = driver.current_window_handle    #current window stored

#Getting how many windows currently opened
current_WindowOpened = driver.window_handles        #1 window

driver.switch_to.window(current_WindowOpened[1])    #switching window with current window of index

NewWindow_tag = driver.find_element(By.TAG_NAME, "h3").text
print(NewWindow_tag)
print(driver.title)

#Close child window alone
driver.close()

#switching window back with current window of index
# driver.switch_to.window(current_WindowOpened[0])

#Another method switch using parent window which is stored already
driver.switch_to.window(parent_window)


#Using loop
# for handle in current_WindowOpened:
#     if handle != parent_window:
#         driver.switch_to.window(handle)
#         print("Switched to new window")



driver.close()

