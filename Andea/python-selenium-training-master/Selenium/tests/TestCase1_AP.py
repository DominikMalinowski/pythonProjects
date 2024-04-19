import unittest2
from Selenium.Utilities import Assertions
from Selenium.Utilities import JsonHandler
from Selenium.Utilities.FileHandler import FileHandler
from Selenium.Utilities.DatabaseConnection import DatabaseConnection
from Selenium.Pages.PageTemplatePages import PageTemplatePages
import os
from os.path import dirname
from selenium import webdriver
import Base.SeleniumDriver
import time

from Selenium.Pages.PageStartPage_AP import PageStartPage_AP
from Selenium.Pages.PageLogin_AP import PageLogin_AP
# from Selenium.Pages.PageMenuAllArrow_AP import PageMenuAllArrow_AP
from Selenium.Pages.PageFind_AP import PageFind_AP
from Selenium.Pages.PageCreateBuildOrder_AP import PageCreateBuildOrder_AP
from Selenium.Pages.PageFillBuildOrder_AP import PageFillBuildOrder_AP

import pyodbc

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
        cls.driver.get(cls.base_configuration.URL_HOME_PAGE_AP)

        # Creating page objects
        cls.page_start_page_AP = PageStartPage_AP(cls.driver)
        cls.page_login_AP = PageLogin_AP(cls.driver)

        # cls.page_menu_all_arrow_AP = PageMenuAllArrow_AP(cls.driver)
        cls.page_find_AP = PageFind_AP(cls.driver)
        cls.page_create_build_order_AP = PageCreateBuildOrder_AP(cls.driver)
        cls.page_fill_build_order_AP = PageFillBuildOrder_AP(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_TemplateTestClass_TC1(self):

        # Assert if the page title is correct
        # Assertions.addAssertion(actual=self.page_start_page_AP.getTitle(), expected="DELMIA Apriso Portal")
        Assertions.addAssertion(actual=self.page_start_page_AP.getTitle(), expected="DELMIA Apriso 2018")

        # On the home page click on 'Standard Login' button
        self.page_start_page_AP.clickStandardLogin()

        # On the main login page:
        # - fill name
        # - fill password
        # - click 'Login' button

        self.page_login_AP.fillNameTxt()
        self.page_login_AP.fillPassword()
        self.page_login_AP.clickLogin()

        # On the menu page- fill 'Fina a screen...' textbox and click on that tab
        self.page_find_AP.fillFind()
        self.page_find_AP.clickPOD11()

        # On the POD11 screen click on 'Create Build Order' button
        self.page_create_build_order_AP.clickCreateBuildOrder()

        # On the POD20 fill all mandatory fileds and click Add Routing
        self.page_fill_build_order_AP.PLM_Project()
        # Connect to the database
        # conn = pyodbc.connect('DRIVER={SQL Server};'
        #                       'SERVER=qatestSQL1\SQL2016;'
        #                       'DATABASE=TestDB;'
        #                       'Trusted_Connection=yes;')
        #
        # cursor = conn.cursor()
        # cursor.execute('SELECT * FROM db_name.Table WHERE ')

        # for row in cursor:
        #     print(row)

        # act = ActionChains(cls.driver)
        # act.send_keys(Keys.ENTER).perform()
        # # On the menu page- click ALL arrow
        # self.page_menu_all_arrow_AP.clickMenuAllArrow()
        #


        time.sleep(25)