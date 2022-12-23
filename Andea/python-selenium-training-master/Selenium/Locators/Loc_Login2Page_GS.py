from selenium.webdriver.common.by import By


class Loc_Login2Page_GS():
    """ This class stores all locators for TemplateLocators page """

    # Static locators
    TXT_NAME = By.XPATH, "//*[@tabindex='1']"

    TXT_PASSWORD = By.XPATH, "//*[@tabindex='2']"

    BTN_LOG_IN = By.XPATH, "//div[@class='LoginButtons controlRow']/input[@tabindex = '6']"

    TAB_TITLE = By.XPATH, "//div[@class='LoginButtons controlRow']"
