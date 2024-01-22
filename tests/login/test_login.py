from lib2to3.pgen2 import driver
import pytest
import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

# from tests.login.conftest import ADD_HUB_BUTTON, SNACKBAR

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.mark.parametrize(
        'email,password',
        [
            pytest.param('qa.ajax.app.automation@gmail.com',
                         '11111',
                         id='login with invalid password'),
            pytest.param('automation@gmail.com',
                         'qa_automation_password',
                         id='login with invalid email'),
            pytest.param('incorrect.email',
                         'qa_automation_password',
                         id='login with incorrect email'),
        ]
)
def test_failed_login(user_login_fixture, email, password):
    logging.info(('Running test_failed_login with email:'
                  f'{email}, password: {password}'))

    user_login_fixture.login(email, password)
    try:
        element = user_login_fixture.find_element(*(AppiumBy.ID, 'com.ajaxsystems:id/snackbar_text'))
        assert element.is_displayed()
        logging.info('Test passed, Snackbar element is present.')
    except NoSuchElementException:
        logging.error(('Test failed.'
                       'Snackbar element is not present on the page.'))
        pytest.fail('Snackbar element is not present on the page.')


def test_successful_login(user_login_fixture):
    email = 'qa.ajax.app.automation@gmail.com'
    password = 'qa_automation_password'
    logging.info(('Running test_successful_login with email: '
                  f'{email}, password: {password}'))

    user_login_fixture.login(email, password)
    try:
        element = user_login_fixture.find_element(*(AppiumBy.ID, 'com.ajaxsystems:id/hubAdd'))
        assert element.is_displayed()
        logging.info('Test passed, AddHub element is present.')
    except NoSuchElementException:
        logging.error(('Test failed. '
                       'AddHub element is not present on the page.'))
        pytest.fail('AddHub element is not present on the page.')
