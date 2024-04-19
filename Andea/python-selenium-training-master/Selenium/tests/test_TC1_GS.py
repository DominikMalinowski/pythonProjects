import unittest2
from Selenium.Utilities import Assertions
from Selenium.Utilities import JsonHandler
from Selenium.Utilities.FileHandler import FileHandler
from Selenium.Utilities.DatabaseConnection import DatabaseConnection
from Selenium.Pages.PageTemplatePages import PageTemplatePages
from Selenium.Base.SeleniumDriver import SeleniumDriver

from Selenium.Pages.PageStart_GS import PageStart_GS
from Selenium.Pages.PageLogin1_GS import PageLogin1_GS
from Selenium.Pages.PageLogin2_GS import PageLogin2_GS
from Selenium.Pages.PageMain_GS import PageMain_GS
from Selenium.Pages.PageSLOC10_GS import PageSLOC10_GS
from Selenium.Pages.PageCRC10_GS import PageCRC10Page_GS
from Selenium.Pages.PageCRC30_GS import PageCRC30Page_GS
from Selenium.Pages.PageCRC40_GS import PageCRC40Page_GS


import pytest
import time
import os
from os.path import dirname
from selenium import webdriver
import string
import json

class test_TC1_GS(unittest2.TestCase):
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
        cls.base_configuration = JsonHandler.getDataFromJsonFile("test_TC1_GS.json")
        cls.test_data = JsonHandler.getDataFromJsonFile("test_TemplateTestClass.json")

        # Creating page objects
        cls.page_template_GS = PageTemplatePages(cls.driver)
        cls.page_start_GS = PageStart_GS(cls.driver)
        cls.page_login1_GS = PageLogin1_GS(cls.driver)
        cls.page_login2_GS = PageLogin2_GS(cls.driver)
        cls.page_main_GS = PageMain_GS(cls.driver)
        cls.page_SLOC10_GS = PageSLOC10_GS(cls.driver)
        cls.page_CRC10_GS = PageCRC10Page_GS(cls.driver)
        cls.page_CRC30_GS = PageCRC30Page_GS(cls.driver)
        cls.page_CRC40_GS = PageCRC40Page_GS(cls.driver)

        # Log into the system / Open home page
        #lp = LoginPage(cls.driver)
        #lp.login()

        cls.driver.get(cls.base_configuration.GS_URL_HOME_PAGE)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    def test_TC1_GS(self):

        # read some strings from BaseConfiguration.json
        base_configuration = JsonHandler.getDataFromJsonFile("test_TC1_GS.json")

        # Login2Page
        login = base_configuration.GS_LOGIN
        password = base_configuration.GS_PASSWORD

        # MainPage
        createContainer = base_configuration.GS_MAIN_SEARCH_INPUT

        # SLOC10Page
        location = base_configuration.GS_LOCATION

        # CRC10Page
        barcodeI = base_configuration.GS_BARCODE_I
        barcodeH = base_configuration.GS_BARCODE_H
        barcodeQ = base_configuration.GS_BARCODE_Q
        batch = base_configuration.GS_BATCH

        #CRC40Page
        printer = base_configuration.GS_PRINTER









        # On the home page, click on the 'Log in to Delmia' button
        self.page_start_GS.clickLogInToDelmia()

        # Assertion - check if next page title is correct (PageLogin2)
        Assertions.addAssertion(actual=self.page_start_GS.getTitle(), expected='DELMIA Apriso 2017')


        # On the login page, click on the 'Standard login' button
        self.page_login1_GS.clickStandardLogin()

        # Assertion - check if screen Login2Page has been opened
        Assertions.addAssertion(actual=self.page_start_GS.getTitle(), expected='DELMIA Apriso Portal')


        # On the main login2 page:
        # - fill name
        # - fill password
        # - click 'Login' button
        self.page_login2_GS.fillNameTxt(login)
        self.page_login2_GS.fillPassword(password)
        self.page_login2_GS.clickLogin()

        #Assertion - check if screen MainPage has been opened
        #Assertions.addAssertion(actual=self.page_login2_GS.getTitle(), expected='DELMIA Apriso')

        # On the main page:
        # - input 'create container' into searchbox
        # - click on 'create container'
        self.page_main_GS.fillSearch(createContainer)
        self.page_main_GS.clickCreateContainer()

        #Assertion - check if screen SLOC10 has been opened
        Assertions.addAssertion(actual=self.page_login2_GS.areElementsPresent(self.page_login2_GS.TAB_TITLE), expected = True)


        # Page SLOC10
        self.page_SLOC10_GS.fillLocation(location)
        self.page_SLOC10_GS.clickNTM_PALLET_8()

        self.page_CRC10_GS.fillBarcodeI(barcodeI)
        self.page_CRC10_GS.fillBarcodeH(barcodeH)
        self.page_CRC10_GS.fillBarcodeQ(barcodeQ)
        self.page_CRC10_GS.fillBatch(batch)
        self.page_CRC10_GS.clickContinue()

#         time.sleep(4)
#
#         flag = self.page_CRC10_GS.checkPopup()
# #   barcodeQ = base_configuration.GS_BARCODE_Q
#         if flag:
#             temp_barCode = barcodeQ[1:]
#             temp_barCode = int(temp_barCode)
#             temp_barCode +=1
#             barcodeQ = "Q" + str(temp_barCode)
#             with open('C:\\Users\gsamolej\source\\repos\Git\python-selenium-training\Selenium\Configuration\\test_TC1_GS.json', 'r+') as f:
#                 data = json.load(f)
#                 data['GS_BARCODE_Q'] = barcodeQ  # <--- add `id` value.
#                 f.seek(0)  # <--- should reset file position to the beginning.
#                 json.dump(data, f, indent=4)
#                 f.truncate()  # remove remaining part
#
#         print (barcodeQ)

        self.page_CRC10_GS.fillBarcodeQ(barcodeQ)
        self.page_CRC10_GS.clickContinue()

        self.page_CRC30_GS.choseQuantity()

        self.page_CRC40_GS.inputPrinter()



        # Assert if the page title is correct
        Assertions.lastAssertion(actual=self.page_CRC10_GS.getTitle(), expected="DELMIA Apriso", message="test")



        # Assert if description is correct for Solution Version = 'LESMES 3.0'
        # Assertions.lastAssertion(actual=self.page_CRC10_GS.getTitle(),
        #                          expected="DELMIA Apriso",
        #                          message="test")
