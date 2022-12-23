import unittest2
from Selenium.Utilities import Assertions
from Selenium.Utilities import JsonHandler
from Selenium.Utilities.FileHandler import FileHandler
from Selenium.Utilities.DatabaseConnection import DatabaseConnection
from Selenium.Pages.PageTemplatePages import PageTemplatePages
import os
from os.path import dirname
from selenium import webdriver


class test_TemplateTestClass(unittest2.TestCase):
    """ Tests for CreateEditInventory scenario """

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
        cls.test_data = JsonHandler.getDataFromJsonFile("test_TemplateTestClass.json")

        # Creating page objects
        cls.page_template = PageTemplatePages(cls.driver)

        # Log into the system / Open home page
        #lp = LoginPage(cls.driver)
        #lp.login()
        cls.driver.get(cls.base_configuration.URL_HOME_PAGE)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    def test_TemplateTestClass_TC1(self):
        # On the home page, click on the 'Andea Servers' link
        self.page_template.clickAndeaServers()

        # Assert if the page title is correct
        Assertions.addAssertion(actual=self.page_template.getTitle(), expected='andea_servers [wiki]')

        # Assert if description is correct for Solution Version = 'LESMES 3.0'
        Assertions.lastAssertion(actual=self.page_template.getDescriptionForSolutionVersion('LESMES 3.0'),
                                 expected=self.test_data.LESMES_DESCRIPTION,
                                 message="Checking if Description is correct for LESMES 3.0")
