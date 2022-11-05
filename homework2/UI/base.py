from _pytest.fixtures import FixtureRequest

from UI.fixtures import *
from UI.pages.base_page import BasePage
from UI.pages.campaign_page import CampaignsPage
from UI.pages.segment_page import SegmentPage


class BaseCase:
    driver = None
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.base_page = BasePage(driver)
        self.campaign_page: CampaignsPage = (
            request.getfixturevalue('campaign_page'))
        self.segment_page: SegmentPage = (
            request.getfixturevalue('segment_page'))
