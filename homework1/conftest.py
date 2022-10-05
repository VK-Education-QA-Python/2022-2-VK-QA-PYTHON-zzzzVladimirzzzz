import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


WAIT_TIME = 10


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true')


@pytest.fixture()
def driver(request):
    if request.config.option.headless:
        options = Options()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        options.add_argument('--headless')
        options.add_argument('--window-size=1280x1696')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.implicitly_wait(10)
    driver.get('https://target-sandbox.my.com/#')
    try:
        login = driver.find_element(By.XPATH, "//*[contains(@class, 'responseHead-module-button')]")
        login.click()
    except NoSuchElementException:
        print("The page hasn't loaded yet")
    email = driver.find_element(By.XPATH, "//*[contains(@class,'authForm-module-input') and "
                                          "contains(@class,'input-module-input')]")
    email.click()
    email.send_keys('povarov.vova99@gmail.com')
    password = driver.find_element(By.XPATH, "//*[contains(@class,'authForm-module-inputPassword')]")
    password.click()
    password.send_keys('Password!')
    sign_in = driver.find_element(By.XPATH, "//*[contains(@class,'authForm-module-button')]")
    sign_in.click()


@pytest.fixture()
def negative_preconditions_login(driver):
    driver.implicitly_wait(10)
    driver.get('https://target-sandbox.my.com/#')
    try:
        login = driver.find_element(By.XPATH, "//*[contains(@class,'responseHead-module-button')]")
        login.click()
    except NoSuchElementException:
        print("The page hasn't loaded yet")


@pytest.fixture()
def logout(driver):
    time.sleep(5)
    right_module = driver.find_element(By.XPATH, "//*[contains(@class,'right-module-userNameWrap')]")
    right_module.click()
    time.sleep(5)
    logout_elem = driver.find_element(By.XPATH, "//*[@href='/logout']")
    logout_elem.click()
