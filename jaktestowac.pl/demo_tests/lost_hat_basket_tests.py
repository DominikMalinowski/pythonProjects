# import of selenium and webdriver
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class LostHatBaskettTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.art_page_url = 'https://autodemo.testoneo.com/en/9-art'

    def tearDown(self):
        self.driver.quit()

    def assert_expected_text(self, driver, xpath, expected_text, current_url_page):
        header_element = driver.find_element(By.XPATH, xpath)
        header_element_text = header_element.text
        self.assertEqual(expected_text,header_element_text, f'Expected text differ than actual. Page: {current_url_page}')

    def test_product_name(self):

        item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        add_to_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        confirmation_pop_up_element = '//*[@id="myModalLabel"]'
        expected_text = 'Product successfully added to your shopping cart'

        driver = self.driver
        driver.get(self.art_page_url)

        item = driver.find_element(By.XPATH, item_xpath)
        item.click()

        add_to_cart_button = driver.find_element(By.XPATH, add_to_cart_button_xpath)
        add_to_cart_button.click()

        time.sleep(3)

        confirmation_pop_up_header_element = driver.find_element(By.XPATH, confirmation_pop_up_element)
        self.assertEqual(expected_text, confirmation_pop_up_header_element.text)





