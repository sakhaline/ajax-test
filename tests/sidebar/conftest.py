import pytest

from framework.sidebar.sidebar import SideBar


@pytest.fixture(scope='function')
def sidebar_fixture(driver):
    yield SideBar(driver)
