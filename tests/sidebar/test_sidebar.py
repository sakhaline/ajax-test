import logging

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from framework.sidebar.content import (ADD_HUB_BUTTON, CCTV_BUTTON, DOC_BUTTON,
                                       HELP_BUTTON, REPORT_PROBLEM_BUTTON,
                                       SETTINGS_BUTTON)


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

LOGGER = logging.getLogger(__name__)


def test_sidebar_button_displayed(login_logout_fixture, sidebar_fixture):
    LOGGER.info('Running test_sidebar_button_displayed')
    try:
        element = sidebar_fixture.find_element_with_waiting(
            AppiumBy.ID, 'com.ajaxsystems:id/menuDrawer'
        )
        assert element, 'Sidebar button element is present on the page.'
        LOGGER.info('Test passed, Sidebar button is displayed.')
    except NoSuchElementException:
        LOGGER.error('Test failed. Sidebar button element is not present on the page.')
        pytest.fail('Sidebar button element is not present on the page.')


@pytest.mark.parametrize(
    'key,element,name',
    [
        pytest.param(*SETTINGS_BUTTON, 'Settings',
                     id='test is settings button displayed'),
        pytest.param(*HELP_BUTTON, 'Help',
                     id='test is help button displayed'),
        pytest.param(*REPORT_PROBLEM_BUTTON, 'Report problem',
                     id='test is report problem button displayed'),
        pytest.param(*CCTV_BUTTON, 'CCTV',
                     id='test is cctv button displayed'),
        pytest.param(*ADD_HUB_BUTTON, 'Add hub',
                     id='test is add button displayed'),
        pytest.param(*DOC_BUTTON, 'Doc',
                     id='test is doc button displayed'),
    ]
)
def test_sidebar_content(sidebar_fixture, key, element, name):
    LOGGER.info(f"Running test_sidebar_content with element: {name}")

    sidebar_fixture.open_sidebar()
    try:
        element = sidebar_fixture.find_element(key, element)
        assert element.is_displayed(), f'{name} button element is present.'
        LOGGER.info(f'Test passed, {name} button is displayed.')
    except NoSuchElementException:
        LOGGER.error(f'Test failed. {name} button element is not present.')
        pytest.fail(f'{name} button element is not present on the page.')
