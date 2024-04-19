from selenium.webdriver.common.by import By


class Loc_PageUpdateAdmin_KK():
    """ This class stores all locators for Update Admin page """

    # Left Menu locators

    TXT_HEADER = By.XPATH, "//div[text()='Update Admin']"

    TXT_FIRST_NAME = By.XPATH, "//input[@placeholder='First name']"

    TXT_LAST_NAME = By.XPATH, "//input[@placeholder='Last name']"

    TXT_EMAIL = By.XPATH, "//input[@placeholder='Email address']"

    TXT_PASSWORD = By.XPATH, "//input[@placeholder='Password']"

    TXT_MOBILE_NUMBER = By.XPATH, "//input[@placeholder='Mobile Number']"

    DDN_COUNTRY = By.XPATH, "//select[@class='chosen-select select2-offscreen']"

    TXT_ADDRESS_1 = By.XPATH, "//input[@placeholder='Full address'][@name='address1']"

    TXT_ADDRESS_2 = By.XPATH, "//input[@placeholder='Full address'][@name='address2']"

    BTN_SUBMIT = By.XPATH, "//button[@class='btn btn-primary btn-block btn-lg']"
