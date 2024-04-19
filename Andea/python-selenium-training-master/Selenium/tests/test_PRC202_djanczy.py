from Selenium.Utilities import JsonHandler
from Selenium.Utilities.FileHandler import FileHandler
from Selenium.Pages.PageLogin_djanczy import PageLogin_djanczy
from Selenium.Pages.PageHome_djanczy import PageHome_djanczy
from Selenium.Pages.PagePRC10_djanczy import PagePRC10_djanczy
from Selenium.Pages.PagePRC202_djanczy import PagePRC202_djanczy
from Selenium.Utilities.Assertions import *

import unittest2
import os
from os.path import dirname
from selenium import webdriver



class test_PRC202_djanczy(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):

        # Creating Selenium WebDriver
        driverLocation = dirname(dirname(__file__)) + "\\Base\\SeleniumDrivers\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        cls.driver = webdriver.Chrome(driverLocation)
        cls.driver.maximize_window()

        # Management objects
        cls.file_handler = FileHandler()

        # Getting test data from json file
        cls.base_configuration = JsonHandler.getDataFromJsonFile("BaseConfiguration.json")
        cls.test_data = JsonHandler.getDataFromJsonFile("test_PRC202_djanczy.json")

        # Creating page objects
        cls.PageLogin_djanczy = PageLogin_djanczy(cls.driver)
        cls.PageHome_djanczy = PageHome_djanczy(cls.driver)
        cls.PagePRC10_djanczy = PagePRC10_djanczy(cls.driver)
        cls.PagePRC202_djanczy = PagePRC202_djanczy(cls.driver)

        # Log into the system / Open home page
        cls.driver.get(cls.base_configuration.URL_HOME_PAGE_DJANCZY)

    @classmethod
    def tearDownClass(cls):

        cls.driver.close()


    def test_PRC202_djanczy(self):

        # Login to Apriso
        self.PageLogin_djanczy.aprisoLogIn(self.base_configuration.LOGIN_DJANCZY, self.base_configuration.PASSWORD_DJANCZY)

        # Open screen PRC10
        self.PageHome_djanczy.findScreen(self.test_data.SCREEN_NAME)

        # Switch to iframe for Page PCR10
        self.PagePRC10_djanczy.switchToIframe()

        # Remove all filters
        self.PagePRC10_djanczy.removeAllFilters()

        # Filter orders by part no
        self.PagePRC10_djanczy.filterOrders(self.test_data.PART_NO)

        # Select proper order and go to PRC202 page
        self.PagePRC10_djanczy.selectOrder()

        # Switch from the iframe Page PCR10
        self.PagePRC10_djanczy.switchToDefault()

        # Switch to iframe Page PCR202
        self.PagePRC202_djanczy.switchToIframe()

        # Add another Lot
        self.PagePRC202_djanczy.addAnotherLot()

        # Generate Lot No
        self.PagePRC202_djanczy.generateLotNo()

        # Check the Lot No
        self.PagePRC202_djanczy.checkLotNo()

        # Add another Lot
        self.PagePRC202_djanczy.addAnotherLot()

        # Remove chosen lot
        self.PagePRC202_djanczy.removeLot()

        # Go back to PRC10
        self.PagePRC202_djanczy.goBack()

        # Switch from iframe for Page PCR202
        self.PagePRC202_djanczy.switchToDefault()

        # Switch to iframe for Page PCR10
        self.PagePRC10_djanczy.switchToIframe()

        # Remove Part No filter
        self.PagePRC10_djanczy.removePartNoFilter()

        # Logout
        self.PagePRC10_djanczy.logout()

        # Switch from iframe for Page PCR10
        self.PagePRC10_djanczy.switchToDefault()



