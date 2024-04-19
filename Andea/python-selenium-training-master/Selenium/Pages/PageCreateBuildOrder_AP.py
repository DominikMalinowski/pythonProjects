from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_CreateBuildOrder_AP import Loc_CreateBuildOrder_AP


class PageCreateBuildOrder_AP(SeleniumDriver, Loc_CreateBuildOrder_AP):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)
    # Action methods

    def clickCreateBuildOrder(self):
        self.switchToStandardFrame()
        if self.isElementVisible(self.BTN_CREATE_BUILD_ORDER, timeout=25):
            self.elementClick(self.BTN_CREATE_BUILD_ORDER)
        self.switchToDefaultContent()