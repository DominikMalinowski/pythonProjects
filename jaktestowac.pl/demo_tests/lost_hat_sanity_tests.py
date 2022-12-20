# import of selenium and webdriver
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from helpers import funcional_helpers as fh
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from helpers.screenshot_listener import ScreenshotListener
from helpers.wrappers import screenshot_decorator

import config_reader as cr

class LostHatSanityTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        config = cr.load()
        self.base_url = config["base_url"]
        driver = webdriver.Chrome(service=Service(executable_path=config["chromedriver_path"]))

        self.conf_driver = EventFiringWebDriver(driver, ScreenshotListener())
        self.art_product_type_page = self.base_url + '9-art'
        self.clothes_product_type_page = self.base_url + '3-clothes'
        self.accessories_product_type_page = self.base_url + '6-accessories'
        self.login_page_url = self.base_url + 'login'

    @classmethod
    def tearDownClass(self):
        self.conf_driver.close()

    @screenshot_decorator
    def test_is_searching_bar_working(self):
        xpath = '//*[@class="ui-autocomplete-input"]'
        products_xpath = '//*[@class="product-miniature js-product-miniature"]'
        product_name = 'mug'
        search_phrase = 'Today Is A Good Day'
        number_of_correct_results = 0
        expected_number_of_correct_results = 5

        driver = self.conf_driver
        driver.get(self.base_url)

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
