from base import BaseCase
from UI.locators.basic_locators import *
import pytest
import os
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.UI
class TestHomework2(BaseCase):

    def test_campaign_create(self, repo_root):
        url = 'https://www.youtube.com/watch?v=bEab0aZ_9Y4'
        file_path_picture = os.path.join(repo_root, 'UI', 'files', 'picture.jpeg')
        file_path_audio = os.path.join(repo_root, 'UI', 'files', 'audio.mp3')
        self.campaign_page.click(locator=CampaignPageLocators.LOCATOR_NEW_CAMPAIGN)
        self.campaign_page.create_audio_campaign(url=url,
                                                 file_path_audio=file_path_audio,
                                                 file_path_picture=file_path_picture)
        self.campaign_page.click(locator=CampaignPageLocators.LOCATOR_CREATED_CAMPAIGN)

    def test_segment_create(self):
        game_url = "https://ok.ru/games/supercity"
        self.segment_page.click(locator=BasePageLocators.LOCATOR_SEGMENTS)
        try:
            self.segment_page.create_game_data_sources(game_url=game_url)
        except NoSuchElementException:
            print('Such a data source has already been created')

        self.segment_page.create_segment(checkbox_locator=SegmentPageLocators.LOCATOR_GAME_CHECKBOX,
                                         segment_name=SegmentPageLocators.segment_name_1,
                                         segment_type_locator=SegmentPageLocators.LOCATOR_SEGMENT_TYPE_GAMES)
        self.segment_page.click(locator=SegmentPageLocators.LOCATOR_CREATED_SEGMENT_1)
        print(SegmentPageLocators.LOCATOR_CREATED_SEGMENT_1)

    def test_segment_create_delete(self):
        group_url = 'https://vk.com/vkedu'
        segment_name = 'Segment_test' + str(uuid.uuid4())
        self.segment_page.click(locator=BasePageLocators.LOCATOR_SEGMENTS)
        try:
            self.segment_page.create_group_data_sources(group_url=group_url)
        except NoSuchElementException:
            print('Such a data source has already been created')
        self.segment_page.create_segment(checkbox_locator=SegmentPageLocators.LOCATOR_VK_GROUP_CHECKBOX,
                                         segment_name=SegmentPageLocators.segment_name_2,
                                         segment_type_locator=SegmentPageLocators.LOCATOR_SEGMENT_TYPE_GROUPS)
        print(segment_name)
        self.segment_page.click(locator=SegmentPageLocators.LOCATOR_CREATED_SEGMENT_2)
        print(SegmentPageLocators.LOCATOR_CREATED_SEGMENT_2)
