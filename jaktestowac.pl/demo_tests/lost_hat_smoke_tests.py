# import of selenium and webdriver
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener
from helpers import funcional_helpers as fh


class LostHatSmokeTest(unittest.TestCase):

    driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
    main_page_url = 'https://autodemo.testoneo.com/en/'

    @classmethod
    def setUpClass(self):
        self.art_product_type_page = self.main_page_url + '9-art'
        self.clothes_product_type_page = self.main_page_url + '3-clothes'
        self.accessories_product_type_page = self.main_page_url + '6-accessories'
        self.login_page_url = self.main_page_url + 'login'

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def get_page_title(self,page):
        self.driver.get(page)
        return self.driver.title

    def title_page_checking(self, page, expected_page_title):
        actual_title = self.get_page_title(page)
        self.assertEqual(expected_page_title, actual_title,
                         f'For page: {self.main_page_url} actual title is difrent than expected title.')

    def test_mainpage_exist(self):
        expected_page_title = 'Lost Hat'
        self.title_page_checking(self.main_page_url, expected_page_title)

    def test_is_art_section_exist(self):
        expected_page_title = 'Art'
        self.title_page_checking(self.art_product_type_page, expected_page_title)

    def test_is_cloth_section_exist(self):
        expected_page_title = 'Clothes'
        self.title_page_checking(self.clothes_product_type_page, expected_page_title)

    def test_is_accesories_section_exist(self):
        expected_page_title = 'Accessories'
        self.title_page_checking(self.accessories_product_type_page, expected_page_title)

    def test_is_login_section_exist(self):
        expected_page_title = 'Login'
        self.title_page_checking(self.login_page_url, expected_page_title)

    def test_is_searching_bar_working(self):
        xpath = '//*[@class="ui-autocomplete-input"]'
        products_xpath = '//*[@class="product-miniature js-product-miniature"]'
        product_name = 'mug'
        expected_number_of_products = 1

        driver = self.driver
        driver.get(self.main_page_url)

        fh.use_search_bar(driver, xpath, product_name)
        number_of_products_on_page = len(driver.find_elements(By.XPATH, products_xpath))

        assert number_of_products_on_page >= expected_number_of_products, \
            f'On page {driver.current_url} there is less products for "{product_name}" ' \
            f'than expected - expected amount of products: {number_of_products_on_page}'


