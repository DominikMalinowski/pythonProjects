from selenium.webdriver.common.by import By

class Loc_POP20_KSM():
    """ This class stores all locators for POP-20 screen page """

    # Static locators
    TXT_LOGIN = By.XPATH, "//div[@class='BusinessControlContainer']//input[@type='text' and @class='Text']"
    TXT_PASSWORD = By.XPATH, "//div[@class='BusinessControlContainer']//input[@type='password' and @class='Text']"
    BTN_LOGIN = By.XPATH, "//button[@value='Login']"
    BTN_ADDSAMPLE = By.XPATH, "//button[@class='ToolButton AddSampleButton']"