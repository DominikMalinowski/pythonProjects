
# import of selenium and webdriver
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

class MainTests(unittest.TestCase):
    # setUp - perform before every test
    def setUp(self):
        pass

    #setUpClass - perform before everything
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    # test 1
    def test_demo_login(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title

    # test 2
    def test_demo_accounts(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/konta.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Konta' == title

    # test 3
    def test_demo_desktop(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/pulpit.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Pulpit' == title

    # test 4
    def test_demo_transfer(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/przelew_nowy_zew.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Przelew' == title

    # tearDown - perform after every test
    #def tearDown(self):
        #self.driver.quit()

    # tearDownClass - perform after everything else
    @classmethod
    def tearDownClass(self):
        self.driver.quit()