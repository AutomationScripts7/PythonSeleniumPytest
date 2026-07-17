import json

import pytest

from Pytest.PageObjects.CheckoutCart import checkoutCart
from Pytest.PageObjects.SelectCart import SelectCart

json_path = 'C:\\Users\\615074106\\PythonBasics\\Pytest\\TestData\\test_Cart.json'

with open(json_path) as file:
    get_data = json.load(file)     #(loaded data from json file,whatever json upload here as it is [key:value, key:value])
    data_get_data = get_data["promocodes"]  #Getting the KEY : VALUE from json dictionary

# @pytest.mark.parametrize("gs_customer", data_get_data["promocodes"])  >commented
@pytest.mark.parametrize("gs_customer", data_get_data)
def test_E2E(launchBrower_CommandLineOption, gs_customer):

    #Cut and move to conftest file
    #---------------------------------------------------------------
    # driver = webdriver.Edge()
    # url = "https://rahulshettyacademy.com/seleniumPractise/#/"
    # driver.get(url)
    # driver.maximize_window()
    # time.sleep(2)
    #---------------------------------------------------------------
    driver = launchBrower_CommandLineOption     #parameterise the fixture

    search_Page = SelectCart(driver)    #creating object for Pageobject and also inherite the file
    search_Page.search_item(gs_customer["textboxSearch"])       #calling from PageObject

    checkoutItem_Page = checkoutCart(driver)
    checkoutItem_Page.checkout_item(gs_customer["DiscountPromoCode"])

    #Calling generic commands steps via PageObject
    GetTitle = search_Page.getTitle()
    print(GetTitle)






