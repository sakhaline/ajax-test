from content import SIDEBAR_BUTTON, ADD_HUB_BUTTON
from framework.page import Page


class MainPage(Page):
    def click_sidebar_button(self):
        sidebar_button = self.find_element(*SIDEBAR_BUTTON)
        self.click_element(sidebar_button)

    def click_add_hub_button(self):
        add_hub_button = self.find_element(*ADD_HUB_BUTTON)
        self.click_element(add_hub_button)
