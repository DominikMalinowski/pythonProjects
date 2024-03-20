import unittest
from selenium import webdriver
from pages import page_factory


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_logout(self):
        home_page = page_factory.home(self.driver)
        home_page.visit()
        login_page = home_page.log_out()
        current_header = login_page.get_login_page_text()
        self.assertEqual('Wersja demonstracyjna serwisu demobank', current_header,
                         f'Current header differs from expected. Current header: {current_header}')
