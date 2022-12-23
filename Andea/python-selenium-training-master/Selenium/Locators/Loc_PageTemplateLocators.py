from selenium.webdriver.common.by import By

class Loc_PageTemplateLocators():
    """ This class stores all locators for TemplateLocators page """

    # Static locators
    LNK_ANDEA_SERVERS = By.XPATH, "//div[@class='content']//ul[1]/li[1]//a"

    # Dynamic locators
    def LBL_DESCRIPTION_DYNAMIC(self, solution_version):
        return By.XPATH, "//td[contains(text(), '" + solution_version + "')]/parent::tr/td[5]"

