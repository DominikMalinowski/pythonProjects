
from selenium.webdriver.common.by import By
import config_reader

class FrontPage():
    def __init__(self, driver):
        config = config_reader.load()
        self.url = config['base_url']
        self.driver = driver

        self.user_name_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'
        self.slider_xpath = '//*[@id="carousel"]'
        self.slider_slides_xpath = '//*[@id="carousel"]/ul/li'
        self.slider_content_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
        self.currency_xpath = '//*[@class="price"]'
        self.products_xpath = '//*[@class="product-miniature js-product-miniature"]'

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def get_username(self):
        self.driver.find_element(By.XPATH, self.user_name_xpath)
        return  self


    def get_amount_of_element_on_main_page(self):
        elements_list = self.driver.find_elements(By.XPATH,self.products_xpath)
        return elements_list

    def get_slider_size(self):
        slider = self.driver.find_element(By.XPATH, self.slider_xpath)
        return {'width': slider.size['width'], 'height': slider.size['height']}

    def get_slider_slides_count(self):
        slider_slides = self.driver.find_elements(By.XPATH,self.slider_slides_xpath)
        return len(slider_slides)

    def get_slider_content(self):
        sliders_element = self.driver.find_elements(By.XPATH, self.slider_content_xpath)
        return sliders_element

    def get_currency(self):
        currency = self.driver.find_elements(By.XPATH, self.currency_xpath)
        return currency