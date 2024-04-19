from selenium.webdriver.common.by import By

class Loc_PageLogin_KK():
    """ This class stores all locators for Login page """

    # Static locators
    TXT_EMAIL = By.XPATH, "//input[@type='text'][@name='email']"

    TXT_PASSWORD = By.XPATH, "//input[@type='password']"

    BTN_LOGIN = By.XPATH, "//button[@type='submit']"



