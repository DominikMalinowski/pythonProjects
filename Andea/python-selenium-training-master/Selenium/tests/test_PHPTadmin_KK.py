import unittest2
from Selenium.Utilities import Assertions
from Selenium.Utilities import JsonHandler
from Selenium.Utilities.FileHandler import FileHandler
from Selenium.Utilities.DatabaseConnection import DatabaseConnection
from Selenium.Pages.PageLogin_KK import PageLogin_KK
from Selenium.Pages.PageDashboard_KK import PageDashboard_KK
from Selenium.Pages.PageAdminsManagement_KK import PageAdminsManagement_KK
from Selenium.Pages.PageAddAdmin_KK import PageAddAdmin_KK
from Selenium.Pages.PageUpdateAdmin_KK import PageUpdateAdmin_KK
import os
from os.path import dirname
from selenium import webdriver


class test_PHPTadmin_KK(unittest2.TestCase):
    """ Tests for Users management scenario """

    @classmethod
    def setUpClass(cls):
        # Creating Selenium WebDriver
        driverLocation = dirname(dirname(__file__)) + "\\Base\\SeleniumDrivers\\chromedriver.exe"
        # os.environ["webdriver.ie.driver"] = driverLocation
        cls.driver = webdriver.Chrome(driverLocation)
        cls.driver.maximize_window()

        # Management objects
        # cls.db_connection = DatabaseConnection()
        cls.file_handler = FileHandler()

        # Getting test data from json file
        cls.base_configuration = JsonHandler.getDataFromJsonFile("BaseConfiguration.json")
        cls.test_data = JsonHandler.getDataFromJsonFile("test_PHPTadmin_KK.json")

        # Creating page objects
        cls.PageLogin_KK = PageLogin_KK(cls.driver)
        cls.PageDashboard_KK = PageDashboard_KK(cls.driver)
        cls.PageAdminsManagement_KK = PageAdminsManagement_KK(cls.driver)
        cls.PageAddAdmin_KK = PageAddAdmin_KK(cls.driver)
        cls.PageUpdateAdmin_KK = PageUpdateAdmin_KK(cls.driver)

        # Log into the system / Open home page
        # lp = LoginPage(cls.driver)
        # lp.login()
        cls.driver.get(cls.base_configuration.KK_URL_HOME_PAGE)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_PHPTadmin_KK(self):
        # Log in to PHPTravels admin dashboard
        self.PageLogin_KK.login(self.base_configuration.KK_LOGIN, self.base_configuration.KK_PASSWORD)

        # Assert if the page title is correct
        Assertions.addAssertion(actual=str(self.PageDashboard_KK.getDashboardConfirmation()), expected='True')

        # Open Accounts menu and select Admins sub menu
        self.PageDashboard_KK.clickOn_Accounts()
        self.PageDashboard_KK.clickOn_Accounts_Admins()

        # Assert if the page title is correct
        Assertions.addAssertion(actual=str(self.PageAdminsManagement_KK.getAdminsManagementConfirmation()),
                                expected='True')

        # Click on ADD button
        self.PageAdminsManagement_KK.clickOn_Add()

        # Create Admin
        self.PageAddAdmin_KK.CreateAdmin(self.test_data.FIRST, self.test_data.LAST, self.test_data.EMAIL,
                                         self.test_data.PASSWORD, self.test_data.MOBILE, self.test_data.COUNTRY,
                                         self.test_data.ADDRESS1, self.test_data.ADDRESS2)

        # Check if user is created
        Assertions.addAssertion(actual=str(self.PageAdminsManagement_KK.isAdminCreted(self.test_data.EMAIL)),
                                expected='True')

        # Edit Admin data
        self.PageAdminsManagement_KK.clickOn_Edit(self.test_data.EMAIL)
        self.PageUpdateAdmin_KK.UpdateAdmin(self.test_data.FIRST_UPDATED, self.test_data.LAST_UPDATED, self.test_data.EMAIL_UPDATED,
                                         self.test_data.PASSWORD_UPDATED, self.test_data.MOBILE_UPDATED, self.test_data.COUNTRY_UPDATED,
                                         self.test_data.ADDRESS1_UPDATED, self.test_data.ADDRESS2_UPDATED)

        # Check if user is updated
        Assertions.addAssertion(actual=str(self.PageAdminsManagement_KK.isAdminCreted(self.test_data.EMAIL_UPDATED)),
                                expected='True')

        # Logout form admin and login on new created Admin
        self.PageAdminsManagement_KK.clickOn_Logout()
        self.PageLogin_KK.login(self.test_data.EMAIL_UPDATED, self.test_data.PASSWORD_UPDATED)
        Assertions.addAssertion(actual=str(self.PageDashboard_KK.getDashboardConfirmation()), expected='True')

        # Login again on main Admin
        self.PageAdminsManagement_KK.clickOn_Logout()
        self.PageLogin_KK.login(self.base_configuration.KK_LOGIN, self.base_configuration.KK_PASSWORD)

        # Remove created Admin
        self.PageDashboard_KK.clickOn_Accounts()
        self.PageDashboard_KK.clickOn_Accounts_Admins()
        self.PageAdminsManagement_KK.clickOn_Checkbox()
        self.PageAdminsManagement_KK.clickOn_DeleteSelected()

        # Check if Admin user is removed
        Assertions.lastAssertion(actual=str(self.PageAdminsManagement_KK.isAdminCreted(self.test_data.EMAIL_UPDATED)),
                                expected='False', message='Admin has been created and Removed')


