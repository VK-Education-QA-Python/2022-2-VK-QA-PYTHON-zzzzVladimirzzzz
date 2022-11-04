from UI.locators.basic_locators import *
from UI.pages.base_page import BasePage


class CampaignsPage(BasePage):
    def create_audio_campaign(self, url, file_path_picture, file_path_audio):
        self.click(locator=CampaignPageLocators.LOCATOR_NEW_CAMPAIGN)
        self.click(locator=CampaignPageLocators.LOCATOR_CAMPAIGN_TYPE)
        self.send_keys(locator=CampaignPageLocators.LOCATOR_CONTENT_LINK, send_input=url)
        self.send_keys(locator=CampaignPageLocators.LOCATOR_CAMPAIGN_NAME,
                       send_input=CampaignPageLocators.campaign_name)
        self.file_upload(locator=CampaignPageLocators.LOCATOR_UPLOAD_PICTURE, file_path=file_path_picture)
        self.click(locator=CampaignPageLocators.LOCATOR_SAVE_PICTURE_BUTTON)
        self.file_upload(locator=CampaignPageLocators.LOCATOR_UPLOAD_AUDIO, file_path=file_path_audio)
        self.click(locator=CampaignPageLocators.LOCATOR_CREATE_CAMPAIGN_BUTTON)
        self.find_campaign(
            campaign_name=CampaignPageLocators.campaign_name)

    def find_campaign(self, campaign_name):
        self.send_keys(locator=CampaignPageLocators.LOCATOR_FIND_CAMPAIGN, send_input=campaign_name)
        self.click(locator=CampaignPageLocators.LOCATOR_CONFIRM_FIND)

    def delete_campaign(self):
        self.click(locator=CampaignPageLocators.LOCATOR_CAMPAIGN_CHECKBOX)
        self.click(locator=CampaignPageLocators.LOCATOR_CAMPAIGN_MODULE_DELETE)
        self.click(locator=CampaignPageLocators.LOCATOR_CAMPAIGN_DELETE_BUTTON)
        self.driver.refresh()
