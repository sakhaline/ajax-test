import pytest
from appium.webdriver.common.appiumby import AppiumBy

from framework.login_page.login_page import LoginPage


ADD_HUB_BUTTON = (AppiumBy.ID, 'com.ajaxsystems:id/snackbar_text')
SNACKBAR = (AppiumBy.ID, 'com.ajaxsystems:id/hubAdd')


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)
