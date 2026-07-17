#in PageObject no needs to follow test_ name rule
import time

from selenium.webdriver.common.by import By

from Pytest.utils.Generic_Commands import Generic_Wrapper


class SelectCart(Generic_Wrapper):
    def __init__(self, driver):
# once inherite the Pageobject to testcase calling class, we pass driver into object right. like that we have to give life to parent class file(Generic commands) by using super().__init(driver) to make it alive. this concept
#The parent class is a car body with steering and brakes, super().__init__(driver) is putting the engine (driver) inside it to make it functional.
        super().__init__(driver)
        self.driver = driver
        self.searchItem = (By.CSS_SELECTOR, ".search-keyword")

#self - instance of class variable
#self.driver = driver  (save the browser driver in this page object)
#self.enterusername = By.ID, "username"  (save the username field locator in this page object)

#if we don't use self in instance variable, life of variable inside the constructor only

    def search_item(self, textboxSearch):
        self.driver.find_element(*self.searchItem).send_keys(textboxSearch)
        time.sleep(2)
        product_list = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        print(len(product_list))
        assert len(product_list) > 0
        for product in product_list:
            product.find_element(By.XPATH, "div/button").click()





