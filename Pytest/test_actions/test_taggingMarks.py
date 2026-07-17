import json

import pytest

from Pytest.PageObjects.CheckoutCart import checkoutCart
from Pytest.PageObjects.SelectCart import SelectCart


json_path = 'C:\\Users\\615074106\\PythonBasics\\Pytest\\TestData\\test_Direct_JsonLoad.json'

with open(json_path) as file:
    data_get_data = json.load(file)

@pytest.mark.smoke
class TestJsonload:
    def test_E2E(self,launchBrower_CommandLineOption):

        driver = launchBrower_CommandLineOption     #parameterise the fixture

        search_Page = SelectCart(driver)    #creating object for Pageobject and also inherite the file
        search_Page.search_item(data_get_data["textboxSearch"])       #calling from PageObject

        checkoutItem_Page = checkoutCart(driver)
        checkoutItem_Page.checkout_item(data_get_data["DiscountPromoCode"])

