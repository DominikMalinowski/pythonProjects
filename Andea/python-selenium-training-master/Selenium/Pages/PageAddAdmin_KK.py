from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PageAddAdmin_KK import Loc_PageAddAdmin_KK


class PageAddAdmin_KK(SeleniumDriver, Loc_PageAddAdmin_KK):
    """ This class stores all methods that can be used for Add Admin page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Provide new admin data
    def CreateAdmin(self, first_name, last_name, email, password, number, country, address1, address2):
        self.sendKeys(first_name, self.TXT_FIRST_NAME, timeout=2)
        self.sendKeys(last_name, self.TXT_LAST_NAME, timeout=2)
        self.sendKeys(email, self.TXT_EMAIL, timeout=2)
        self.sendKeys(password, self.TXT_PASSWORD, timeout=2)
        self.sendKeys(number, self.TXT_MOBILE_NUMBER, timeout=2)
        self.setDropdownOptionByText(self.DDN_COUNTRY, country, timeout=2)
        self.sendKeys(address1, self.TXT_ADDRESS_1, timeout=2)
        self.sendKeys(address2, self.TXT_ADDRESS_2, timeout=2)
        self.elementClick(self.BTN_SUBMIT, timeout=2)
