from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, key, value):
        return self.driver.find_element(key, value)

    def click_element(self, element):
        element.click()

    def send_keys_to_element(self, element, value):
        element.send_keys(value)

    def wait_for_element(self, key, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((key, value)))
