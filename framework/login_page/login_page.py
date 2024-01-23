from .content import (CONFIRM_BUTTON, LOGIN_BUTTON,
                      PASSWORD_FIELD, USERNAME_FIELD)
from framework.page import Page


class LoginPage(Page):
    def click_login_button(self):
        login_button = self.find_element_with_waiting(*LOGIN_BUTTON)
        self.click_element(login_button)

    def enter_email(self, email):
        username_field = self.find_element_with_waiting(*USERNAME_FIELD)
        self.clear_field(username_field)
        self.send_keys_to_element(username_field, email)

    def enter_password(self, password):
        password_field = self.find_element_with_waiting(*PASSWORD_FIELD)
        self.clear_field(password_field)
        self.send_keys_to_element(password_field, password)

    def click_confirm_button(self):
        confirm_button = self.find_element_with_waiting(*CONFIRM_BUTTON)
        self.click_element(confirm_button)

    def login(self, email, password):
        self.click_login_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_confirm_button()

    def navigate_to_starting_page(self):
        self.driver.back()
