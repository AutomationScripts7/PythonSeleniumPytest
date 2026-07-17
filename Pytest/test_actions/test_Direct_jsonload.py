import json

from Pytest.PageObjects.CheckoutCart import checkoutCart
from Pytest.PageObjects.SelectCart import SelectCart



json_path = 'C:\\Users\\615074106\\PythonBasics\\Pytest\\TestData\\test_Direct_JsonLoad.json'

with open(json_path) as file:
    data_get_data = json.load(file)

class TestJsonload:
    def test_E2E(self,launchBrower_CommandLineOption):

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
        search_Page.search_item(data_get_data["textboxSearch"])       #calling from PageObject(search_item)

        checkoutItem_Page = checkoutCart(driver)
        checkoutItem_Page.checkout_item(data_get_data["DiscountPromoCode"])




#NOTE FOR JSON LOAD:

#Correct. If it's single test data, just access it directly:

#data_get_data["DiscountPromoCode"]  # no parametrize needed

#@pytest.mark.parametrize is only needed when you want to run the same test multiple times with different data.

#Summary:
#Scenario                            - Single data	- Direct access: data["key"]
#Multiple data (run test N times)	 - @pytest.mark.parametrize


#"promocodes" → Temporary variable name (nee edhu venalum vachikalam: user, record, item, data_set)

#data_get_data["promocodes"] → JSON la irukkura list

#Pytest → Andha list la irukkura ovvoru dictionary-yum promocodes variable-ku assign panni test-a separate-a run pannum.

##Array [] is only needed when you have multiple items to iterate over in json
#Example
#{
  #"promocodes": [{"code": "abc"}, {"code": "xyz"}],
  #"textboxSearch": "berry"
#}
