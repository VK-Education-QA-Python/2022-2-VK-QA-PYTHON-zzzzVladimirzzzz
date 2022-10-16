from selenium.webdriver.common.by import By
from base import BaseCase
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pytest
from locators.locators import *

WAIT_TIME = 10

@pytest.mark.UI
class TestMain(BaseCase):
    def test_login(self, login, driver):
        self.find(by=By.XPATH, what=LOCATOR_RIGHT_MODULE)
        self.find(by=By.XPATH, what=LOCATOR_BALANCE)

    def test_logout(self, login, logout):
        self.find(by=By.XPATH, what=LOCATOR_LOGIN_MENU).click()
        self.find(by=By.XPATH, what=LOCATOR_REG_FORM)

    def test_negative_login(self, driver, negative_preconditions_login):
        sign_in = self.find(by=By.XPATH, what=LOCATOR_LOGIN_BUTTON)
        sign_in.click()
        self.find(by=By.XPATH, what=LOCATOR_REG)

    def test_negative_incorrect_password(self, driver, negative_preconditions_login):
        password_negative = '1'
        email = self.find(by=By.XPATH, what=LOCATOR_LOGIN_EMAIL_INPUT)
        email.click()
        email.send_keys(password_negative)
        time.sleep(10)
        password = self.find(by=By.XPATH, what=LOCATOR_LOGIN_PASSWORD_INPUT)
        password.click()
        password.send_keys(password_negative)
        sign_in = self.find(by=By.XPATH, what=LOCATOR_LOGIN_BUTTON)
        sign_in.click()
        self.find(by=By.XPATH, what=LOCATOR_ERROR_PASSWORD_NOTIFICATION)

    def test_profile(self, login, driver):
        profile = self.find(by=By.XPATH, what=LOCATOR_PROFILE)
        profile.click()
        surname_input = self.find(by=By.XPATH, what=LOCATOR_SURNAME_INPUT)
        surname_input.clear()
        surname_input.send_keys('Петров Александр Александрович')
        save_button = self.find(by=By.XPATH, what=LOCATOR_SAVE_PROFILE_BUTTON)
        save_button.click()
        driver.refresh()
        self.find(by=By.XPATH, what=LOCATOR_FIO)

    @pytest.mark.parametrize('locator, exp',
                             [
                                (LOCATOR_PROFILE, LOCATOR_SURNAME_INPUT),
                                (LOCATOR_SEGMENTS, LOCATOR_PRICE_LIST)
                             ]
                             )
    def test_change(self, login, locator, exp):
        try:
            s = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, locator)))
            s.click()
        except NoSuchElementException:
            print('Page does not load or item not found')
        self.find(by=By.XPATH, what=exp)
