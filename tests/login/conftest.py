import pytest

from framework.login_page.login_page import LoginPage
from appium.webdriver.common.appiumby import AppiumBy


ADD_HUB_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/snackbar_text")
SNACKBAR = (AppiumBy.ID, "com.ajaxsystems:id/hubAdd")


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)
