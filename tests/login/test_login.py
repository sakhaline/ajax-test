import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.parametrize(
        "email,password",
        [
            pytest.param("qa.ajax.app.automation@gmail.com",
                         "11111",
                         id="login with invalid password"),
            pytest.param("automation@gmail.com",
                         "qa_automation_password",
                         id="login with invalid email"),
        ]
)
def test_failed_login(user_login_fixture, email, password, SNACKBAR):
    user_login_fixture.login(email, password)
    try:
        element = user_login_fixture.find_element(*SNACKBAR)
        assert element.is_displayed(), "Snackbar element is present on the page."
    except NoSuchElementException:
        pytest.fail("Snackbar element is not present on the page.")


def test_successful_login(user_login_fixture, ADD_HUB_BUTTON):
    email = "qa.ajax.app.automation@gmail.com"
    password = "qa_automation_password"
    user_login_fixture.login(email, password)
    try:
        element = user_login_fixture.find_element(*ADD_HUB_BUTTON)
        assert element.is_displayed(), "AddHub element is present on the page."
    except NoSuchElementException:
        pytest.fail("AddHub element is not present on the page.")
