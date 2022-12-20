# import of selenium and webdriver

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

        # confirmation_modal_elements = oh.wait_for_elements(driver, confirmation_modal_element_xpath)
        # confirmation_modal_element = confirmation_modal_elements[0]
        # self.assertEqual(expected_text, confirmation_modal_element.text)
