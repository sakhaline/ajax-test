import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


def test_sidebar_button_displayed(user_login_fixture,
                                  sidebar_fixture):
    user_login_fixture.login('qa.ajax.app.automation@gmail.com',
                             'qa_automation_password')
    try:
        element = sidebar_fixture.find_element(AppiumBy.ID,
                                               'com.ajaxsystems:id/menuDrawer')
        assert element.is_displayed(), 'Sidebar button element is present on the page.'
    except NoSuchElementException:
        pytest.fail('Sidebar button element is not present on the page.')


@pytest.mark.parametrize(
    'key,element,name',
    [
        pytest.param(AppiumBy.ID, 'com.ajaxsystems:id/settings', 'Settings',
                     id='test is settings button displayed'),
        pytest.param(AppiumBy.ID, 'com.ajaxsystems:id/help', 'Help',
                     id='test is help button displayed'),
        pytest.param(AppiumBy.ID, 'com.ajaxsystems:id/logs', 'Report problem',
                     id='test is report problem button displayed'),
        pytest.param(AppiumBy.ID, 'com.ajaxsystems:id/camera', 'Cctv',
                     id='test is cctv button displayed'),
        pytest.param(AppiumBy.XPATH,
                     '(//android.widget.TextView[@resource-id="com.ajaxsystems:id/text"])[2]', 'Add hub',
                     id='test is add button displayed'),
        pytest.param(AppiumBy.ID, 'com.ajaxsystems:id/documentation_text', 'Doc',
                     id='test is doc button displayed'),
    ]
)
def test_sidebar_content(sidebar_fixture, key, element, name):
    sidebar_fixture.open_sidebar()
    try:
        element = sidebar_fixture.find_element(key, element)
        assert element.is_displayed(), f'{name} button element is present on the page.'
    except NoSuchElementException:
        pytest.fail(f'{name} button element is not present on the page.')
    sidebar_fixture.driver.back()
