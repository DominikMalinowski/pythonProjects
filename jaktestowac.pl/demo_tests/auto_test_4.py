# import of selenium and webdriver
import time
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LostHatTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.main_page_url = 'https://autodemo.testoneo.com/en/'
        self.login_page_url = 'https://autodemo.testoneo.com/en/login?back=my-account'
        self.product_page_url = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'

    def tearDown(self):
        self.driver.quit()

    def test_header_element_title(self):
        driver = self.driver
        driver.get(self.login_page_url)
        expected_title = 'Log in to your account'
        header_element_title = driver.find_element(By.XPATH, '//*[@id="main"]/header/h1')
        header_element_title_text = header_element_title.text
        self.assertEqual(expected_title,header_element_title_text, f'Actual tile of page is diffrent than expected')

    def test_product_name(self):
        driver = self.driver
        driver.get(self.product_page_url)

        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        product_element_name = driver.find_element(By.XPATH, '//*[@id="main"]//*[@class="h1"]')
        product_element_name_text = product_element_name.text
        self.assertEqual(expected_product_name,product_element_name_text, f'Actual name is diffrent than expected')

    def test_check_product_price(self):
        expected_product_price = 'PLN23.52'
        driver = self.driver
        driver.get(self.product_page_url)

        price_element = driver.find_element(By.XPATH, '//*[@class="current-price"]//*[@itemprop="price"]')
        price_element_text = price_element.text
        self.assertEqual(expected_product_price, price_element_text,
                         f'Expected text differ from actual for page url: {self.product_page_url}')

    def user_login(self, driver, user_mail, user_pass):
        email_input_field = driver.find_element(By.XPATH, '//*[@type="email"]')
        email_input_field.send_keys(user_mail)

        password_input_field = driver.find_element(By.XPATH, '//*[@type="password"]')
        password_input_field.send_keys(user_pass)

        button_next_element = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
        button_next_element.click()

    def test_correct_login(self):
        expected_text = 'place holder'
        user_mail = 'mail@mail.com'
        user_pass = 'passwordnigga'

        driver = self.driver
        driver.get(self.login_page_url)
        self.user_login(driver, user_mail, user_pass)
        error_message = driver.find_element(By.XPATH, '//*[@class="account"]/*[@class="hidden-sm-down"]')
        error_message_text = error_message.text
        self.assertEqual(expected_text, error_message_text,
                         f'Actual account name is diffrent than expected')

    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        user_mail = 'dupa@dupa.com'
        user_pass = 'passwordnigga'

        driver = self.driver
        driver.get(self.login_page_url)
        self.user_login(driver, user_mail, user_pass)

        authentication_error_message = driver.find_element(By.XPATH, '//*[@class="alert alert-danger"]')
        authentication_error_message_text = authentication_error_message.text
        self.assertEqual(authentication_error_message_text, expected_text,
                         f'Actual text is different than expected')
