import pytest
from base import BaseCase
from UI.locators.basic_locators import *
from UI.files.static_files import *


@pytest.mark.UI
class TestHomework2(BaseCase):
    def test_campaign_create(self, create_picture_path, create_audio_path):
        self.campaign_page.click(locator=CampaignPageLocators.LOCATOR_NEW_CAMPAIGN)
        self.campaign_page.create_audio_campaign(url=youtube_url,
                                                 file_path_audio=create_audio_path,
                                                 file_path_picture=create_picture_path)
        self.campaign_page.find_campaign(campaign_name=CampaignPageLocators.campaign_name)
        assert CampaignPageLocators.campaign_name in self.driver.page_source
        self.campaign_page.delete_campaign()
        assert CampaignPageLocators.campaign_name not in self.driver.page_source

    def test_segment_create(self):
        self.segment_page.click(locator=BasePageLocators.LOCATOR_SEGMENTS)
        self.segment_page.create_game_data_sources(game_url=game_url)
        self.segment_page.create_segment(checkbox_locator=SegmentPageLocators.LOCATOR_GAME_CHECKBOX,
                                         segment_name=SegmentPageLocators.segment_name_1,
                                         segment_type_locator=SegmentPageLocators.LOCATOR_SEGMENT_TYPE_GAMES)
        assert (self.segment_page.find(locator=SegmentPageLocators.LOCATOR_CREATED_SEGMENT_1).text ==
                SegmentPageLocators.segment_name_1)
        self.segment_page.delete_segment(remove_segment_name=SegmentPageLocators.segment_name_1)
        assert SegmentPageLocators.segment_name_2 not in self.driver.page_source

    def test_segment_create_delete(self):
        self.segment_page.click(locator=BasePageLocators.LOCATOR_SEGMENTS)
        self.segment_page.create_group_data_sources(data_group_url=group_url)
        self.segment_page.create_segment(checkbox_locator=SegmentPageLocators.LOCATOR_VK_GROUP_CHECKBOX,
                                         segment_name=SegmentPageLocators.segment_name_2,
                                         segment_type_locator=SegmentPageLocators.LOCATOR_SEGMENT_TYPE_GROUPS)
        assert (self.segment_page.find(locator=SegmentPageLocators.LOCATOR_CREATED_SEGMENT_2).text ==
                SegmentPageLocators.segment_name_2)
        self.segment_page.delete_segment(remove_segment_name=SegmentPageLocators.segment_name_2)
        assert SegmentPageLocators.segment_name_2 not in self.driver.page_source
        self.segment_page.delete_data_source(source_name=data_source_name)
        assert data_source_name not in self.driver.page_source
