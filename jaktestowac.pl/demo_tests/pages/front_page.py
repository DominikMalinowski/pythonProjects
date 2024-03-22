
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class FrontPage():
    def __init__(self, driver:WebDriver):
        self.url = 'https://autodemo.testoneo.com/en/'
        self.driver = driver
        self.currency_xpath = '//*[@class="price"]'
        self.products_xpath = '//*[@class="product-miniature js-product-miniature"]'

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def get_currency(self):
        currency = self.driver.find_elements(By.XPATH, self.currency_xpath)
        return currency

    def get_amount_of_element_on_main_page(self):
        elements_list = self.driver.find_elements(By.XPATH,self.products_xpath)
        return elements_list
