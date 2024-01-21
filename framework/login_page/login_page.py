from content import LOGIN_BUTTON, PASSWORD_FIELD, USERNAME_FIELD

from framework.page import Page


class LoginPage(Page):
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
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
