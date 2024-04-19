import unittest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener
import config_reader as cr

class BaseTestClass(unittest.TestCase):

    @classmethod
    def setUp(self):
        driver = webdriver.Chrome()
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_page_url = self.base_url + 'login?back=my-account'
        self.art_page_url = self.base_url + '9-art'
        self.product_page_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.man_t_shirt_url = self.base_url + 'men/1-4-hummingbird-printed-t-shirt.html'


        config = cr.load()
        if config["event_firing_driver"] == True:
            self.conf_driver = EventFiringWebDriver(driver, ScreenshotListener())
        else:
            self.conf_driver = driver

        # self.base_url = 'https://autodemo.testoneo.com/en/'
        self.base_url = config['base_url']


    @classmethod
    def tearDown(self):
        self.conf_driver.quit()
