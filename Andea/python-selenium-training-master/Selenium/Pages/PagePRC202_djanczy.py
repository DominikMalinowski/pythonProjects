import time
from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PagePRC202_djanczy import Loc_PagePRC202_djanczy
from Selenium.Utilities.Assertions import *
from datetime import date


class PagePRC202_djanczy(SeleniumDriver, Loc_PagePRC202_djanczy):

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def switchToIframe(self):
        ''' Switch to iframe '''
        SeleniumDriver.switchToStandardFrame(self, self.FRA_PRC202)

    def switchToDefault(self):
        ''' Switch back from iframe '''
        SeleniumDriver.switchToDefaultContent(self)

    def addAnotherLot(self):
        """ Add another Lot to the list """

        ''' Calculate expected number of Lots in "Lot and Quantity" and "Printing" sections after addition '''
        self.waitForElement(self.BTN_GENERATE_LOT_NO)
        expected_lot_quantity = self.getNumberOfElements(self.BTN_GENERATE_LOT_NO) + 1

        self.waitForElement(self.BTN_PRINT_NOW)
        expected_lot_printing = self.getNumberOfElements(self.BTN_PRINT_NOW) + 1

        ''' Click Add button '''
        self.elementClick(self.BTN_ADD_LOT)

        ''' Obtain actual number of Lots in "Lot and Quantity" and "Printing" sections after addition '''
        time.sleep(0.5)

        actual_lots_quantity = self.getNumberOfElements(self.BTN_GENERATE_LOT_NO)
        actual_lots_printing = self.getNumberOfElements(self.BTN_PRINT_NOW)

        ''' Compare expected and actual numbers of Lots '''

        '''When method is used second time last assertion is added'''
        addAssertion(str(actual_lots_quantity), str(expected_lot_quantity))
        addAssertion(str(actual_lots_printing), str(expected_lot_printing))

    def generateLotNo(self):
        """ Generate Lot No for given Lot"""

        time.sleep(0.5)
        ''' Click on the "Generate Lot No" button for Lot on the bottom of the list '''
        element_no = self.getNumberOfElements(self.BTN_GENERATE_LOT_NO) - 1
        self.clickElementFromList(self.BTN_GENERATE_LOT_NO, element_no)


    def checkLotNo(self):
        """ Check if Lot Number is valid"""


        ''' Get today's date '''
        today = date.today()

        ''' Get Lot No from the Lot on the bottom of the list '''
        element_no = self.getNumberOfElements(self.TXT_LOT_NO) - 1
        time.sleep(0.5)
        text = self.getTextFromList(self.TXT_LOT_NO, element_no)

        ''' Compare current date and date from Lot No '''
        date_lotno = text[0:8]
        expected_date = today.strftime("%Y" + "%m" + "%d")
        addAssertion(date_lotno, expected_date)

    def removeLot(self):
        """ Remove Lot from the list """


        ''' Calculate expected number of Lots in "Lot and Quantity" and "Printing" sections after removal '''
        self.waitForElement(self.BTN_REMOVE)
        expected_lot_quantity = self.getNumberOfElements(self.BTN_REMOVE) - 1

        self.waitForElement(self.BTN_PRINT_NOW)
        expected_lot_printing = self.getNumberOfElements(self.BTN_PRINT_NOW) - 1

        ''' Click on "Remove" button '''
        element_no = self.getNumberOfElements(self.BTN_REMOVE)
        self.clickElementFromList(self.BTN_REMOVE, element_no - 1)

        time.sleep(0.5)

        ''' Obtain actual number of Lots in "Lot and Quantity" and "Printing" sections after removal '''
        actual_lots_quantity = self.getNumberOfElements(self.BTN_REMOVE)
        actual_lots_printing = self.getNumberOfElements(self.BTN_PRINT_NOW)

        ''' Compare expected and actual numbers of Lots '''
        addAssertion(str(actual_lots_quantity), str(expected_lot_quantity))
        lastAssertion(str(actual_lots_printing), str(expected_lot_printing), "All PASSED")

    def goBack(self):
        """ Go back to page PCR10 """

        ''' Click Back button '''
        self.elementClick(self.BTN_BACK)

