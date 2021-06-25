from pageObjects.homePage import HomePage
from utilities.baseClass import BaseClass


"""
    TestE2E holds all pytest methods in the end to end
    module.
"""
class TestE2E(BaseClass):

    """
        test_end2end tests the full capabilities of an ecommerce
        site. The test opens the shop page and purchases a Blackberry.
        There is then an assertion for the success message.
    """
    def test_end2end(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")  # Open the website.
        logger = self.getLogger()  # Create the logger object.
        homePage = HomePage(self.driver)  # Create a HomePage object.

        shopPage = homePage.shopItems()  # Click the shop button and create a ShopPage object.
        cardTitles = shopPage.getCardTitles()  # Get the card titles.

        i = 0  # Initialize the counter
        # Iterate through the card titles to find Blackberry.
        for card in cardTitles:
            cardText = card.text  # Get the card text.

            # Check for the blackberry
            if cardText == "Blackberry":
                shopPage.getCardFooterButtons()[i].click()  # Click the footer button to add the product to the cart.
                logger.info("Selected Matching Product: Blackberry")
            i = i + 1  # Increment

        checkoutPage = shopPage.clickCheckoutButton()  # Click the checkout button and receive the CheckoutPage object
        purchasePage = checkoutPage.clickCheckoutButton()  # Click the checkout button and receive the PurchasePage object
        logger.info("Setting text to ind")
        purchasePage.getCountryTextBox().send_keys("ind")  # Get country text box and send keys to the box.

        self.verifyLinkTextPresence("India")  # Verify that the option is present.
        logger.info("Matching text found.")

        purchasePage.getCountry("India").click()  # Click the appropriate option.
        purchasePage.getTermsCheckbox().click()  # Click the checkbox.
        purchasePage.getSubmitButton().click()  # Click the submit button.

        successText = purchasePage.getSuccessMessage().text  # Get the text from the success message.
        logger.info(f"Alert text: {successText}")

        assert "Success! Thank you!" in successText, logger.error("Success message does not match")  # Check that the success message is valid


