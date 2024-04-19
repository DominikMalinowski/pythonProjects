from selenium.webdriver.common.by import By

class Loc_PageDashboard_KK():
    """ This class stores all locators for Dashboard page """

    # Left Menu locators
    TXT_HEADER = By.XPATH, "//p[@class='serverHeader__title']"

    BTN_DASHBOARD = By.XPATH, "//li/a/i[@class='fa fa-desktop']"

    BTN_UPDATES = By.XPATH, "//li/a/i[@class='fa fa-refresh']"

    BTN_MODULES = By.XPATH, "//li/a/i[@class='fa fa-cube']"

    BTN_ACCOUNTS = By.XPATH, "//li/a/i[@class='fa fa-user-circle']"

    BTN_ACCOUNTS_ADMINS = By.XPATH, "//ul[@ID='ACCOUNTS']/li[1]/a"

    BTN_ACCOUNTS_SUPPLIERS = By.XPATH, "//ul[@ID='ACCOUNTS']/li[2]/a"

    BTN_ACCOUNTS_CUSTOMERS = By.XPATH, "//ul[@ID='ACCOUNTS']/li[3]/a"

    BTN_ACCOUNTS_GUESTCUSTOMERS = By.XPATH, "//ul[@ID='ACCOUNTS']/li[4]/a]"






