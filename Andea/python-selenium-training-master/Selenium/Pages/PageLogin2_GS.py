from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_Login2Page_GS import Loc_Login2Page_GS
from Selenium.Utilities import JsonHandler

class PageLogin2_GS(SeleniumDriver, Loc_Login2Page_GS):
    """ This class stores all methods that can be used for Login page """




    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def fillNameTxt(self, login):
        self.sendKeys(login, self.TXT_NAME)

    def fillPassword(self, password):
        self.sendKeys(password, self.TXT_PASSWORD)

    def clickLogin(self):
        self.elementClick(self.BTN_LOG_IN)

