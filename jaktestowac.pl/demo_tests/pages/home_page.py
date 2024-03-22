
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver: WebDriver):
        self.url = 'https://autodemo.testoneo.com/en/my-account'
        self.driver = driver
        self.username_xpath = '//header*[@class="hidden-sm-down"]'

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def get_user_name(self):
        current_user = self.driver.find_element(By.XPATH, self.username_xpath)
        return current_user.text()