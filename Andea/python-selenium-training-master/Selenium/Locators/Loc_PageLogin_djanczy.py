from selenium.webdriver.common.by import By

class Loc_PageLogin_djanczy():
    """ This class stores all locators for TemplateLocators page """

    # Static locators
    TXT_LOGIN = By.XPATH, "//input[@name='ctl04$LoginTextBox']"
    TXT_PASSWORD = By.XPATH, "//input[@name='ctl04$PasswordTextbox']"
    BTN_LOGIN = By.XPATH, "//input[@name='ctl04$LogInButton']"


