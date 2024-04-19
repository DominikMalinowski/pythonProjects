from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_FillBuildOrder_AP import Loc_FillBuildOrder_AP
import time

class PageFillBuildOrder_AP(SeleniumDriver, Loc_FillBuildOrder_AP):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)
    # Action methods

    def PLM_Project(self):
        self.switchToStandardFrame()
        # PLM Project
        self.elementClick(self.DDN_PLM_PROJECT, timeout=10)
        #DZIAŁA NA XPATH# self.setDropdownOptionByText(self.DDN_PLM_PROJECT, value="188901 AHO GPM INF IF DEV")
        self.sendKeys("188901 AHO GPM INF IF DEV", self.DDN_PLM_PROJECT2, timeout=10)
        # if self.waitForElement(self.DDN_PLM_PROJECT4):

        if self.isElementVisible(self.DDN_PLM_PROJECT3, timeout=25):
            self.sendKeys("188901 AHO GPM INF IF DEV", self.DDN_PLM_PROJECT3)

        # Alternate Engineer
        self.elementClick(self.DDN_ALTER_ENGIN, timeout=5)
        self.sendKeys('en01', self.DDN_ALTER_ENGIN2, timeout=5)
        self.elementClick(self.DDN_ALTER_ENGIN3, timeout=10)
        # AFIS Number
        self.elementClick(self.TXT_AFIS_NUM, timeout=5)
        self.sendKeys('apankiewicz', self.TXT_AFIS_NUM, timeout=5)
        # Cost Center
        self.elementClick(self.TXT_COST_CEN, timeout=5)
        self.elementClick(self.TXT_COST_CEN2, timeout=5)
        # End Use Designation- Internal
        self.elementClick(self.RDO_INTER_USE, timeout=10)
        # Category
        self.elementClick(self.DDN_CATEGORY, timeout=5)
        self.sendKeys('a', self.DDN_CATEGORY2, timeout=5)
        self.elementClick(self.DDN_CATEGORY3, timeout=10)
        # Part number
        self.elementClick(self.DDN_PART_NUM, timeout=5)
        if self.isElementVisible(self.DDN_PART_NUM2, timeout=25):
            self.sendKeys('X644146100A-00-02', self.DDN_PART_NUM2)
        # if self.waitForElement(self.DDN_PART_NUM2, timeout=25):
        # self.setDropdownOptionByText('X644146100A-00-02', self.DDN_PART_NUM2)
        self.elementClick(self.DDN_PART_NUM3, timeout=25)
        # Facility
        self.elementClick(self.DDN_FACILITY, timeout=5)
        self.sendKeys('ABR', self.DDN_FACILITY2, timeout=5)
        self.elementClick(self.DDN_FACILITY3, timeout=5)



        self.switchToDefaultContent()

        # //li[@class='select2-results__option select2-results__option--highlighted']