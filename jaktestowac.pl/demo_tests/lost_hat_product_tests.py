# import of selenium and webdriver
import unittest

from selenium.webdriver.common.by import By
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass

class LostHatProductTest(BaseTestClass):

    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))


    def assert_expected_text(self, driver, xpath, expected_text, current_url_page):
        header_element = driver.find_element(By.XPATH, xpath)
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ than actual. Page: {current_url_page}')

    @screenshot_decorator
    def test_product_name(self):
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        xpath = '//*[@id="main"]//*[@class="h1"]'
        current_url_page = self.product_page_url

        driver = self.conf_driver
        driver.get(self.product_page_url)

        self.assert_expected_text(driver, xpath, expected_text, current_url_page)

    @screenshot_decorator
    def test_check_product_price(self):
        expected_text = 'PLN23.52'
        xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        current_page_url = self.product_page_url

        driver = self.conf_driver
        driver.get(self.product_page_url)

        self.assert_expected_text(driver, xpath, expected_text, current_page_url)




