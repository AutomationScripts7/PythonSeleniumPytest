import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#Directly hard coded parameterise instead of doing in fixture and json file
# @pytest.mark.parametrize("crossBrowser_1", ["Chrome", "Edge", "IE"])
# @pytest.mark.parametrize("login_data", [{"username": "admin", "password": "pass123"}])

class TestCrossBrowser():

    def test_launchURL(self, crossBrowser_1, login_data):
        if crossBrowser_1 == "Chrome":
            driver = webdriver.Chrome()
        elif crossBrowser_1 == "Edge":
            driver = webdriver.Edge()
        elif crossBrowser_1 == "IE":
            driver = webdriver.Ie()

        driver.get("https://rahulshettyacademy.com/angularpractice/")
        time.sleep(2)

# json & params - Yes! Both approaches achieve data-driven testing (running multiple times with different data)

        driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(login_data["username"])
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(login_data["password"])

        time.sleep(2)



