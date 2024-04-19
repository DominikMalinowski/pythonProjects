from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PageLogin_djanczy import Loc_PageLogin_djanczy

class PageLogin_djanczy(SeleniumDriver, Loc_PageLogin_djanczy):

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def aprisoLogIn(self, login, password):
        """ Login to Apriso """

        self.sendKeys(login, self.TXT_LOGIN, timeout=2)
        self.sendKeys(password, self.TXT_PASSWORD, timeout=2)
        self.elementClick(self.BTN_LOGIN, timeout=2)
