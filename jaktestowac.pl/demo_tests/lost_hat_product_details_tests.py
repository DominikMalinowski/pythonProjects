from selenium.webdriver.support.select import Select

from helpers.base_test_class import BaseTestClass
from helpers.wrappers import screenshot_decorator
from selenium.webdriver.common.by import By


class LostHatProductDetailsTests(BaseTestClass):
    @screenshot_decorator
    def test_check_product_default_size(self):
        expected_product_default_size = 'M'
        size_select_xpath = '//*[@id="group_1"]'
        default_select_option_xpath = f'{size_select_xpath}/*[@selected = "selected"]'
        url = 'https://autodemo.testoneo.com/en/men/1-4-hummingbird-printed-t-shirt.html'
        driver = self.ef_driver

        driver.get(url)
        selected_size_element = driver.find_element(By.XPATH, default_select_option_xpath)
        self.assertEqual(selected_size_element.text, expected_product_default_size,
                         f'Expected size differ from actual on page: {driver.current_url}')

    @screenshot_decorator
    def test_check_product_size_change(self):
        expected_product_default_size = 'L'
        size_select_xpath = '//*[@id="group_1"]'
        default_select_option_xpath = f'{size_select_xpath}/*[@selected = "selected"]'
        size_l_select_xpath = f'{size_select_xpath}/*[@title = "L"]'

        url = 'https://autodemo.testoneo.com/en/men/1-4-hummingbird-printed-t-shirt.html'
        driver = self.ef_driver

        driver.get(url)
        selected_size_element = driver.find_element(By.XPATH, default_select_option_xpath)
        observed_product_default_size_text = selected_size_element.text

        product_size_select_element = driver.find_element(By.XPATH, size_select_xpath)
        product_size_select_element.click()

        option_l_element = driver.find_element(By.XPATH, size_l_select_xpath)
        option_l_element.click()

        observed_product_size_changed_value = product_size_select_element.get_attribute('value')
        observed_product_size_changed_value_element = driver.find_element(By.XPATH,
                                                                          f'//*[@id="group_1"]/*[@value="{observed_product_size_changed_value}"]')
        observed_product_size_changed_value_element_text = observed_product_size_changed_value_element.text

        self.assertNotEqual(expected_product_default_size, observed_product_default_size_text,
                            f'Expected size is the same as actual on page: {driver.current_url}')

        self.assertEqual(expected_product_default_size, observed_product_size_changed_value_element_text,
                         f'Expected size differ from actual on page: {driver.current_url}')

    @screenshot_decorator
    def test_check_product_size_change_new(self):
        expected_product_changed_size = 'L'
        size_select_xpath = '//*[@id="group_1"]'
        url = 'https://autodemo.testoneo.com/en/men/1-4-hummingbird-printed-t-shirt.html'

        driver = self.ef_driver
        driver.get(url)

        product_size_select_element = driver.find_element(By.XPATH, size_select_xpath)
        product_size_select = Select(product_size_select_element)
        observed_product_default_size_text = product_size_select.first_selected_option.text
        print(observed_product_default_size_text)