# import of selenium and webdriver
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener

class LostHatProductTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def setUp(self):
        driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())
        self.main_page_url = 'https://autodemo.testoneo.com/en/'
        self.login_page_url = 'https://autodemo.testoneo.com/en/login?back=my-account'
        self.product_page_url = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'

    def tearDown(self):
        self.ef_driver.quit()

    def assert_expected_text(self, driver, xpath, expected_text, current_url_page):
        header_element = driver.find_element(By.XPATH, xpath)
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ than actual. Page: {current_url_page}')

    def test_product_name(self):
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        xpath = '//*[@id="main"]//*[@class="h1"]'
        current_url_page = self.product_page_url

        driver = self.ef_driver
        driver.get(self.product_page_url)

        self.assert_expected_text(driver, xpath, expected_text, current_url_page)

    def test_check_product_price(self):
        expected_text = 'PLN23.52'
        xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        current_page_url = self.product_page_url

        driver = self.ef_driver
        driver.get(self.product_page_url)

        self.assert_expected_text(driver, xpath, expected_text, current_page_url)




