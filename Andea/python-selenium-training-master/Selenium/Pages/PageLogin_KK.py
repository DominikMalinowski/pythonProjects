from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PageLogin_KK import Loc_PageLogin_KK

class PageLogin_KK(SeleniumDriver, Loc_PageLogin_KK):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def login(self, login, password):
        self.sendKeys(login, self.TXT_EMAIL, timeout=2)
        self.sendKeys(password, self.TXT_PASSWORD, timeout=2)
        self.elementClick(self.BTN_LOGIN, timeout=2)
