from framework.page import Page
from framework.sidebar.content import SIDEBAR_BUTTON


class SideBar(Page):
    def open_sidebar(self):
        sidebar_button = self.find_element_with_waiting(*SIDEBAR_BUTTON)
        self.click_element(sidebar_button)
