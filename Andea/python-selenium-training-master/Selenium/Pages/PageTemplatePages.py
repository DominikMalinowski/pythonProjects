from Selenium.Base.SeleniumDriver import SeleniumDriver
import Selenium.Utilities.Logger as ml
from Selenium.Locators.Loc_PageTemplateLocators import Loc_PageTemplateLocators

class PageTemplatePages(SeleniumDriver, Loc_PageTemplateLocators):
    """ This class stores all methods that can be used for Login page """

    logs = ml.MESlogger()

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)

    # Action methods
    def clickAndeaServers(self):
        self.elementClick(self.LNK_ANDEA_SERVERS)

    def getDescriptionForSolutionVersion(self, solution_version):
        return self.getElementText(self.LBL_DESCRIPTION_DYNAMIC(solution_version))

