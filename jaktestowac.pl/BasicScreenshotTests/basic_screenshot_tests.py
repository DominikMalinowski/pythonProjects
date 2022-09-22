import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as NSEE


class BasicScreenShotTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://antoogle.testoneo.com/'
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def tearDown(self):
        self.driver.quit()

    def test_opened_base_url(self):
        self.driver.get(self.base_url)
        self.assertEqual('The Antoogle Search Page', self.driver.title,
                         f'Expected title differ from actual for page url: {self.base_url}')
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="wont_find_me"]')
        except NSEE:
            self.driver.get_screenshot_as_file("screenshot.png")
            raise NSEE
