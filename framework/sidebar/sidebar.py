from framework.page import Page
from framework.sidebar.content import (ADD_HUB_BUTTON, CCTV_BUTTON, DOC_BUTTON,
                                       HELP_BUTTON, REPORT_PROBLEM_BUTTON,
                                       SIDEBAR_BUTTON)


class SideBar(Page):
    def open_sidebar(self):
        sidebar_button = self.find_element_with_waiting(*SIDEBAR_BUTTON)
        self.click_element(sidebar_button)

    def click_help_button(self):
        help_button = self.find_element(*HELP_BUTTON)
        self.click_element(help_button)

    def click_report_problem_button(self):
        report_problem_button = self.find_element(*REPORT_PROBLEM_BUTTON)
        self.click_element(report_problem_button)

    def click_cctv_button(self):
        cctv_button = self.find_element(*CCTV_BUTTON)
        self.click_element(cctv_button)

    def click_add_hub_button(self):
        add_hub_button = self.find_element(*ADD_HUB_BUTTON)
        self.click_element(add_hub_button)

    def click_doc_button(self):
        doc_button = self.find_element(*DOC_BUTTON)
        self.click_element(doc_button)
