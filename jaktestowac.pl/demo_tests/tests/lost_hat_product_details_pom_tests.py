
import time

from selenium.webdriver.support.select import Select

from helpers.base_test_class import BaseTestClass
from helpers.wrappers import screenshot_decorator
from pages.product_page import ProductPage


class LostHatProductDetailsTests(BaseTestClass):
    @screenshot_decorator
    def test_check_product_default_size(self):
        expected_product_default_size = 'M'

        product_page = ProductPage(self.conf_driver)
        product_page.visit()

        current_product_size = product_page.current_product_size_xpath
        product_size_select = Select(current_product_size)
        observed_product_default_size_text = product_size_select.first_selected_option.text

        self.assertEqual(observed_product_default_size_text, expected_product_default_size,
                         f'Actual size differ from expected. Actual size: {current_product_size}')

    @screenshot_decorator
    def test_check_product_size_change(self):
        expected_product_changed_size = 'L'
        product_page = ProductPage(self.conf_driver)
        product_page.visit()

        current_product_size = product_page.current_product_size_xpath
        product_size_select = Select(current_product_size)
        observed_product_default_size_text = product_size_select.first_selected_option.text
        product_size_select.select_by_visible_text(expected_product_changed_size)
        observed_product_size_changed_text = product_size_select.first_selected_option.text

        self.assertNotEqual(expected_product_changed_size, observed_product_default_size_text,
                            f'Expected size is the same as actual')
        self.assertEqual(observed_product_default_size_text, observed_product_size_changed_text,
                         f'Actual size differ from expected. Actual size: {current_product_size}')
