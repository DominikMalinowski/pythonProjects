import unittest2
from Selenium.Utilities import Assertions
import Selenium.Utilities.Utilities_KSM as KSM
from Selenium.Utilities import JsonHandler
from Selenium.Utilities.FileHandler import FileHandler
from Selenium.Utilities.DatabaseConnection import DatabaseConnection
from Selenium.Pages.PageLogin_KSM import PageLogin_KSM
from Selenium.Pages.PageHome_KSM import PageHome_KSM
from Selenium.Pages.POP10_KSM import POP10_KSM
from Selenium.Pages.POP20_KSM import POP20_KSM
import os
from os.path import dirname
from selenium import webdriver


class test_PrimaryOperatorPortal_KSM(unittest2.TestCase):
    """ Tests for Primary OP scenario """

    @classmethod
    def setUpClass(cls):
        # Creating Selenium WebDriver
        driverLocation = dirname(dirname(__file__)) + "\\Base\\SeleniumDrivers\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverLocation
        cls.driver = webdriver.Ie(driverLocation)
        cls.driver.maximize_window()

        # Management objects
        cls.db_connection = DatabaseConnection()
        cls.file_handler = FileHandler()

        # Getting test data from json file
        cls.base_configuration = JsonHandler.getDataFromJsonFile("BaseConfiguration.json")
        cls.test_data = JsonHandler.getDataFromJsonFile("test_PrimaryOperatorPortal_KSM.json")

        # Creating page objects
        cls.PageLogin_KSM = PageLogin_KSM(cls.driver)
        cls.PageHome_KSM = PageHome_KSM(cls.driver)
        cls.POP10_KSM = POP10_KSM(cls.driver)
        cls.POP20_KSM = POP20_KSM(cls.driver)

        # Log into the system / Open home page
        #lp = LoginPage(cls.driver)
        #lp.login()
        cls.driver.get(cls.base_configuration.KSM_URL_HOME_PAGE)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    def test_PrimaryOperatorPortal_KSM(self):
        # Login to Apriso
        self.PageLogin_KSM.login(self.base_configuration.KSM_LOGIN, self.base_configuration.KSM_PASSWORD)

        # Choose proper Menu Item
        self.PageHome_KSM.openFlexPartbyKeyword(self.test_data.KSM_INITIALFLEXPART)

        # Load list of work centers that should be visible. This is Pyobdc.row object
        row_work_center = self.db_connection.select(JsonHandler.getDatabaseStatement("POP10_AvailableWorkCenterList"))

        # Create list from pyobdc.Row object
        work_center_list = []
        work_center_list = KSM.convertSingleColumnToList(row_work_center)
        #work_center_list.append("asdasdas") --- for test purpose

        # Create assertion for Work Center buttons
        Assertions.addAssertion(actual = self.POP10_KSM.checkWorkCentersAvailable(work_center_list), expected = str(True))

        # Click on the work center
        self.POP10_KSM.chooseWorkCenter(self.test_data.KSM_POP10WORKCENTER)

        # Login to Portal
        self.POP20_KSM.login(self.base_configuration.KSM_LOGIN, self.base_configuration.KSM_PASSWORD)

        # Last assertion - Check if add sample button is clickable
        Assertions.lastAssertion(actual = str(self.POP20_KSM.checkAddSampleButton()), expected = str(True), message = "Failed.")
