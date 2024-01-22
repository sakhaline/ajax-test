from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, key, value):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((key, value)))
        return element

    def click_element(self, element):
        element.click()
        return element

    def send_keys_to_element(self, element, value):
        element.send_keys(value)

    def clear_field(self, key, value):
        element = self.find_element(key, value)
        element = self.click_element(element)
        element.clear()
