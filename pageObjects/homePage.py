from selenium.webdriver.common.by import By
from pageObjects.shopPage import ShopPage


"""
    HomePage class is used to control elements on the home page of the
    tested website. Provides methods to access all elements.
"""
class HomePage:

    # Create variables to hold element search values
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    nameBox = (By.CSS_SELECTOR, "[name='name']")
    emailBox = (By.CSS_SELECTOR, "[name='email']")
    passwordBox = (By.CSS_SELECTOR, "[id='exampleInputPassword1']")
    iceCreamCheckBox = (By.XPATH, "//input[@id='exampleCheck1']")
    genderDropDown = (By.CSS_SELECTOR, "select[id='exampleFormControlSelect1']")
    radioButtons = (By.CSS_SELECTOR, ".form-check.form-check-inline")
    birthday = (By.CSS_SELECTOR, "[name='bday']")
    submit = (By.CSS_SELECTOR, ".btn.btn-success")
    successMessage = (By.CSS_SELECTOR, ".alert-success")

    """
        Constructor function to add driver.
    """
    def __init__(self, driver):
        self.driver = driver

    """
        Clicks shop button and returns new ShopPage object.
    """
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        return ShopPage(self.driver)

    """
        Return name box web element.
    """
    def getNameBox(self):
        return self.driver.find_element(*HomePage.nameBox)

    """
        Return email box web element.
    """
    def getEmailBox(self):
        return self.driver.find_element(*HomePage.emailBox)

    """
        Return password box web element.
    """
    def getPasswordBox(self):
        return self.driver.find_element(*HomePage.passwordBox)

    """
        Return ice cream checkbox web element.
    """
    def getIceCreamCheckBox(self):
        return self.driver.find_element(*HomePage.iceCreamCheckBox)

    """
        Return gender dropdown list web element.
    """
    def getGenderDropDown(self):
        return self.driver.find_element(*HomePage.genderDropDown)

    """
        Return radio web elements.
    """
    def getRadioButtons(self):
        return self.driver.find_elements(*HomePage.radioButtons)

    """
        Return birthday box web element.
    """
    def getBirthdayTextBox(self):
        return self.driver.find_element(*HomePage.birthday)

    """
        Return submit button web element.
    """
    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submit)

    """
        Return success message web element.
    """
    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
