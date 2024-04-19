
from selenium.webdriver.common.by import By


class Loc_CRC10Page_GS():
    """ This class stores all locators for TemplateLocators page """

    # Static locators

    TXT_BARDOCODE_I = By.XPATH, "//div[1]/div[3][@class = 'HorizontalLayout']//input"

    TXT_BARDOCODE_H = By.XPATH, "//div[1]/div[4][@class = 'HorizontalLayout']//input"

    TXT_BARDOCODE_Q = By.XPATH, "//div[1]/div[5][@class = 'HorizontalLayout']//input"

    TXT_BATCH = By.XPATH, "//div[1]/div[6][@class = 'HorizontalLayout']//input"

    BTN_CONTINUE = By.XPATH, "//span[@class='numericBox']/table//td[2]/a "


#TODO
    # do poprawy
    POPUP_ERROR_Q = By.XPATH, "//*[@id=\"GPh\"]/div[2]/div/span[2]"
    # POPUP_ERROR_H = By.XPATH, "//*[@class=\"ErrorMessage\"]"//span[@class='numericBox']/span/table/tbody/tr/td[2]