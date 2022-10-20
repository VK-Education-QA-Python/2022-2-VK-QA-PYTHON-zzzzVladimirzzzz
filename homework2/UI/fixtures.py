import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from UI.pages.base_page import BasePage
from UI.pages.campaign_page import CampaignsPage
from UI.pages.segment_page import SegmentPage
from UI.locators.basic_locators import *


WAIT_TIME = 10


@pytest.fixture()
def driver(request):
    url = 'https://target-sandbox.my.com/#'
    options = Options()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    if request.config.option.headless:
        options.add_argument('--headless')
        options.add_argument('--window-size=1280x1696')
        options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)
    yield driver
    driver.quit()


@pytest.fixture()
def cookies(driver):
    login_page = LoginPage(driver)
    login_page.login(user="povarov.vova99@gmail.com", password="Password!")
    cookies = driver.get_cookies()
    return cookies


class LoginPage(BasePage):

    def login(self, user, password):
        self.click((By.XPATH, LOCATOR_LOGIN_MENU))
        self.find((By.XPATH, LOCATOR_LOGIN_EMAIL_INPUT)).send_keys(user)
        self.find((By.XPATH, LOCATOR_LOGIN_PASSWORD_INPUT)).send_keys(password)

        self.click((By.XPATH, LOCATOR_LOGIN_BUTTON))

        time.sleep(5)
        return BasePage(driver=driver)


@pytest.fixture()
def campaign_page(driver):
    return CampaignsPage(driver=driver)


@pytest.fixture()
def segment_page(driver):
    return SegmentPage(driver=driver)
