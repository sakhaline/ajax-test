import pytest
from appium.webdriver.common.appiumby import AppiumBy

from framework.login_page.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    login_page = LoginPage(driver)
    yield login_page
    login_page.navigate_to_starting_page()
