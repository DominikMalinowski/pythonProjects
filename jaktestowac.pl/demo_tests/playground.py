# import of selenium and webdriver
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainTests(unittest.TestCase):

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
        self.assertEqual (expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')

        login_form_header_element = driver.find_element(By.XPATH, '//*[@id="login_form"]/h1')
        # login_form_header_element = driver.find_element(By.XPATH, '//*[@id="login_form_lolcat"]/h1')
        print(f'Login form header text: {login_form_header_element.text}')

        login_input_element = driver.find_element(By.XPATH,'//*[@id="login_id"]')
        print(f'Initial value for input box: {login_input_element.get_attribute("value")}')

        login_input_element.send_keys('Kiczur123')
        print(f'Value for input box after \'send keys\': {login_input_element.get_attribute("value")}')

        login_input_element.clear()
        # login_input_element.send_keys(Keys.BACKSPACE)
        print(f'Value for input box after clear: {login_input_element.get_attribute("value")}')



    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()
