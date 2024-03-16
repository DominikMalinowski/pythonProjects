
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.home_page import HomePage

class LoginPage:
    def __init__(self, driver:WebDriver):
        self.url = 'https://demobank.jaktestowac.pl/logowanie_etap_2.html'
        self.driver = driver
        print(type(driver))

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def log_in(self, user, password):
        # finding login field and passing data
        login_field = self.driver.find_element(By.ID, 'login_id')
        login_field.clear()
        login_field.send_keys(user)

        # finding password field and passing data
        password_field = self.driver.find_element(By.ID, 'login_password')
        password_field.clear()
        password_field.send_keys(password)

        #using button to log in
        log_in_button = self.driver.find_element(By.ID, 'login_next')
        log_in_button.click()
        time.sleep(5)

        return HomePage(self.driver)


