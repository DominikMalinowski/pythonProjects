
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from helpers import operational_helpers as oh

class ProductPage():
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.url = None
        # self.url = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'
        self.product_xpath = '//*[@id="main"]//*[@class="h1"]'
        self.price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        self.current_product_size_xpath = '//*[@id="group_1"]'
        self.shopping_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        self.confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'
        self.continue_shopping_button_xpath = '//*[@class="btn btn-secondary"]'
        self.cart_products_count_xpath = './/*[@class="cart-products-count"]'

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def get_product_name(self):
        product = self.driver.find_element(By.XPATH, self.product_xpath)
        return product.text

    def get_product_price(self):
        price = self.driver.find_element(By.XPATH,self.price_xpath)
        return price.text

    def get_product_size(self):
        size_element = self.driver.find_element(By.XPATH, self.current_product_size_xpath)
        size = Select(size_element)
        return size.first_selected_option.text

    def change_product_size(self, new_size):
        product_size_select_element = self.driver.find_element(By.XPATH,self.current_product_size_xpath)
        product_size_select = Select(product_size_select_element)
        product_size_select.select_by_visible_text(new_size)
        return self

    def add_item_and_get_confirmation_message(self, item_name):
        shopping_cart_button_element = self.driver.find_element(By.XPATH, self.shopping_cart_button_xpath)
        shopping_cart_button_element.click()

        confirmation_modal_element = oh.visibility_of_element_wait(self.driver, self.confirmation_modal_title_xpath)
        return confirmation_modal_element.text

    def add_item_to_cart(self):
        shopping_cart_button_element = self.driver.find_element(By.XPATH, self.shopping_cart_button_xpath)
        shopping_cart_button_element.click()
        oh.visibility_of_element_wait(self.driver, self.confirmation_modal_title_xpath)
        continue_shopping_button_element = self.driver.find_element(By.XPATH, self.continue_shopping_button_xpath)
        continue_shopping_button_element.click()
        return self

    def get_items_count(self):
        cart_products_count_element = oh.visibility_of_element_wait(self.driver, self.cart_products_count_xpath)
        return cart_products_count_element.text
