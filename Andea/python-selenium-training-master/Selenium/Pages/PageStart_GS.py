from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_StartPage_GS import Loc_StartPage_GS


class PageStart_GS(SeleniumDriver, Loc_StartPage_GS):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def clickLogInToDelmia(self):
        self.elementClick(self.BTN_LOG_INT_TO_DELMIA)
