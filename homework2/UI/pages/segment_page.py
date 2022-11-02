from selenium.common.exceptions import TimeoutException, NoSuchElementException
from UI.pages.base_page import BasePage
from UI.locators.basic_locators import *


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

    def find_segment(self, segment_name):
        self.send_keys(locator=SegmentPageLocators.LOCATOR_FIND_SEGMENT, send_input=segment_name)
        self.click(locator=SegmentPageLocators.LOCATOR_CONFIRM_SEGMENT_FIND)

    def delete_segment(self, remove_segment_name):
        self.find_segment(segment_name=remove_segment_name)
        self.click(locator=SegmentPageLocators.LOCATOR_SEGMENT_CHECKBOX)
        self.click(locator=SegmentPageLocators.LOCATOR_SELECT_MODULE)
        self.click(locator=SegmentPageLocators.LOCATOR_SEGMENT_REMOVE)
        self.driver.refresh()

    def find_data_source(self, group_name):
        self.send_keys(locator=SegmentPageLocators.LOCATOR_FIND_DATA_SOURCE, send_input=group_name)

    def create_group_data_sources(self, data_group_url):
        try:
            self.click(locator=SegmentPageLocators.LOCATOR_GROUPS)
            self.send_keys(locator=SegmentPageLocators.LOCATOR_INPUT_GROUP, send_input=data_group_url)
            self.click(locator=SegmentPageLocators.LOCATOR_SELECT_ALL)
            self.click(locator=SegmentPageLocators.LOCATOR_ADD_CHOSEN_GROUP, timeout=5)
            self.driver.refresh()
        except NoSuchElementException:
            print('Such a data source has already been created')

    def delete_data_source(self, source_name):
        self.click(locator=SegmentPageLocators.LOCATOR_GROUPS)
        self.find_data_source(group_name=source_name)
        self.click(locator=SegmentPageLocators.LOCATOR_REMOVE_SOURCE)
        self.click(locator=SegmentPageLocators.LOCATOR_CONFIRM_REMOVE)
        self.find(locator=SegmentPageLocators.LOCATOR_INPUT_GROUP)
        self.driver.refresh()
