import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener

class BaseTestClass(unittest.TestCase):

    @classmethod
    def setUp(self):
        driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())
        self.main_page_url = 'https://autodemo.testoneo.com/en/'
        self.login_page_url = self.main_page_url + 'login?back=my-account'
        self.art_page_url = self.main_page_url + '9-art'
        self.product_page_url = self.main_page_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.man_t_shirt_url = self.main_page_url + 'men/1-4-hummingbird-printed-t-shirt.html'

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()
