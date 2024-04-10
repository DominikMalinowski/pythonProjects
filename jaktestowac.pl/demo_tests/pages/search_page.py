
import config_reader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SearchPage():
    def __init__(self, driver):
        config = config_reader.load()
        self.url = config['base_url']
        self.driver = driver
        self.search_input_xpath = '//*[@name="s"]'
        self.result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'

    def visit(self):
        self.driver.get(self.url)
        return self

    def search(self, search_phrase):
        search_input_element = self.driver.find_element(By.XPATH, self.search_input_xpath)
        search_input_element.send_keys(search_phrase)
        search_input_element.send_keys(Keys.ENTER)
        return self

    def get_search_results(self):
        result_elements = self.driver.find_elements(By.XPATH, self.result_element_xpath)
        return result_elements