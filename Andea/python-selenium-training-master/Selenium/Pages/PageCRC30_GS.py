from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_CRC30Page_GS import Loc_CRC30Page_GS


class PageCRC30Page_GS(SeleniumDriver, Loc_CRC30Page_GS):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def choseQuantity(self):
        self.switchToStandardFrame()
        self.elementClick(self.DDN_QUANTITY_UNIT)
        self.elementClick(self.DDN_QUANTITY_KG)
        self.switchToDefaultContent()

