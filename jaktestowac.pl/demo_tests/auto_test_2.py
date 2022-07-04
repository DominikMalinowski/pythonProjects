
# import of selenium and webdriver
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

class MainTests(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def test_demo_login(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title

    def test_demo_accounts(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/konta.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Konta' == title

    def test_demo_desktop(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/pulpit.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Pulpit' == title

    def test_demo_transfer(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/przelew_nowy_zew.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Przelew' == title

    #def tearDown(self):
        #self.driver.quit()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()