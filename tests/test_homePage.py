import logging
import pytest
from pageObjects.homePage import HomePage
from testData.homePageData import HomePageData
from utilities.baseClass import BaseClass

"""
    TestHomePage holds all pytest methods for testing 
    of the Home Page.
"""
class TestHomePage(BaseClass):

    """
        test_formSubmission holds the testing script to
        test the form submission page and its functionality.
    """
    def test_formSubmission(self, getData):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")  # Go to website.
        logger = self.getLogger()  # Create logger object
        homePage = HomePage(self.driver)  # Create HomePage object

        homePage.getNameBox().send_keys(getData["Name"])  # Send information to the name box
        homePage.getEmailBox().send_keys(getData["Email"]) # Send information to the email box
        homePage.getPasswordBox().send_keys(getData["Password"])  # Send information to the password box
        homePage.getIceCreamCheckBox().click()  # Click the checkbox

        assert homePage.getIceCreamCheckBox().is_selected(), logger.error("Checkbox was not checked.")  # Assert the that the checkbox is selected

        self.selectDropDownByText(homePage.getGenderDropDown(), getData["Gender"])  # Select appropriate gender from dropdown

        employmentStatusButtons = homePage.getRadioButtons()  # Retrieve radio buttons
        # Find the appropriate employment status
        for button in employmentStatusButtons:
            if button.text == getData["EmpStatus"]:
                button.click()
                break

        homePage.getBirthdayTextBox().send_keys(getData["Birthday"].strip())  # Send information to the birthday box

        homePage.getSubmitButton().click()  # Click the submit button.

        alertText = homePage.getSuccessMessage().text  # Get the alert text

        assert "Success! The Form has been submitted successfully!" in alertText, logging.error("Success message doesn't match.")  # Assert that the success message matches

    """
        getData sends retrieved test case data and sends it to 
        test_formSubmission.
    """
    @pytest.fixture(params=HomePageData().getData())
    def getData(self, request):
        return request.param
