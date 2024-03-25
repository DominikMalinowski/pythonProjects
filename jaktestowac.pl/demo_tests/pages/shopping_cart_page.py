
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class ShoppingCartPage():
    def __init__(self, driver:WebDriver):
        self.url = 'https://autodemo.testoneo.com/en/cart?action=show'
        self.driver = driver
        self.item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        self.add_to_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        self.confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def