from selenium.webdriver.common.by import By

class Loc_POP10_KSM():
    """ This class stores all locators for POP-10 screen page """

    # Static locators
    BTN_EXIT = By.XPATH, "//button[@value='Exit']//span//span"

    # Dynamic locators
    def BTN_WORKCENTER(self, workcenter):
        return By.XPATH, "//button[@title='"+workcenter+"']"
