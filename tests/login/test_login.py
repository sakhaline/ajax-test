import logging

import pytest
from selenium.common.exceptions import NoSuchElementException

from framework.login_page.content import ADD_HUB, SNACKBAR


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

LOGGER = logging.getLogger(__name__)


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
def test_failed_login(user_login_fixture, user_logout_fixture,
                      email, password):
    LOGGER.info(f'Running test_failed_login with email: {email}, password: {password}')

    user_login_fixture.login(email, password)
    try:
        element = user_login_fixture.find_element_with_waiting(*SNACKBAR)
        assert element.is_displayed()
        LOGGER.info('Test passed, Snackbar element is present.')
    except NoSuchElementException:
        LOGGER.error('Test failed. Snackbar element is not present on the page.')
        pytest.fail('Snackbar element is not present on the page.')
    finally:
        user_login_fixture.navigate_to_starting_page()


def test_successful_login(user_login_fixture):
    email = 'qa.ajax.app.automation@gmail.com'
    password = 'qa_automation_password'

    LOGGER.info(f'Running test_successful_login with email: {email}, password: {password}')

    user_login_fixture.login(email, password)
    try:
        element = user_login_fixture.find_element_with_waiting(*ADD_HUB)
        assert element.is_displayed()
        LOGGER.info('Test passed, AddHub element is present.')
    except NoSuchElementException:
        LOGGER.error('Test failed. AddHub element is not present on the page.')
        pytest.fail('AddHub element is not present on the page.')
