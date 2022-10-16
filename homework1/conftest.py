import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from UI.locators import locators

WAIT_TIME = 10


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')


@pytest.fixture()
def driver(request):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    if request.config.option.headless:
        options.add_argument('--headless')
        options.add_argument('--window-size=1280x1696')
        options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get('https://target-sandbox.my.com/#')
    try:
        login = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, locators.LOCATOR_LOGIN_MENU)))
        login.click()
    except NoSuchElementException:
        print("The page hasn't loaded yet")
    email = driver.find_element(By.XPATH, locators.LOCATOR_LOGIN_EMAIL_INPUT)
    email.send_keys('povarov.vova99@gmail.com')
    password = driver.find_element(By.XPATH, locators.LOCATOR_LOGIN_PASSWORD_INPUT)
    password.send_keys('Password!')
    sign_in = driver.find_element(By.XPATH, locators.LOCATOR_LOGIN_BUTTON)
    sign_in.click()


@pytest.fixture()
def negative_preconditions_login(driver):
    driver.get('https://target-sandbox.my.com/#')
    try:
        login = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, locators.LOCATOR_LOGIN_MENU)))
        login.click()
    except NoSuchElementException:
        print("The page hasn't loaded yet")
