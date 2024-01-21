from framework.page import Page
from content import (SETTINGS_BUTTON,
                     HELP_BUTTON,
                     REPORT_PROBLEM_BUTTON,
                     CCTV_BUTTON,
                     ADD_HUB_BUTTON,
                     DOC_BUTTON,
                     WINDOW_HEIGHT,
                     WINDOW_WIDTH,)
from appium.webdriver.common.touch_action import TouchAction


class SideBar(Page):
    def click_settings_button(self):
        settings_button = self.find_element(*SETTINGS_BUTTON)
        self.click_element(settings_button)

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

    def close_sidebar(self):
        start_x = int(WINDOW_HEIGHT * 0.2)
        end_x = int(WINDOW_WIDTH * 0.8)
        y = int(WINDOW_HEIGHT * 0.5)

        swipe = TouchAction(self.driver)
        swipe.long_press(x=start_x,
                         y=y).move_to(x=end_x,
                                      y=y).release().perform()
