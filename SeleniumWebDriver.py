
# import of selenium and webdriver
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

    # tearDown - perform after every test
    #def tearDown(self):
        #self.driver.quit()

    # # tearDownClass - perform after everything else
    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

class LostHatTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    # setUp method with pages for test
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.main_page_url = 'https://autodemo.testoneo.com/en/'
        self.login_page_url = 'https://autodemo.testoneo.com/en/login?back=my-account'
        self.product_page_url = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'

    def tearDown(self):
        self.driver.quit()

    # method for checking login into website
    def user_login(self, driver, user_mail, user_pass):
        email_input_field = driver.find_element(By.XPATH, '//*[@type="email"]')
        email_input_field.send_keys(user_mail)

        password_input_field = driver.find_element(By.XPATH, '//*[@type="password"]')
        password_input_field.send_keys(user_pass)

        button_next_element = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
        button_next_element.click()

    # method for checking assertion
    def assert_expected_text(self, driver, xpath, expected_text, current_url_page):
        header_element = driver.find_element(By.XPATH, xpath)
        header_element_text = header_element.text
        self.assertEqual(expected_text,header_element_text, f'Expected text differ than actual. Page: {current_url_page}')

    # test with correct credential and invoking both method from earlier
    def test_correct_login(self):
        expected_text = 'place holder'
        user_mail = 'mail@mail.com'
        user_pass = 'passwordnigga'
        xpath = '//*[@class="account"]/*[@class="hidden-sm-down"]'
        current_url_page = self.login_page_url

        driver = self.driver
        driver.get(self.login_page_url)

        self.user_login(driver, user_mail, user_pass)
        self.assert_expected_text(driver,xpath, expected_text, current_url_page)

    # test with incorrect credential and invoking both method from earlier
    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        user_mail = 'dupa@dupa.com'
        user_pass = 'passwordnigga'
        xpath = '//*[@class="alert alert-danger"]'
        current_url_page = self.login_page_url

        driver = self.driver
        driver.get(self.login_page_url)

        self.user_login(driver, user_mail, user_pass)
        self.assert_expected_text(driver,xpath,expected_text,current_url_page)

    # test with assertion that don't stop on error
    def test_loop_usage(self):
        expected_text_included_in_string = 'star'
        list_of_items = ['stargate', 'starship', 'cat', 'stardust', 'startreck', 'dog']

        for title_element in list_of_items:
            print(f'Text: {title_element}')

        for item in list_of_items:
            with self.subTest(item):
                self.assertIn(expected_text_included_in_string, item, f'Item doesn\'t contain string')