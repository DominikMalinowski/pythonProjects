from selenium.webdriver.common.by import By

class Loc_PagePRC202_djanczy():
    """ This class stores all locators for TemplateLocators page """

    # Static locators
    FRA_PRC202 = By.XPATH, "//iframe[@class='apr-fullscreen-tab']"

    BTN_ADD_LOT = By.XPATH, "//button[@class = 'ToolButton AddEmpty']"

    TBL_LOTS = By.XPATH, "//*[@external-value]"

    BTN_GENERATE_LOT_NO = By.XPATH, "//button[@data-field = 'generatelotno']"

    BTN_PRINT_NOW = By.XPATH, "//button[@data-field = 'printnow']"

    TXT_LOT_NO = By.XPATH, "//input[@data-field = 'lotno']"

    BTN_REMOVE = By.XPATH, "//button[@data-field = 'remove']"

    BTN_BACK = By.XPATH, "//a[@class='apr-header-action back no-icon']"
