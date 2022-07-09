
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
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title : {title}')
        expected_title = 'Demobank - Bankowość Internetowa - Logowanie'
        self.assertEqual(expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')


    def test_demo_accounts(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/konta.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title : {title}')
        expected_title = 'Demobank - Bankowość Internetowa - Konta'
        self.assertEqual(expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')

    def test_demo_desktop(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/pulpit.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title : {title}')
        expected_title ='Demobank - Bankowość Internetowa - Pulpit'
        self.assertEqual(expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')

    def test_demo_transfer(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title : {title}')
        expected_title = 'Demobank - Bankowość Internetowa - Przelew'
        self.assertEqual(expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')

    #def tearDown(self):
        #self.driver.quit()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

