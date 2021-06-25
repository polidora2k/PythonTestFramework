from selenium.webdriver.common.by import By
from pageObjects.checkoutPage import CheckoutPage


"""
    ShopPage class is used to control elements on the shop page of the
    tested website. Provides methods to access all elements.
"""
class ShopPage:

    # Create variables to hold element search values
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    """
        Constructor function to add driver.
    """
    def __init__(self, driver):
        self.driver = driver

    """
        Return card titles web elements.
    """
    def getCardTitles(self):
        return self.driver.find_elements(*ShopPage.cardTitle)

    """
        Return card footer buttons web elements.
    """
    def getCardFooterButtons(self):
        return self.driver.find_elements(*ShopPage.cardFooter)

    """
        Clicks checkout button and returns a new CheckoutPage object.
    """
    def clickCheckoutButton(self):
        self.driver.find_element(*ShopPage.checkout).click()
        return CheckoutPage(self.driver)
