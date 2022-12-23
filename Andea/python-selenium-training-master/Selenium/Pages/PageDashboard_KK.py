from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PageDashboard_KK import Loc_PageDashboard_KK

class PageDashboard_KK(SeleniumDriver, Loc_PageDashboard_KK):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def getDashboardConfirmation(self):
        if self.isElementPresent(self.TXT_HEADER):
            return True
        else:
            return False

    # Click on Menu item

    def clickOn_Dashboard(self):
        self.elementClick(self.BTN_DASHBOARD)

    def clickOn_Updates(self):
        self.elementClick(self.BTN_UPDATES)

    def clickOn_Modules(self):
        self.elementClick(self.BTN_MODULES)

    def clickOn_Accounts(self):
        self.elementClick(self.BTN_ACCOUNTS)

    def clickOn_Accounts_Admins(self):
        self.elementClick(self.BTN_ACCOUNTS_ADMINS)

