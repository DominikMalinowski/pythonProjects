from selenium.webdriver.common.by import By

class Loc_PageHome_KSM():
    """ This class stores all locators for Home page """

    # Static locators
    TXT_SEARCH = By.XPATH, "//li[@class='appbar-menu-item apr-searchbox-container']//input"
    BTN_FIRSTROW = By.XPATH, "//li[@class='appbar-menu-item apr-searchbox-container']//div[@class='item-line-name ng-binding']"
