import pytest
import logging
from selenium.common.exceptions import NoSuchElementException


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
        ]
)
def test_failed_login(user_login_fixture, email, password, SNACKBAR):
    logging.info(f'Running test_failed_login with email:'
                 '{email}, password: {password}')

    user_login_fixture.login(email, password)
    try:
        element = user_login_fixture.find_element(*SNACKBAR)
        assert element.is_displayed()
        logging.info('Test failed as expected, Snackbar element is present.')
    except NoSuchElementException:
        logging.error('Test failed.'
                      'Snackbar element is not present on the page.')
        pytest.fail('Snackbar element is not present on the page.')


def test_successful_login(user_login_fixture, ADD_HUB_BUTTON):
    email = 'qa.ajax.app.automation@gmail.com'
    password = 'qa_automation_password'
    logging.info(f'Running test_successful_login with email: '
                 '{email}, password: {password}')

    user_login_fixture.login(email, password)
    try:
        element = user_login_fixture.find_element(*ADD_HUB_BUTTON)
        assert element.is_displayed()
        logging.info('Test passed, AddHub element is present.')
    except NoSuchElementException:
        logging.error('Test failed. '
                      'AddHub element is not present on the page.')
        pytest.fail('AddHub element is not present on the page.')
