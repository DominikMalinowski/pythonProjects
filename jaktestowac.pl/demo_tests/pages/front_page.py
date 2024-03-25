
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class FrontPage():
    def __init__(self, driver:WebDriver):
        self.url = 'https://autodemo.testoneo.com/en/'
        self.driver = driver
        self.currency_xpath = '//*[@class="price"]'
        self.products_xpath = '//*[@class="product-miniature js-product-miniature"]'
        self.slider_xpath = '//*[@id="carousel"]'
        self.slider_slides_xpath = '//*[@id="carousel"]/ul/li'
        self.slider_content_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'

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

    def get_slider(self):
        slider = self.driver.find_element(By.XPATH, self.slider_xpath)
        return slider

    def get_slider_slides(self):
        slider_slides = self.driver.find_element(By.XPATH,self.slider_slides_xpath)
        return slider_slides

    def get_slider_content(self):
        sliders_element = self.driver.find_element(By.XPATH, self.slider_content_xpath)
        return sliders_element