from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_MainPage_GS import Loc_MainPage_GS
from selenium.webdriver.common.keys import Keys


class PageMain_GS(SeleniumDriver, Loc_MainPage_GS):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def fillSearch(self, createContainer):
        self.sendKeys(createContainer, self.TXT_SEARCH)

    def clickSearch(self):
        self.elementClick(self.TXT_SEARCH)

    def clickEnter(self):
        self.sendKeys(Keys.RETURN, self.BTN_CONTAINER)

    def clickCreateContainer(self):
        self.elementClick(self.BTN_CONTAINER)
