from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_Find_AP import Loc_Find_AP


class PageFind_AP(SeleniumDriver, Loc_Find_AP):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def fillFind(self):
        self.sendKeys('POD11', self.TXT_FIND, timeout=10)
    def clickPOD11(self):
        self.elementClick(self.BTN_POD11, timeout=10)