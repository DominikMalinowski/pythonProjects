from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_Login_AP import Loc_Login_AP


class PageLogin_AP(SeleniumDriver, Loc_Login_AP):
    """ This class stores all methods that can be used for Login page """


    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def fillNameTxt(self):
        self.sendKeys('apankiewicz', self.TXT_NAME)
#self.LOGIN_AP
    def fillPassword(self):
        self.sendKeys('253', self.TXT_PASSWORD)
#self.PASSWORD_AP
    def clickLogin(self):
        self.elementClick(self.BTN_LOG_IN)

