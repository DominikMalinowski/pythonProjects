
import unittest
from selenium import webdriver


class LoginPageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        username = 'placeholder'
        password = 'password'
        # login_page = LoginPage(self.driver)


