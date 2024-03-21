
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


class LoginPage:
    def __init__(self, driver:WebDriver):
        self.url = 'https://autodemo.testoneo.com/en/login?back=my-account'
        self.driver = driver
        self.header_xpath = '//header[@class="page-header"]'
        self.login_field_xpath = '//header*[@class="form-control"]'
        self.password_field_xpath = '//header*[@class="form-control js-child-focus js-visible-password"]'
        self.button_xpath = '//header*[@class="btn btn-primary"]'
        self.error_message_xpath = '//*[@class="alert alert-danger"]'

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def get_header(self):
        header_element = self.driver.find_element(By.XPATH, self.header_xpath)
        return header_element.text

    def get_warning_text(self):
        warning_message_element = self.driver.find_element(By.XPATH, self.error_message_xpath)
        return warning_message_element.text

    def enter_username(self, user_name):
        # finding login field and passing data
        login_field = self.driver.find_element(By.XPATH, self.login_field_xpath)
        login_field.clear()
        login_field.send_keys(user_name)
        return self

    def enter_password(self, password):
        # finding password field and passing data
        password_field = self.driver.find_element(By.XPATH, self.password_field_xpath)
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login_button(self):
        #using button to log in
        log_in_button = self.driver.find_element(By.XPATH, self.button_xpath)
        log_in_button.click()
        return self

    def log_in(self, user, password):
        # combine previous methods to log in
        self.enter_username(user)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(3)
        return HomePage(self.driver)

    def log_in_invalid(self, user, password):
        # combine previous methods to log in
        self.enter_username(user)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(3)
        return self





