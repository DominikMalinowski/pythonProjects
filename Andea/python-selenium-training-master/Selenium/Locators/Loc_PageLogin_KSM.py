from selenium.webdriver.common.by import By

class Loc_PageLogin_KSM():
    """ This class stores all locators for Login page """

    # Static locators
    TXT_LOGIN = By.NAME, "ctl04$LoginTextBox"
    TXT_PASSWORD = By.NAME, "ctl04$PasswordTextbox"
    BTN_LOGIN = By.NAME, "ctl04$LogInButton"
