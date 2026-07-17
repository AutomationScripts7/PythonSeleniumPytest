from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


class checkoutCart:

    def __init__(self, driver):
        self.driver = driver
        self.click_purchasedIcon = (By.CSS_SELECTOR, "img[alt='Cart']")
        self.click_checkoutButton = "//button[text()='PROCEED TO CHECKOUT']"



    def checkout_item(self, DiscountPromoCode):
        # Validating total discount amount less than total amount

        self.driver.find_element(*self.click_purchasedIcon).click()
        self.driver.find_element(By.XPATH, self.click_checkoutButton).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys(DiscountPromoCode)
        self.driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException]).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
        print(self.driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

        Total_amount = int(self.driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
        print(Total_amount)

        Total_after_Discount = float(self.driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
        print(Total_after_Discount)

        assert Total_amount > Total_after_Discount
