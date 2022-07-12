
# import of selenium and webdriver
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title : {title}')
        expected_title = 'Demobank - Bankowość Internetowa - Logowanie'
        self.assertEqual(expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')

    # test 2
    def test_demo_login_2(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        # finding element and taking text from it
        login_form_header_element = driver.find_element(By.XPATH, '//*[@id="login_form"]/h1')
        print(f'Login form header text: {login_form_header_element.text}')

        # finding element and providing value for it
        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.send_keys('Kiczur123')
        print(f'Value for input box after \'send keys\': {login_input_element.get_attribute("value")}')

        # clearing finded element
        login_input_element.send_keys(Keys.BACKSPACE)
        login_input_element.clear()

        # getting atribute of element
        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        login_next_button_element_disabled = login_next_button_element.get_attribute('disabled')
        print(f'Disabled value {login_next_button_element_disabled}')

        #getting property of attribute
        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        login_next_button_element_disabled_property = login_next_button_element.get_property('disabled')
        print(f'Is boolean True? {login_next_button_element_disabled_property == True}')

        # clicking the button
        login_reminder_element = driver.find_element(By.XPATH, '//*[@id="ident_rem"]')
        login_reminder_element_use = login_reminder_element.click()

        # closing the pop up (after 2s wait)
        time.sleep(2)
        closing_button = driver.find_element(By.XPATH, '//*[@id="shadowbox"]/div/i')
        closing_button_use = closing_button.click()

        # exercise 2
        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.send_keys('123456789', Keys.ENTER)
        new_value = login_input_element.get_attribute("value")
        print(new_value)

    # tearDown - perform after every test
    #def tearDown(self):
        #self.driver.quit()

    # # tearDownClass - perform after everything else
    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()