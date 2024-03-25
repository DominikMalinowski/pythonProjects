# import of selenium and webdriver
import unittest

from selenium.webdriver.common.by import By
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass
from pages.product_page import ProductPage


class LostHatProductPomTest(BaseTestClass):

    @screenshot_decorator
    def test_product_name(self):
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        product_page = ProductPage(self.conf_driver)
        product_page.visit()
        product_name = product_page.get_product_name()

        self.assertEqual(product_name, expected_text,
                         f'Actual producct name differs from expected. Actual product name: {product_name}')

    @screenshot_decorator
    def test_check_product_price(self):
        expected_text = 'PLN23.52'
        product_page = ProductPage(self.conf_driver)
        product_page.visit()
        product_price = product_page.get_product_price()

        self.assertEqual(product_price, expected_text,
                         f"Actual price differ from expected. Actual price: {product_price}")
