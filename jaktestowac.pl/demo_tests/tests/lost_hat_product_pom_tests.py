# import of selenium and webdriver
import time
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass
from pages.shirt_product_page import ShirtProductPage


class LostHatProductPomTest(BaseTestClass):

    @screenshot_decorator
    def test_product_name(self):
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        product_page = ShirtProductPage(self.conf_driver)
        product_page.visit()
        product_name = product_page.get_product_name()

        self.assertEqual(product_name, expected_text,
                         f'Actual producct name differs from expected. Actual product name: {product_name}')

    @screenshot_decorator
    def test_check_product_price(self):
        expected_text = 'PLN23.52'
        product_page = ShirtProductPage(self.conf_driver)
        product_page.visit()
        product_price = product_page.get_product_price()
        time.sleep(3)

        self.assertEqual(expected_text, product_price,
                         f"Actual price differ from expected. Actual price: {product_price}")



