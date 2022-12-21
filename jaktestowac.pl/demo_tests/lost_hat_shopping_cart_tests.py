# import of selenium and webdriver
import time

from selenium.webdriver.common.by import By
from helpers import operational_helpers as oh
from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass

class LostHatBaskettTest(BaseTestClass):

    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    @screenshot_decorator
    def assert_expected_text(self, driver, xpath, expected_text, current_url_page):
        header_element = driver.find_element(By.XPATH, xpath)
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ than actual. Page: {current_url_page}')
    @screenshot_decorator
    def test_adding_item_to_shopping_cart(self):
        item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        add_to_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'
        expected_text = '\ue876Product successfully added to your shopping cart'

        driver = self.conf_driver
        driver.get(self.art_page_url)

        item = driver.find_element(By.XPATH, item_xpath)
        item.click()

        add_to_cart_button = driver.find_element(By.XPATH, add_to_cart_button_xpath)
        add_to_cart_button.click()

        confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)

        self.assertEqual(expected_text, confirmation_modal_element.text)

    # @screenshot_decorator
    # def test_adding_multiple_item_to_shopping_cart(self):
    #     item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
    #     add_to_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
    #     confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'
    #     continue_shopping_button_xpath = '//*[@class="btn btn-secondary"]'
    #
    #     driver = self.conf_driver
    #     driver.get(self.art_page_url)
    #
    #     item = driver.find_element(By.XPATH, item_xpath)
    #     item.click()
    #
    #     # adding first product
    #     add_to_cart_button = driver.find_element(By.XPATH, add_to_cart_button_xpath)
    #     add_to_cart_button.click()
    #
    #     oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
    #
    #     continue_shopping_button_element = driver.find_element(By.XPATH, continue_shopping_button_xpath)
    #     continue_shopping_button_element.click()
    #
    #     # adding second product
    #     add_to_cart_button = driver.find_element(By.XPATH, add_to_cart_button_xpath)
    #     add_to_cart_button.click()
    #     oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
    #
    #     continue_shopping_button_element = driver.find_element(By.XPATH, continue_shopping_button_xpath)
    #     continue_shopping_button_element.click()
    #
    #     expected_cart_item_count = '(2)'
    #     cart_xpath = '//*[@class="cart-products-count"]'
    #     cart_element = oh.visibility_of_element_wait(driver, cart_xpath)
    #     cart_element_count = cart_element.text
    #     self.assertEqual(cart_element_count, expected_cart_item_count)



    @screenshot_decorator
    def test_adding_multiple_item_to_shopping_cart(self):
        add_to_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'
        continue_shopping_button_xpath = '//*[@class="btn btn-secondary"]'
        number_of_item_added = 4

        driver = self.conf_driver
        driver.get(self.art_page_url)

        item = driver.find_element(By.XPATH, item_xpath)
        item.click()

        for i in range (1, number_of_item_added+1):

            add_to_cart_button = driver.find_element(By.XPATH, add_to_cart_button_xpath)
            add_to_cart_button.click()
            oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)

            continue_shopping_button_element = driver.find_element(By.XPATH, continue_shopping_button_xpath)
            continue_shopping_button_element.click()

            expected_cart_item_count = f'({i})'
            cart_xpath = '//*[@class="cart-products-count"]'
            cart_element = oh.visibility_of_element_wait(driver, cart_xpath)
            cart_element_count = cart_element.text
            self.assertEqual(cart_element_count, expected_cart_item_count)
            print(f'Added {i} elements to cart')


