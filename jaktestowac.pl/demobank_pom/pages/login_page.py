
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages import page_factory

class LoginPage:
    def __init__(self, driver:WebDriver):
        self.url = 'https://demobank.jaktestowac.pl/logowanie_etap_2.html'
        self.driver = driver
        print(type(driver))

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def enter_username(self, user_name):
        # finding login field and passing data
        login_field = self.driver.find_element(By.ID, 'login_id')
        login_field.clear()
        login_field.send_keys(user_name)
        return self

    def enter_password(self, password):
        # finding password field and passing data
        password_field = self.driver.find_element(By.ID, 'login_password')
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login_button(self):
        #using button to log in
        log_in_button = self.driver.find_element(By.ID, 'login_next')
        log_in_button.click()
        return self

    def log_in(self, user, password):
        # combine previous methods to log in
        self.enter_username(user)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(3)
        return page_factory.home(self.driver)

    def log_in_invalid(self, user, password):
        # combine previous methods to log in
        self.enter_username(user)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(3)
        return self

    def get_warning_text_for_id(self):
        warning_message_element = self.driver.find_element(By.ID,'error_login_id')
        return warning_message_element.text

    def get_login_page_text(self):
        header_element = self.driver.find_element(By.ID,'header_2')
        return header_element.text

