import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class LoginPageClassictest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\Programy\chromedriver-win64\chromedriver.exe'))

    def tearDown(self):
        self.driver.quit()

    def test_login_classic(self):
        pass 
