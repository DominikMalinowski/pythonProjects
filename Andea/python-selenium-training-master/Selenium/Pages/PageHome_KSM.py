from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PageHome_KSM import Loc_PageHome_KSM

class PageHome_KSM(SeleniumDriver, Loc_PageHome_KSM):
    """ This class stores all methods that can be used for Home page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def openFlexPartbyKeyword(self, keyword):
        self.sendKeys(keyword, self.TXT_SEARCH)
        self.elementClick(self.BTN_FIRSTROW)
