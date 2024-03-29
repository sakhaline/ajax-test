from framework.page import Page
from framework.sidebar.content import SETTINGS_BUTTON

from .content import LOGOUT_BUTTON


class Settings(Page):
    def open_settings(self):
        settings_button = self.find_element(*SETTINGS_BUTTON)
        self.click_element(settings_button)

    def logout(self):
        logout_button = self.find_element(*LOGOUT_BUTTON)
        self.click_element(logout_button)
