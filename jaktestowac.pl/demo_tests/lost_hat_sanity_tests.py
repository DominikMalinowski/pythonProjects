# import of selenium and webdriver
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from helpers import funcional_helpers as fh


class LostHatSanityTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.main_page_url = 'https://autodemo.testoneo.com/en/'
        self.art_product_type_page = self.main_page_url + '9-art'
        self.clothes_product_type_page = self.main_page_url + '3-clothes'
        self.accessories_product_type_page = self.main_page_url + '6-accessories'
        self.login_page_url = self.main_page_url + 'login'

    @classmethod
    def tearDownClass(self):
        self.driver.close()