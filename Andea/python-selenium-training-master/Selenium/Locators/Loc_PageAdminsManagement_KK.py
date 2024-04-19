from selenium.webdriver.common.by import By


class Loc_PageAdminsManagement_KK():
    """ This class stores all locators for Admins Management page """

    # Menu locators

    TXT_HEADER = By.XPATH, "//div[@class='panel-heading']"

    BTN_ADD = By.XPATH, "//button[@type='submit']"

    BTN_PRINT = By.XPATH, "//a[@data-task='print']"

    BTN_EXPORT = By.XPATH, "//a[@data-task='csv']"

    BTN_DELETE_SELECTED = By.XPATH, "//button[@id='deleteAll']"

    CHK_SELECT_ALL = By.XPATH, "//input[@onchange='select_all_data(this)']"

    BTN_LOGOUT = By.XPATH, "//i[@class='fa fa-sign-out']"

    # New Admin Locator (dynamic)

    def TXT_EMAIL_DYNAMIC(self, email):
        return By.XPATH, "//td/a[contains(text(), '" + email + "')]"

    def BTN_EDIT(self, email):
        return By.XPATH, "//a[contains(text(), '" + email + "')]//parent::td//following-sibling::td[@class='xcrud-current xcrud-actions xcrud-fix']//a[@title='Edit']"