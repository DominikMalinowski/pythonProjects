# import of selenium and webdriver

from selenium.webdriver.common.by import By
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass

class LostHatsFrontPageTests(BaseTestClass):

    @screenshot_decorator
    def test_is_slider_present(self):
        driver = self.conf_driver
        driver.get(self.base_url)

        xpath = '//*[@id="carousel"]'
        slider_element = driver.find_element(By.XPATH, xpath)

    @screenshot_decorator
    def test_slider_minimum_size(self):
        driver = self.conf_driver
        driver.get(self.base_url)

        xpath = '//*[@id="carousel"]'
        expected_min_height = 300
        expected_min_width = 600

        slider_element = driver.find_element(By.XPATH, xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']

        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height,
                            f'Element height for page {self.base_url} is smaller than expected {expected_min_height}')

        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width,
                            f'Element width for page {self.base_url} is smaller than expected {expected_min_width}')

    # @screenshot_decorator
    # def test_slider_contain_exact_number_of_slides(self):
    #     driver = self.conf_driver
    #     driver.get(self.base_url)
    #
    #     expecxted_number_of_slides = 3
    #     xpath = '//*[@id="carousel"]/ul/li'
    #
    #     slider_elements = driver.find_elements(By.XPATH, xpath)
    #     actual_number_of_slides = len(slider_elements)
    #
    #     self.assertEqual(expecxted_number_of_slides, actual_number_of_slides,
    #                      f'Actual number of slides is different than expected')
    #
    # @screenshot_decorator
    # def test_slider_contain_sample_text(self):
    #     driver = self.conf_driver
    #     driver.get(self.base_url)
    #
    #     expected_text_included_in_slide = 'sample'
    #     xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
    #
    #     driver.get(self.base_url)
    #     title_elements = driver.find_elements(By.XPATH, xpath)
    #
    #     for title_element in title_elements:
    #         title_element_text = title_element.get_attribute("textContent")
    #         title_element_text_lower = title_element_text.lower()
    #
    #         with self.subTest(title_element):
    #             self.assertIn(expected_text_included_in_slide, title_element_text_lower,
    #                           f'Expected text is diffrent than actual')
    #
    # @screenshot_decorator
    # def test_amount_of_element_on_main_page(self):
    #     driver = self.conf_driver
    #     driver.get(self.base_url)
    #
    #     expected_number_of_products = 8
    #     xpath = '//*[@class="product-miniature js-product-miniature"]'
    #
    #     list_of_products_on_main_page = driver.find_elements(By.XPATH, xpath)
    #     number_of_products_on_main_page = len(list_of_products_on_main_page)
    #     self.assertEqual(expected_number_of_products, number_of_products_on_main_page,
    #                      f'Number of products on main page is diffrent tah expected')
    #
    # @screenshot_decorator
    # def test_loop_usage(self):
    #     expected_text_included_in_string = 'star'
    #     list_of_items = ['stargate', 'starship', 'cat', 'stardust', 'startreck', 'dog']
    #
    #     for title_element in list_of_items:
    #         print(f'Text: {title_element}')
    #
    #     for item in list_of_items:
    #         with self.subTest(item):
    #             self.assertIn(expected_text_included_in_string, item, f'Item doesn\'t contain string')
    #
    # @screenshot_decorator
    # def test_currency_for_product_on_main_page(self):
    #     expected_currency = 'PLN'
    #     xpath = '//*[@class="price"]'
    #
    #     driver = self.conf_driver
    #     driver.get(self.base_url)
    #
    #     elements_list = driver.find_elements(By.XPATH, xpath)
    #
    #     for element in elements_list:
    #         with self.subTest(element):
    #             self.assertIn(expected_currency, element.text, f'Currency isn\'t set to "PLN')
