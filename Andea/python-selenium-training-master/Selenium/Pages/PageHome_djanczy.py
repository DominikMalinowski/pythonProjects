import time
from selenium.webdriver.common.keys import Keys
from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PageHome_djanczy import Loc_PageHome_djanczy


class PageHome_djanczy(SeleniumDriver, Loc_PageHome_djanczy):

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def findScreen(self, screen_name):
        """ Find screen PCR10 in search engine """

        time.sleep(0.5)

        ''' Wait until loading of the page is finished '''
        loading_page = self.isElementPresent(self.LOADING, timeout=0.5)
        while loading_page is True:
            loading_page = self.isElementPresent(self.LOADING, timeout=0.5)

        ''' Enter name of the screen and click ENTER'''
        self.sendKeys(screen_name, self.TXT_FIND_SCREEN)
        time.sleep(0.5)
        self.sendKeys(Keys.ENTER, self.TXT_FIND_SCREEN)



