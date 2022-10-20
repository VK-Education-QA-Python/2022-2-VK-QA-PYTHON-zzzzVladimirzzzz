from UI.pages.base_page import BasePage
from UI.locators.basic_locators import *
from selenium.common.exceptions import TimeoutException


class SegmentPage(BasePage):
    def create_game_data_sources(self, game_url):
        self.click(locator=SegmentPageLocators.LOCATOR_GAMES)
        self.send_keys(locator=SegmentPageLocators.LOCATOR_GAME_TYPE, send_input=game_url)
        self.click(locator=SegmentPageLocators.LOCATOR_SELECT_ALL)
        self.click(locator=SegmentPageLocators.LOCATOR_ADD_ALL)
        self.click(locator=SegmentPageLocators.LOCATOR_SEGMENTS_LIST)

    def create_segment(self, checkbox_locator, segment_name, segment_type_locator):
        self.click(locator=SegmentPageLocators.LOCATOR_SEGMENTS_LIST)
        try:
            self.click(locator=SegmentPageLocators.LOCATOR_NEW_SEGMENT)
        except TimeoutException:
            self.click(locator=SegmentPageLocators.LOCATOR_SEGMENT_SUBMIT)
        self.click(locator=segment_type_locator)
        self.click(locator=checkbox_locator)
        self.click(locator=SegmentPageLocators.LOCATOR_SEGMENT_SUBMIT_BUTTON)
        self.send_keys(locator=SegmentPageLocators.LOCATOR_SEGMENT_LIST_INPUT,
                       send_input=segment_name)
        self.click(locator=SegmentPageLocators.LOCATOR_ADD_SEGMENTS)

    def create_group_data_sources(self, group_url):
        self.click(locator=SegmentPageLocators.LOCATOR_GROUPS)
        self.send_keys(locator=SegmentPageLocators.LOCATOR_INPUT_GROUP, send_input=group_url)
        self.click(locator=SegmentPageLocators.LOCATOR_SELECT_ALL)
        self.click(locator=SegmentPageLocators.LOCATOR_ADD_CHOSEN_GROUP)
