from selenium.webdriver.common.by import By

class Loc_PageHome_djanczy():
    """ This class stores all locators for TemplateLocators page """

    # Static locators
    TXT_FIND_SCREEN = By.XPATH, "//li[@class='appbar-menu-item apr-searchbox-container']//input"

    DDN_SCREEN_NAME = By.XPATH, "//search-box-item[@class]//strong"

    LOADING = By.XPATH, "//div[@class = 'reveal-modal-bg fade in']"

