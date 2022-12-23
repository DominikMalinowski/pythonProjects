from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_Login1Page_GS import Loc_Login1Page_GS


class PageLogin1_GS(SeleniumDriver, Loc_Login1Page_GS):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def clickStandardLogin(self):
        self.elementClick(self.BTN_STANDARD_LOGIN)