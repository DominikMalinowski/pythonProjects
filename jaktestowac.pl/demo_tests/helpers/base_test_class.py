import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener
import config_reader as cr

class BaseTestClass(unittest.TestCase):

    @classmethod
    def setUp(self):
        config = cr.load()

        driver = webdriver.Chrome(service=Service(executable_path=config['chromedriver_path']))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

        # self.base_url = 'https://autodemo.testoneo.com/en/'
        self.base_url = config['base_url']

        self.login_page_url = self.base_url + 'login?back=my-account'
        self.art_page_url = self.base_url + '9-art'
        self.product_page_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.man_t_shirt_url = self.base_url + 'men/1-4-hummingbird-printed-t-shirt.html'

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()
