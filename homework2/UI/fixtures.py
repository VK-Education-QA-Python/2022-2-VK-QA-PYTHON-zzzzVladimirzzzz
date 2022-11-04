import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from UI.locators.basic_locators import *
from UI.pages.base_page import BasePage
from UI.pages.campaign_page import CampaignsPage
from UI.pages.segment_page import SegmentPage


@pytest.fixture()
def driver(request):
    url = 'https://target-sandbox.my.com/#'
    options = Options()
    if request.config.option.headless:
        options.add_argument('--headless')
        options.add_argument('--window-size=1280x1696')
        options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


class LoginPage(BasePage):

    def login(self, user, password):
        self.click((By.XPATH, LOCATOR_LOGIN_MENU))
        self.find((By.XPATH, LOCATOR_LOGIN_EMAIL_INPUT)).send_keys(user)
        self.find((By.XPATH, LOCATOR_LOGIN_PASSWORD_INPUT)).send_keys(password)
        self.click((By.XPATH, LOCATOR_LOGIN_BUTTON))
        return BasePage(driver=driver)


@pytest.fixture()
def campaign_page(driver):
    return CampaignsPage(driver=driver)


@pytest.fixture()
def segment_page(driver):
    return SegmentPage(driver=driver)


@pytest.fixture()
def create_picture_path(repo_root):
    return os.path.join(repo_root, 'UI', 'static', 'picture.jpeg')


@pytest.fixture()
def create_audio_path(repo_root):
    return os.path.join(repo_root, 'UI', 'static', 'audio.mp3')
