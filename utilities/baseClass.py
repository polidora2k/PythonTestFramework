import inspect
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


"""
    BaseClass provides utilities to be used in
    all test cases.  
"""
@pytest.mark.usefixtures("setup")
class BaseClass:

    """
        verifyLinkTestPresence uses a wait function to verify
        that link text is present.
    """
    def verifyLinkTextPresence(self, linkText):
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, linkText)))

    """
        selectDropDownByText creates a Select object and selects
        an option based on the visibleText provided.
    """
    def selectDropDownByText(self, element, visibleText):
        dropdown = Select(element)
        dropdown.select_by_visible_text(visibleText)

    """
        getLogger creates a logger object and sets up formatting 
        and log files for use throughout the project. Returns a 
        logging object
    """
    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # Get the current files name.
        logger = logging.getLogger(loggerName)  # Create a logging object.
        fileHandler = logging.FileHandler(f"/Users/ipolidora/PycharmProjects/PythonTestFramework/testLogs/testlog.log")  # Create a fileHandler object with a log file.
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")  # Create a formatter to format log messages.
        fileHandler.setFormatter(formatter)  # Set the formatter of the fileHandler.
        logger.addHandler(fileHandler)  # Add the handler to the logger object.

        logger.setLevel(logging.DEBUG)  # Set the logging level to debug.
        return logger
