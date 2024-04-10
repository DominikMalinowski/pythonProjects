from pages.product_page import ProductPage
from selenium.webdriver.common.by import By


class CategoryPage():
    def __init__(self, driver):
        self.url = None # there is category page
        self.driver = driver
        self.item_xpath = '//*[@alt="{0}"]'

    def visit(self):
        self.driver.get(self.url)
        return self

    def open_product_page(self, item_name):
        item_element = self.driver.find_element(By.XPATH, self.item_xpath.format(item_name))
        item_element.click()
        return ProductPage(self.driver)
