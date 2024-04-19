import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPageClassicTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login_classic(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_2.html')

        login_field = driver.find_element(By.ID, 'login_id')
        login_field.send_keys('placeholder')

        password_field = driver.find_element(By.ID, 'login_password')
        password_field.send_keys('password')

        log_in_button = driver.find_element(By.ID, 'login_next')
        log_in_button.click()

        time.sleep(5)
