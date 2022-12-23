from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_CRC10Page_GS import Loc_CRC10Page_GS


class PageCRC10Page_GS(SeleniumDriver, Loc_CRC10Page_GS):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def fillBarcodeI(self, BarcodeI):
        self.switchToStandardFrame()
        self.sendKeys(BarcodeI, self.TXT_BARDOCODE_I)
        self.switchToDefaultContent()

    def fillBarcodeH(self, barcodeH):
        self.switchToStandardFrame()
        self.sendKeys(barcodeH, self.TXT_BARDOCODE_H)
        self.switchToDefaultContent()

    def fillBarcodeQ(self, barcodeQ):
        self.switchToStandardFrame()
        self.sendKeys(barcodeQ, self.TXT_BARDOCODE_Q)
        self.switchToDefaultContent()

    def fillBatch(self, batch):
        self.switchToStandardFrame()
        self.sendKeys(batch, self.TXT_BATCH)
        self.switchToDefaultContent()

    def clickContinue(self):
        self.switchToStandardFrame()
        self.elementClick(self.BTN_CONTINUE)
        self.switchToDefaultContent()

    def checkPopup(self):
        self.switchToStandardFrame()
        flag = self.areElementsPresent(self.POPUP_ERROR_Q)
        self.switchToDefaultContent()
        return flag
