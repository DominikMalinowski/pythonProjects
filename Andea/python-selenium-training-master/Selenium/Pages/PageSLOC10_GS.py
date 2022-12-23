from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_SLOC10_GS import Loc_SLOC10_GS
from Selenium import Base
import json


class PageSLOC10_GS(SeleniumDriver, Loc_SLOC10_GS):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
  #  def clickPALLET5(self):
   #      self.elementClick(self.BTN_778PALLET5)

    def fillLocation(self, location):
        self.switchToStandardFrame()
        self.sendKeys(location, self.TXT_LOCATION)
        self.switchToDefaultContent()

    def clickNTM_PALLET_8(self):
        self.switchToStandardFrame()
        self.elementClick(self.BTN_NTM_PALLET)
        self.switchToDefaultContent()

