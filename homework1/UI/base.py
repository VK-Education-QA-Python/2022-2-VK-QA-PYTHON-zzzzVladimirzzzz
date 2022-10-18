import pytest
from UI.locators import locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, by, what, timeout=None):
        return self.wait(timeout).until(ec.presence_of_element_located((by, what)))

    def logout(self):
        clicks = 50
        time_clicks = 0.01
        for _ in range(clicks):
            try:
                right_module = self.find(by=By.XPATH, what=locators.LOCATOR_RIGHT_MODULE)
                right_module.click()
                logout_elem = self.find(by=By.XPATH, what=locators.LOCATOR_LOGOUT)
                logout_elem.click()
                break
            except StaleElementReferenceException:
                time.sleep(time_clicks)
            except ElementClickInterceptedException:
                time.sleep(time_clicks)
