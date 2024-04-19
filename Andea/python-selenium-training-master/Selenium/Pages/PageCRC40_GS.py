from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_CRC40Page_GS import Loc_CRC40Page_GS


class PageCRC40Page_GS(SeleniumDriver, Loc_CRC40Page_GS):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def inputPrinter(self, printer):
        self.switchToStandardFrame()
        self.sendKeys(printer, self.TXT_PRINTER)
        self.switchToDefaultContent()

