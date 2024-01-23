from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_waiting(self, key, value):
        element = WebDriverWait(
            self.driver, 10
        ).until(EC.presence_of_element_located((key, value)))
        return element

    def find_element(self, key, value):
        element = self.driver.find_element(key, value)
        return element

    @staticmethod
    def click_element(element):
        element.click()

    @staticmethod
    def send_keys_to_element(element, value):
        element.send_keys(value)

    @staticmethod
    def clear_field(field):
        field.clear()
