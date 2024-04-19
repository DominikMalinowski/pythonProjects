from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_POP20_KSM import Loc_POP20_KSM

class POP20_KSM(SeleniumDriver, Loc_POP20_KSM):
    """ This class stores all methods that can be used for POP-20 screen page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    # Login to Portal
    def login(self, login, password):
        self.switchToStandardFrame()
        self.sendKeys(login, self.TXT_LOGIN, timeout=2)
        self.sendKeys(password, self.TXT_PASSWORD, timeout=2)
        self.elementClick(self.BTN_LOGIN, timeout=2)
        self.switchToDefaultContent()

    # Exit to POP-10
    def exit(self):
        self.switchToStandardFrame()
        self.elementClick(BTN_EXIT)
        self.switchToDefaultContent()

    def checkAddSampleButton(self):
        self.switchToStandardFrame()
        result = self.isElementPresent(self.BTN_ADDSAMPLE)
        self.switchToDefaultContent()
        return result
    # that's one of the case where biult-in with can reduce more than one line
    # now, as we need to be flexible, we are initially switching to standard frame on the beginning
    # if we want to return the value (and that's the case for most of the assertion oriented methods)
    # we need to define variable and assign the value. We can't return result directly, as we need to
    # switch back to default content. If switching method will be packed to with, above example will
    # look sth like that:
    #   def checkAddSampleButton(self):
    #       with self.switchToStandardFrame()
    #       return self.isElementPresent(self.BTN_ADDSAMPLE)