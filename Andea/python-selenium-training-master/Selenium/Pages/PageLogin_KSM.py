from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PageLogin_KSM import Loc_PageLogin_KSM

class PageLogin_KSM(SeleniumDriver, Loc_PageLogin_KSM):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def login(self, login, password):
        self.sendKeys(login, self.TXT_LOGIN, timeout=2)
        self.sendKeys(password, self.TXT_PASSWORD, timeout=2)
        self.elementClick(self.BTN_LOGIN, timeout=2)
