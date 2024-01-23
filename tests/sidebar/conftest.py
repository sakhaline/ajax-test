import pytest

from framework.login_page.login_page import LoginPage
from framework.settings.settings import Settings
from framework.sidebar.sidebar import SideBar


@pytest.fixture(scope='function')
def sidebar_fixture(driver):
    yield SideBar(driver)


@pytest.fixture(scope='module')
def login_logout_fixture(driver):
    login_page = LoginPage(driver)
    login_page.login('qa.ajax.app.automation@gmail.com',
                     'qa_automation_password')
    yield
    settings = Settings(driver)
    settings.open_settings()
    settings.logout()
