from selenium.webdriver.common.by import By


class Loc_Find_AP():

    # Static locators
    TXT_FIND = By.XPATH, "//li[contains(@class,'searchbox')]//input"

    BTN_POD11 = By.XPATH, "//div[contains(@class,'item-selected')]"