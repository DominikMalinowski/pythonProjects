from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_StartPage_AP import Loc_StartPage_AP


class PageStartPage_AP(SeleniumDriver, Loc_StartPage_AP):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def clickStandardLogin(self):
        self.elementClick(self.LNK_STANDARD_LOGIN, timeout=10)