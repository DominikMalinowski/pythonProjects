
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages import login_page


class HomePage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://autodemo.testoneo.com/en/'
        self.driver = driver
        self.username_xpath = '//a[@class="account"]/*[@class="hidden-sm-down"]'

        self.slider_xpath = '//*[@id="carousel"]'
        self.slides_xpath = '//*[@id="carousel"]/ul/li'
        self.slides_titles_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
        self.featured_products_xpath = '//*[@class="product-miniature js-product-miniature"]'
        self.product_prices_xpath = '//*[@class="product-miniature js-product-miniature"]//*[@class="price"]'

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def get_user_name(self):
        current_user = self.driver.find_element(By.XPATH, self.username_xpath)
        return current_user.text

    def open_login_page(self):
        button_next_element = self.driver.find_element(By.XPATH,'//*[@class="user-info"]')
        button_next_element.click()
        return login_page.LoginPage(self.driver)

    def get_slider_size(self):
        slider_element = self.driver.find_element(By.XPATH,self.slider_xpath)
        return {'width': slider_element.size['width'], 'height': slider_element.size['height']}

    def get_slider_elements_count(self):
        slider_elements = self.driver.find_elements(By.XPATH,self.slides_xpath)
        return len(slider_elements)

    def get_slider_titles(self):
        title_elements = self.driver.find_elements(By.XPATH,self.slides_titles_xpath)
        return title_elements

    def get_featured_products_count(self):
        product_elements = self.driver.find_elements(By.XPATH,self.featured_products_xpath)
        return len(product_elements)

    def get_product_prices(self):
        product_price_elements = self.driver.find_elements(By.XPATH,self.product_prices_xpath)
        return product_price_elements