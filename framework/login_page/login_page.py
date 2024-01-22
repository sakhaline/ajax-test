from framework.login_page.content import (LOGIN_BUTTON, PASSWORD_FIELD,
                                          USERNAME_FIELD, FIRST_LOGIN_BUTTON)

from framework.page import Page


class LoginPage(Page):
    def click_first_login_button(self):
        first_login_button = self.find_element(*FIRST_LOGIN_BUTTON)
        self.click_element(first_login_button)

    def enter_email(self, email):
        username_field = self.find_element(*USERNAME_FIELD)
        self.send_keys_to_element(username_field, email)

    def enter_password(self, password):
        password_field = self.find_element(*PASSWORD_FIELD)
        self.send_keys_to_element(password_field, password)

    def click_login_button(self):
        login_button = self.find_element(*LOGIN_BUTTON)
        self.click_element(login_button)

    def login(self, email, password):
        self.click_first_login_button()
        self.clear_field(*USERNAME_FIELD)
        self.enter_email(email)
        self.clear_field(*PASSWORD_FIELD)
        self.enter_password(password)
        self.click_login_button()
