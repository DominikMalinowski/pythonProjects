
from selenium.webdriver.common.by import By


class Loc_MainPage_GS():
    """ This class stores all locators for TemplateLocators page """

    # Static locators

    TXT_SEARCH = By.XPATH, "//li[3]//input"

    BTN_CONTAINER = By.XPATH, "//li[not(contains(@class, 'ng-hide'))]//div[@class='search-box']/div[2]"
