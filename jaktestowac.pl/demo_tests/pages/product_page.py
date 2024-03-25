
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
class ProductPage():
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.url = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'
        self.product_xpath = '//*[@id="main"]//*[@class="h1"]'
        self.price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        self.current_product_size_xpath = '//*[@id="group_1"]'

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def get_product_name(self):
        self.driver.find_element(By.XPATH, self.product_xpath)
        return self

    def get_product_price(self):
        self.driver.find_element(By.XPATH, self.price_xpath)
        return self

    def get_product_size(self):
        self.driver.find_element(By.XPATH, self.current_product_size_xpath)
        return self