from selenium.webdriver.common.by import By

class Loc_PagePRC10_djanczy():
    """ This class stores all locators for TemplateLocators page """

    # Static locators

    #iframe
    FRA_PRC10 = By.XPATH, "//iframe[@class='apr-fullscreen-tab']"

    # filters
    TXT_TRACKING_FILTER = By.XPATH, "//td[@data-field = 'trackingtype']//input"

    TXT_PARTNO_FILTER = By.XPATH, "//td[@data-field = 'productnumber']//input"

    TXT_PART_DESCRIPTION_FILTER = By.XPATH, "//td[@data-field = 'partdescription']//input"

    TXT_PROJECT_DESCRIPTION_FILTER = By.XPATH, "//td[@data-field = 'projectdescription']//input"

    LBL_PYROTECHNIC_FILTER_CHECK = By.XPATH, "//div[@class='fix']/input[@ data-field='dangerousmaterial']"

    LBL_PYROTECHNIC_FILTER_CLICK = By.XPATH, "//div[@class='fix']/label"

    TAB_ORDER = By.XPATH, "//tr[@data-key = 'MTAwMDAwMzkzfDQ3MDYuMzkwNzUuNjQwOTkuMjEwOTQ=']"

    BTN_RECEIVE = By.XPATH, "//button[@class = 'ToolButton _RECEIVE']"

    # Logout
    IMG_USER = By.XPATH, "//span[@class='apr-header-action user active']"
    LNK_LOGOUT = By.XPATH, "//span[@class='apr-header-action user active']//ul"




