import pytest

from UI.locators.basic_locators import *
from UI.static.data import *
from base import BaseCase
from UI.static.creds import creds


@pytest.mark.UI
class TestHomework2(BaseCase):
    def test_campaign_create(self, create_picture_path, create_audio_path):
        self.login_page.login(user=creds[0], password=creds[1])
        self.campaign_page.create_audio_campaign(url=YOUTUBE_URL,
                                                 file_path_audio=create_audio_path,
                                                 file_path_picture=create_picture_path)

        assert self.campaign_page.find(locator=CampaignPageLocators.LOCATOR_CREATED_CAMPAIGN).text[
               7:] == CampaignPageLocators.campaign_name
        assert CampaignPageLocators.campaign_name in self.driver.page_source

        self.campaign_page.delete_campaign()

    def test_segment_create_delete(self):
        self.login_page.login(user=creds[0], password=creds[1])
        self.segment_page.click(locator=BasePageLocators.LOCATOR_SEGMENTS)
        self.segment_page.create_game_data_sources(game_url=GAME_URL)
        self.segment_page.create_segment(checkbox_locator=SegmentPageLocators.LOCATOR_GAME_CHECKBOX,
                                         segment_name=SegmentPageLocators.segment_name_1,
                                         segment_type_locator=SegmentPageLocators.LOCATOR_SEGMENT_TYPE_GAMES)

        assert (self.segment_page.find(locator=SegmentPageLocators.LOCATOR_CREATED_SEGMENT_1).text ==
                SegmentPageLocators.segment_name_1)
        assert self.segment_page.find(locator=SegmentPageLocators.LOCATOR_CREATED_SEGMENT_1)
        assert SegmentPageLocators.segment_name_1 in self.driver.page_source

        self.segment_page.delete_segment(
            remove_segment_name=SegmentPageLocators.segment_name_1)

    def test_segment_data_source_create_delete(self):
        self.login_page.login(user=creds[0], password=creds[1])
        self.segment_page.click(locator=BasePageLocators.LOCATOR_SEGMENTS)
        self.segment_page.create_group_data_sources(data_group_url=GROUP_URL)
        self.segment_page.create_segment(checkbox_locator=SegmentPageLocators.LOCATOR_VK_GROUP_CHECKBOX,
                                         segment_name=SegmentPageLocators.segment_name_2,
                                         segment_type_locator=SegmentPageLocators.LOCATOR_SEGMENT_TYPE_GROUPS)

        assert (self.segment_page.find(locator=SegmentPageLocators.LOCATOR_CREATED_SEGMENT_2).text ==
                SegmentPageLocators.segment_name_2)
        assert SegmentPageLocators.segment_name_2 in self.driver.page_source

        self.segment_page.delete_segment(
            remove_segment_name=SegmentPageLocators.segment_name_2)

        assert SegmentPageLocators.segment_name_2 not in self.driver.page_source
        assert SegmentPageLocators.segment_name_2 not in self.driver.page_source

        self.segment_page.delete_data_source(source_name=DATA_SOURCE_NAME)

        assert DATA_SOURCE_NAME not in self.driver.page_source
