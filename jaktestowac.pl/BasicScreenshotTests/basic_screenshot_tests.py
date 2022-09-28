import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from screenshot_listener import ScreenshotListener


class BasicScreenShotTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://antoogle.testoneo.com/'
        driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    def tearDown(self):
        self.ef_driver.quit()

    def test_demo(self):
        self.ef_driver.get(self.base_url)
        self.assertEqual('The Antoogle Search Page', self.ef_driver.title,
                         f'Expected title differ from actual for page url: {self.base_url}')

    def test_demo_search(self):
        self.ef_driver.get(self.base_url)
        element = self.ef_driver.find_element(By.XPATH, '//*[@id="wont_find_me"]')
        self.assertEqual('Search!', element.text,
                         f'Expected element text differ from actual for page url: {self.base_url}')

    def test_that_fails_without_screenshot(self):
        self.ef_driver.get(self.base_url)
        self.assertEqual('Invalid Page Name', self.ef_driver.title,
                         f'Expected tile differ from actual title for page {self.base_url}')
