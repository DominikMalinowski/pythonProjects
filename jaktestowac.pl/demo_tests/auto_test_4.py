# import of selenium and webdriver
import time
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainTests(unittest.TestCase):

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

    def test_log_in(self):
        driver = self.driver
        driver.get(self.login_page_url)

        email_input_field = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div[1]/div[1]/input')
        email_input_field.send_keys('mail@mail.com')

        password_input_field = driver.find_element(By.XPATH, '//*[@id="login-form"]/section/div[2]/div[1]/div/input')
        password_input_field.send_keys('passwordnigga', Keys.ENTER)

    def test_product(self):
        driver = self.driver
        driver.get(self.product_page_url)

        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        product_element_name = driver.find_element(By.XPATH, '//*[@id="main"]//*[@class="h1"]')
        product_element_name_text = product_element_name.text
        self.assertEqual(expected_product_name,product_element_name_text, f'Actual name is diffrent than expected')

