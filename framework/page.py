class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, key, value):
        return self.driver.find_element(key, value)

    def click_element(self, element):
        element.click()

    def send_keys_to_element(self, element, value):
        element.send_keys(value)
