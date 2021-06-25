from selenium.webdriver.common.by import By
from pageObjects.purchasePage import PurchasePage

"""
    CheckoutPage class is used to control elements on the checkout page 
    of the tested website. Provides methods to access all elements.
"""
class CheckoutPage:

    # Create variables to hold element search values
    checkoutButton = (By.XPATH, "//button[@class='btn btn-success']")

    """
        Constructor function to add driver.
    """
    def __init__(self, driver):
        self.driver = driver

    """
        Clicks checkout button and returns a new PurchasePage  object.
    """
    def clickCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        return PurchasePage(self.driver)

