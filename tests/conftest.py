import pytest
from selenium import webdriver


"""
    pytest_addoption allows for a browser to be chosen from the command line.
    Default value is chrome.
"""
def pytest_addoption(parser):
    parser.addoption("--bn", action="store", default="chrome")  # Adds browser selection option.


"""
    setup provides initializing step for the testing environment.
"""
@pytest.fixture(scope="class")
def setup(request):
    # Retrieve the browser name from the command line.
    browserName = request.config.getoption("bn")

    # Determine the browser and initialize the driver.
    if browserName == "chrome":
        driver = webdriver.Chrome("/Users/ipolidora/WebDrivers/chromedriver")
    elif browserName == "firefox":
        driver = webdriver.Firefox("/Users/ipolidora/WebDrivers/geckodriver")
    elif browserName == "edge":
        driver = webdriver.Edge("/Users/ipolidora/WebDrivers/edgedriver_mac64/msedgedriver")

    driver.maximize_window()  # Maximize the browser window.
    request.cls.driver = driver  # Pass the driver to the class.
    yield
    driver.close()  # Close the driver after finished testing
