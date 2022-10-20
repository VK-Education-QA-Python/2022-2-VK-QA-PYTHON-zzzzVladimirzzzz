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
        return self.wait(timeout).until(ec.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        send_clicks = 5
        time_clicks = 0.01
        for _ in range(send_clicks):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(ec.element_to_be_clickable(locator))
                elem.click()
                break
            except TimeoutException:
                time.sleep(time_clicks)
        else:
            raise TimeoutException

    def send_keys(self, locator, send_input, timeout=None):
        send_clicks = 5
        time_clicks = 0.01
        for _ in range(send_clicks):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(ec.element_to_be_clickable(locator))
                elem.clear()
                elem.send_keys(send_input)
                break
            except TimeoutException:
                time.sleep(time_clicks)
        else:
            raise TimeoutException

    def file_upload(self, locator, file_path):
        elem = self.driver.find_element(*locator)
        elem.send_keys(file_path)
