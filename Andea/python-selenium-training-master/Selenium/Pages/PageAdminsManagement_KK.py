from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
import time
from selenium.webdriver.common.keys import Keys
from Selenium.Locators.Loc_PageAdminsManagement_KK import Loc_PageAdminsManagement_KK

class PageAdminsManagement_KK(SeleniumDriver, Loc_PageAdminsManagement_KK):
    """ This class stores all methods that can be used for Admins Management page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def getAdminsManagementConfirmation(self):
        if self.isElementPresent(self.TXT_HEADER):
            return True
        else:
            return False

    def isAdminCreted(self, email):
        if self.isElementPresent(self.TXT_EMAIL_DYNAMIC(email)):
            return True
        else:
            return False


    # Click on item

    def clickOn_Add(self):
        self.isElementPresent(self.BTN_ADD)
        self.elementClick(self.BTN_ADD)
        self.elementClick(self.BTN_ADD)

    def clickOn_Print(self):
        self.elementClick(self.BTN_PRINT)

    def clickOn_Export(self):
        self.elementClick(self.BTN_EXPORT)

    def clickOn_DeleteSelected(self):
        self.elementClick(self.BTN_DELETE_SELECTED)
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        time.sleep(2)

    def clickOn_Edit(self, email):
        self.elementClick(self.BTN_EDIT(email))

    def clickOn_Logout(self):
        self.elementClick(self.BTN_LOGOUT)

    # Click on checkbox
    def clickOn_Checkbox(self):
        time.sleep(1)
        self.elementClick(self.CHK_SELECT_ALL)



