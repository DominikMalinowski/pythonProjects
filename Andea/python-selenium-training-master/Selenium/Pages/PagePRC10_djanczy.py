import time

from selenium.webdriver.common.keys import Keys

from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PagePRC10_djanczy import Loc_PagePRC10_djanczy

class PagePRC10_djanczy(SeleniumDriver, Loc_PagePRC10_djanczy):

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def switchToIframe(self):
        ''' Switch to iframe '''
        SeleniumDriver.switchToStandardFrame(self, self.FRA_PRC10)

    def switchToDefault(self):
        ''' Switch back from iframe '''
        SeleniumDriver.switchToDefaultContent(self)

    def filterOrders(self, part_no):
        """ Filter order with proper part number """

        self.elementClick(self.TXT_PARTNO_FILTER)
        self.sendKeys(part_no + Keys.ENTER, self.TXT_PARTNO_FILTER, timeout=2)

    def selectOrder(self):
        """ Select given order and move to Page PRC202 """

        ''' Select order '''
        self.elementClick(self.TAB_ORDER)

        ''' CLick "Receive" button '''
        self.elementClick(self.BTN_RECEIVE)

    def removeAllFilters(self):
        """ Removes all filters """


        ''' Remove Part No '''
        self.sendKeys(Keys.BACK_SPACE, self.TXT_PARTNO_FILTER)

        ''' Remove Tracking Type '''
        self.sendKeys(Keys.BACK_SPACE, self.TXT_TRACKING_FILTER)

        ''' Remove Part Description '''
        self.sendKeys(Keys.BACK_SPACE, self.TXT_PART_DESCRIPTION_FILTER)

        ''' Remove Project Description '''
        self.sendKeys(Keys.BACK_SPACE, self.TXT_PROJECT_DESCRIPTION_FILTER)

        ''' Check if Pyrotechnic filter is set to default '''
        element_attribute = self.getElementAttribute(self.LBL_PYROTECHNIC_FILTER_CHECK, "indeterminate")

        ''' If it is, exit method'''
        if element_attribute is not None:
            return

        ''' If not, click on Pyrotechnic filter until it's set to default '''
        while element_attribute is None:
            time.sleep(0.5)
            self.elementClick(self.LBL_PYROTECHNIC_FILTER_CLICK)
            self.waitForElement(self.LBL_PYROTECHNIC_FILTER_CHECK)
            element_attribute = self.getElementAttribute(self.LBL_PYROTECHNIC_FILTER_CHECK, "indeterminate")


    def removePartNoFilter(self):
        """ Removes Part no filter """

        self.sendKeys(Keys.BACK_SPACE, self.TXT_PARTNO_FILTER)

    def logout(self):
        """ Logout from Apriso """

        ''' Click on the user icon '''
        self.elementClick(self.IMG_USER)

        ''' Logout '''
        self.elementClick(self.LNK_LOGOUT)
