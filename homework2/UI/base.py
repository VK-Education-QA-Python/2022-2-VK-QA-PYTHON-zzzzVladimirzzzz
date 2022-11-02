from _pytest.fixtures import FixtureRequest
from contextlib import contextmanager
from UI.fixtures import *
from UI.pages.base_page import BasePage
from UI.pages.campaign_page import CampaignsPage
from UI.pages.segment_page import SegmentPage


class BaseCase:
    driver = None
    authorize = True

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest, cookies):
        self.driver = driver
        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            self.base_page = BasePage(driver)
        self.campaign_page: CampaignsPage = (request.getfixturevalue('campaign_page'))
        self.segment_page: SegmentPage = (request.getfixturevalue('segment_page'))
