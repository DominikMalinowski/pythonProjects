# import of selenium and webdriver

from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass
from pages.front_page import FrontPage

class LostHatsFrontPagePomTests(BaseTestClass):

    @screenshot_decorator
    def test_is_slider_present(self):
        front_page = FrontPage(self.conf_driver)
        front_page.visit()
        front_page.get_slider_size()

    @screenshot_decorator
    def test_slider_minimum_size(self):
        expected_min_height = 300
        expected_min_width = 600

        front_page = FrontPage(self.conf_driver)
        front_page.visit()
        slider_element = front_page.get_slider_size()

        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']

        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height,
                            f'Element height for page {self.base_url} is smaller than expected {expected_min_height}')

        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width,
                            f'Element width for page {self.base_url} is smaller than expected {expected_min_width}')
    #
    # @screenshot_decorator
    # def test_slider_contain_exact_number_of_slides(self):
    #     expecxted_number_of_slides = 3
    #
    #     front_page = FrontPage(self.conf_driver)
    #     front_page.visit()
    #     slider_elements = front_page.get_slider_slides()
    #     actual_number_of_slides = len(slider_elements)
    #
    #     self.assertEqual(expecxted_number_of_slides, actual_number_of_slides,
    #                      f'Actual number of slides is different than expected')
    #
    # @screenshot_decorator
    # def test_slider_contain_sample_text(self):
    #     expected_text_included_in_slide = 'sample'
    #
    #     front_page = FrontPage(self.conf_driver)
    #     front_page.visit()
    #     elements_list = front_page.get_slider_content()
    #
    #     for title_element in elements_list:
    #         title_element_text = title_element.get_attribute("textContent")
    #         title_element_text_lower = title_element_text.lower()
    #
    #         with self.subTest(title_element):
    #             self.assertIn(expected_text_included_in_slide, title_element_text_lower,
    #                           f'Expected text is diffrent than actual')
    #
    # @screenshot_decorator
    # def test_amount_of_element_on_main_page(self):
    #     expected_number_of_products = 8
    #
    #     front_page = FrontPage(self.conf_driver)
    #     front_page.visit()
    #     element_list = front_page.get_amount_of_element_on_main_page()
    #     number_of_products_on_main_page = len(element_list)
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
    #
    #     front_page = FrontPage(self.conf_driver)
    #     front_page.visit()
    #     elements_list = front_page.get_currency()
    #
    #     for element in elements_list:
    #         with self.subTest(element):
    #             self.assertIn(expected_currency, element.text, f'Currency isn\'t set to "PLN')
