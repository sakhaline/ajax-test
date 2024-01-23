import pytest

from framework.login_page.login_page import LoginPage
from framework.settings.settings import Settings
from framework.sidebar.sidebar import SideBar


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    login_page = LoginPage(driver)
    yield login_page


@pytest.fixture(scope="module")
def user_logout_fixture(driver):
    yield
    sidebar = SideBar(driver)
    sidebar.open_sidebar()
    settings = Settings(driver)
    settings.open_settings()
    settings.logout()
