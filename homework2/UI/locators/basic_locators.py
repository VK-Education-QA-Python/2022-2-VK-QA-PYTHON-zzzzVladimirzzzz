from selenium.webdriver.common.by import By
from UI.entity_functions.entity_generation import *


class BasePageLocators:
    LOCATOR_CAMPAIGNS = (By.XPATH, "//*[contains(@class, 'center-module-button') and "
                                   "contains(@class,'center-module-campaigns')]")
    LOCATOR_SEGMENTS = (By.XPATH, "//*[@href='/segments']")


class CampaignPageLocators(BasePageLocators):
    campaign_name = generate_campaign_name(base_campaign_name='Campaign')
    LOCATOR_CONTACTS = (By.XPATH, "//*[@href='/profile/contacts']")
    LOCATOR_SURNAME_INPUT = (By.XPATH, "//*[contains(@class, 'input__inp') and contains(@class,'js-form-element')]")
    LOCATOR_SAVE_PROFILE_BUTTON = (By.XPATH, "//*[contains(@class, 'button') and contains(@class,'button_submit')]")
    LOCATOR_CAMPAIGN_TYPE = (By.XPATH, "//*[contains(@class,'column-list-item _audiolistening')]")
    LOCATOR_NEW_CAMPAIGN = (By.XPATH, "//*[contains(@class,'button-module-button') and "
                                      "contains(@class,'button-module-blue')]")
    LOCATOR_CONTENT_LINK = (By.XPATH, "//*[contains(@class, 'mainUrl-module-searchInput') and "
                                      "contains(@class,'suggester-module-searchInput')]")
    LOCATOR_CAMPAIGN_NAME = (By.XPATH, "//div[@class='input input_campaign-name input_with-close']/"
                                       "div[@class='input__wrap']/input[1]")
    LOCATOR_UPLOAD_PICTURE = (By.XPATH, "//*[@data-test='overlay_500x500']")
    LOCATOR_SAVE_PICTURE_BUTTON = (By.XPATH, "//input[contains(@class,'image-cropper__save js-save')]")
    LOCATOR_UPLOAD_AUDIO = (By.XPATH, "//div[contains(@class,'upload-module-wrapper')]/input[@accept='.mp3']")
    LOCATOR_CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//*[contains(@data-class-name,'Submit') and "
                                                "contains(@data-service-readonly,'true')]")
    LOCATOR_CREATED_CAMPAIGN = (By.XPATH, "//*[@title='{}']".format(campaign_name))
    LOCATOR_FIND_CAMPAIGN = (By.XPATH, "//*[contains(@class,'module-searchInput')]")
    LOCATOR_CONFIRM_FIND = (By.XPATH, "//*[contains(@class,'optionWrap')]")
    LOCATOR_CAMPAIGN_CHECKBOX = (By.XPATH, "//*[contains(@class,'module-campaignNameCell')]/input")
    LOCATOR_CAMPAIGN_MODULE_DELETE = (By.XPATH, "//*[contains(@class,'module-selectItem')]")
    LOCATOR_CAMPAIGN_DELETE_BUTTON = (By.XPATH, "//*[contains(@title,'Удалить') or contains(@title,'Delete')]")


class SegmentPageLocators(BasePageLocators):
    segment_name_1 = generate_segments_name(base_segment_name='Segment1')
    segment_name_2 = generate_segments_name(base_segment_name='Segment2')
    LOCATOR_GAMES = (By.XPATH, "//*[@href='/segments/apps_games_list']")
    LOCATOR_GAME_TYPE = (By.XPATH, "//input[contains(@class,'multiSelectSuggester')]")
    LOCATOR_SELECT_ALL = (By.XPATH, "//div[@data-test='select_all']")
    LOCATOR_ADD_ALL = (By.XPATH, "//*[@data-test='add_selected_items_button']")
    LOCATOR_GROUPS = (By.XPATH, "//*[@href='/segments/groups_list']")
    LOCATOR_INPUT_GROUP = (By.XPATH, "//*[contains(@class,'multiSelectSuggester-module-search')]")
    LOCATOR_SEGMENTS_LIST = (By.XPATH, "//*[@href='/segments/segments_list']")
    LOCATOR_SEGMENT_LIST_INPUT = (By.XPATH, "//*[contains(@class,'input__inp') and "
                                            "contains(@maxlength,60)]")
    LOCATOR_SEGMENT_SUBMIT = (By.XPATH, "//*[@data-class-name='Submit']")
    LOCATOR_ADD_SEGMENTS = (By.XPATH, "//*[@class='button button_submit']")
    LOCATOR_NEW_SEGMENT = (By.XPATH, "//*[@href='/segments/segments_list/new/']")
    LOCATOR_GAME_CHECKBOX = (By.XPATH, "//*[contains(text(),'«СуперСити»')]/../../../input")
    LOCATOR_SEGMENT_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class,'adding-segments-modal')]/button")
    LOCATOR_CREATED_SEGMENT_1 = (By.XPATH, "//*[@title='{}']".format(segment_name_1))
    LOCATOR_CREATED_SEGMENT_2 = (By.XPATH, "//*[@title='{}']".format(segment_name_2))
    LOCATOR_ADD_CHOSEN_GROUP = (By.XPATH, "//*[contains(@class,'button-module-textWrapper')]")
    LOCATOR_SEGMENT_TYPE_GAMES = (By.XPATH, "//div[contains(text(),'Приложения и игры в соцсетях') or "
                                            "contains(text(),'Apps and games in social networks')]")
    LOCATOR_SEGMENT_TYPE_GROUPS = (By.XPATH, "//div[contains(text(),'Группы ОК и VK') or contains(text(),"
                                             "'Groups OK and VK')]")
    LOCATOR_VK_GROUP_CHECKBOX = (By.XPATH, "//input[contains(@class,'adding-segments')]")
    LOCATOR_REMOVE_SOURCE = (By.XPATH, "//*[contains(@class,'remove-source')]")
    LOCATOR_CONFIRM_REMOVE = (By.XPATH, "//*[contains(@class,'confirm-remove button_general')]")
    LOCATOR_FIND_DATA_SOURCE = (By.XPATH, "//*[@data-loc-ru ='Поиск по имени или id ...']")
    LOCATOR_FIND_SEGMENT = (By.XPATH, "//*[contains(@class,' segmentsTable-module-suggester')]")
    LOCATOR_CONFIRM_SEGMENT_FIND = (By.XPATH, f"//*[contains(@class,'optionsList-module-option') and "
                                              "contains(@title,{})]".format(segment_name_2))
    LOCATOR_SEGMENT_CHECKBOX = (By.XPATH, "//*[contains(@class,'dCellWrap')]/input")
    LOCATOR_SELECT_MODULE = (By.XPATH, "//*[contains(@class,'module-selectItem')]")
    LOCATOR_SEGMENT_REMOVE = (By.XPATH, "//*[contains(@data-test,'remove')]")


LOCATOR_LOGIN_MENU = "//*[contains(@class, 'responseHead-module-button')]"
LOCATOR_LOGIN_EMAIL_INPUT = "//*[contains(@class,'authForm-module-input') and contains(@class,'input-module-input')]"
LOCATOR_LOGIN_PASSWORD_INPUT = "//*[contains(@class,'authForm-module-inputPassword')]"
LOCATOR_LOGIN_BUTTON = "//*[contains(@class,'authForm-module-button')]"
