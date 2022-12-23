from selenium.webdriver.common.by import By

class Loc_SLOC10_GS():
    """ This class stores all locators for TemplateLocators page """

    # Static locators
    #TXT_LOCATION = By.XPATH, "//div//*[@class=\"VerticalLayout\"]//*[@type='text']"

    TXT_LOCATION = By.XPATH, "//input[@class='Text']"

    BTN_NTM_PALLET = By.XPATH, "//span[@class='numericBox']/span/table/tbody/tr/td[2]"

