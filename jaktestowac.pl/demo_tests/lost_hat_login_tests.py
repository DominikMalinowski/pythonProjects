# import of selenium and webdriver
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from helpers import funcional_helpers as fh

class LostHatLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.main_page_url = 'https://autodemo.testoneo.com/en/'
        self.login_page_url = 'https://autodemo.testoneo.com/en/login?back=my-account'

    def tearDown(self):
        self.driver.quit()

    def assert_expected_text(self, driver, xpath, expected_text, current_url_page):
        header_element = driver.find_element(By.XPATH, xpath)
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ than actual. Page: {current_url_page}')

    def test_header_element_title(self):
        expected_text = 'Log in to your account'
        xpath = '//*[@id="main"]/header/h1'
        current_url_page = self.main_page_url

        driver = self.driver
        driver.get(self.login_page_url)

        self.assert_expected_text(driver, xpath, expected_text, current_url_page)

    def test_correct_login(self):
        expected_text = 'place holder'
        user_mail = 'mail@mail.com'
        user_pass = 'passwordnigga'
        xpath = '//*[@class="account"]/*[@class="hidden-sm-down"]'
        current_url_page = self.login_page_url

        driver = self.driver
        driver.get(self.login_page_url)

        fh.user_login(driver, user_mail, user_pass)
        self.assert_expected_text(driver, xpath, expected_text, current_url_page)

    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        user_mail = 'dupa@dupa.com'
        user_pass = 'passwordnigga'
        xpath = '//*[@class="alert alert-danger"]'
        current_url_page = self.login_page_url

        driver = self.driver
        driver.get(self.login_page_url)

        fh.user_login(driver, user_mail, user_pass)
        self.assert_expected_text(driver, xpath, expected_text, current_url_page)