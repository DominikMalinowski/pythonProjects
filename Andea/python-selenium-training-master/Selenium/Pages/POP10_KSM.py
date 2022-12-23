from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_POP10_KSM import Loc_POP10_KSM

class POP10_KSM(SeleniumDriver, Loc_POP10_KSM):
    """ This class stores all methods that can be used for POP-10 screen page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    # Enter POP 20 choosing workcenter
    def chooseWorkCenter(self, workcenter):
        self.switchToStandardFrame()
        self.elementClick(self.BTN_WORKCENTER(workcenter), timeout=7)
        self.switchToDefaultContent()

    #Exit and go back to home screen
    def exit(self):
        self.switchToStandardFrame()
        self.elementClick(BTN_EXIT)
        self.switchToDefaultContent()

    #Method for Checking available buttons for workcenters
    #Query for capturing work centers that should be visible is in the DatabaseStatements.json
    #Work centers will be inputted as a list
    def checkWorkCentersAvailable(self, work_center_list):
        self.switchToStandardFrame()
        locatorlist = []

        for work_center in work_center_list:
            locatorlist.append(self.BTN_WORKCENTER(work_center))
        result = self.areElementsPresent(*locatorlist)
        self.switchToDefaultContent()
        return str(result)
        