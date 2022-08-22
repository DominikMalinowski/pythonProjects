# import of selenium and webdriver
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from helpers import funcional_helpers as fh


class LostHatSanityTest(unittest.TestCase):
    main_page_url = 'https://autodemo.testoneo.com/en/'

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.art_product_type_page = self.main_page_url + '9-art'
        self.clothes_product_type_page = self.main_page_url + '3-clothes'
        self.accessories_product_type_page = self.main_page_url + '6-accessories'
        self.login_page_url = self.main_page_url + 'login'

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test_is_searching_bar_working(self):
        xpath = '//*[@class="ui-autocomplete-input"]'
        products_xpath = '//*[@class="product-miniature js-product-miniature"]'
        product_name = 'mug'
        search_phrase = 'Today Is A Good Day'
        number_of_correct_results = 0
        expected_number_of_correct_results = 5

        driver = self.driver
        driver.get(self.main_page_url)

        fh.use_search_bar(driver, xpath, product_name)
        products_list = driver.find_elements(By.XPATH, products_xpath)
        for product in products_list:
            if search_phrase in product.text:
                number_of_correct_results += 1
            else:
                continue

        self.assertEqual(number_of_correct_results, expected_number_of_correct_results,
                         f'The number of expected result differ from number of actual results.\n'
                         f'Expected: {expected_number_of_correct_results}\nActual: {number_of_correct_results}')
