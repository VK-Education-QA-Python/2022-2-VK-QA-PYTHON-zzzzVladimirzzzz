import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        chance_find = 10
        time_finds = 0.01
        try:
            for _ in range(chance_find):
                return self.wait(timeout).until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            time.sleep(time_finds)

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(ec.element_to_be_clickable(locator))
        elem.click()

    def send_keys(self, locator, send_input):
        elem = self.find(locator=locator)
        elem.clear()
        elem.send_keys(send_input)

    def file_upload(self, locator, file_path):
        elem = self.driver.find_element(*locator)
        elem.send_keys(file_path)
