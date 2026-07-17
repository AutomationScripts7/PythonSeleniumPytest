from Pytest.PageObjects.SelectCart import SelectCart
from Pytest.PageObjects.CheckoutCart import checkoutCart
from Pytest.utils.JSON_Reader import JSON_Reader


class Test_GS_JSON_Load:

    def test_gs_json_load(self, launchBrower_CommandLineOption):
        driver = launchBrower_CommandLineOption
        data = JSON_Reader()

        search_Page = SelectCart(driver)
        search_Page.search_item(data.get_data("gs_customer", "textboxSearch"))

        checkoutItem_Page = checkoutCart(driver)
        checkoutItem_Page.checkout_item(data.get_data("gs_customer", "DiscountPromoCode"))

        GetTitle = search_Page.getTitle()
        print(GetTitle)
