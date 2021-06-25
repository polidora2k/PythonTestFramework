from selenium.webdriver.common.by import By

"""
    PurchasePage class is used to control elements on the purchase page of the
    tested website. Provides methods to access all elements.
"""
class PurchasePage:

    # Create variables to hold element search values
    countryTextBox = (By.CSS_SELECTOR, "input[id='country']")
    termsCheckbox = (By.CSS_SELECTOR, "div.checkbox.checkbox-primary")
    submitButton = (By.CSS_SELECTOR, "input[type='submit']")
    successMessage = (By.CSS_SELECTOR, ".alert-success")

    """
        Constructor function to add driver.
    """
    def __init__(self, driver):
        self.driver = driver

    """
        Returns country text box web element.
    """
    def getCountryTextBox(self):
        return self.driver.find_element(*PurchasePage.countryTextBox)

    """
        Returns country web element corresponding to the provided link text.
    """
    def getCountry(self, linkText):
        return self.driver.find_element(*(By.LINK_TEXT, linkText))

    """
        Returns terms checkbox web element.
    """
    def getTermsCheckbox(self):
        return self.driver.find_element(*PurchasePage.termsCheckbox)

    """
        Returns submit button web element.
    """
    def getSubmitButton(self):
        return self.driver.find_element(*PurchasePage.submitButton)

    """
        Returns success message web element.
    """
    def getSuccessMessage(self):
        return self.driver.find_element(*PurchasePage.successMessage)
