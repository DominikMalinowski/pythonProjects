
# import of selenium and webdriver
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass
from pages.shirt_product_page import ShirtProductPage

class LostHatProductPomTest(BaseTestClass):
    def test_check_product_default_size(self):
        expected_product_default_size = 'M'

        product_page = ShirtProductPage(self.conf_driver)
        product_page.visit()
        observed_product_default_size_text = product_page.get_product_size()

        self.assertEqual(expected_product_default_size, observed_product_default_size_text,
                         f"Current size differ from expected. Current size: {observed_product_default_size_text}")

    @screenshot_decorator
    def test_check_product_size_change(self):
        expected_product_changed_size = 'L'
        product_page = ShirtProductPage(self.conf_driver)
        product_page.visit()

        old_size = product_page.get_product_size()
        product_page.change_product_size(expected_product_changed_size)

        new_size = product_page.get_product_size()

        self.assertNotEqual(old_size, new_size ,f'Expected size is the same as actual')