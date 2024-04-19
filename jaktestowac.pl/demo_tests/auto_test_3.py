# import of selenium and webdriver
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from helpers.screenshot_listener import ScreenshotListener
from helpers import operational_helpers_2 as oh2


class MainTests(unittest.TestCase):
    # def setUp(self):
    #     pass

    @classmethod
    def setUpClass(self):
        driver = webdriver.Chrome()
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    # def tearDown(self):
    # self.driver.quit()

    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()

    def test_demo_login(self):
        driver = self.ef_driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        print(f'Actual title : {self.ef_driver.title}')
        expected_title = 'Demobank - Bankowość Internetowa - Logowanie'
        self.assertEqual(expected_title, self.ef_driver.title,
                         f'Expected title: ({expected_title}) differ from actual title ({self.ef_driver.title}) for page url {url}')

    def test_demo_accounts(self):
        driver = self.ef_driver
        url = 'https://demobank.jaktestowac.pl/konta.html'
        driver.get(url)
        print(f'Actual title : {self.ef_driver.title}')
        expected_title = 'Demobank - Bankowość Internetowa - Konta'
        self.assertEqual(expected_title, self.ef_driver.title,
                         f'Expected title: ({expected_title}) differ from actual title ({self.ef_driver.title}) for page url {url}')

    def test_demo_desktop(self):
        driver = self.ef_driver
        url = 'https://demobank.jaktestowac.pl/pulpit.html'
        driver.get(url)
        print(f'Actual title : {self.ef_driver.title}')
        expected_title = 'Demobank - Bankowość Internetowa - Pulpit'
        self.assertEqual(expected_title, self.ef_driver.title,
                         f'Expected title: ({expected_title}) differ from actual title ({self.ef_driver.title}) for page url {url}')

    def test_demo_transfer(self):
        driver = self.ef_driver
        url = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
        driver.get(url)
        print(f'Actual title : {self.ef_driver.title}')
        expected_title = 'Demobank - Bankowość Internetowa - Przelew'
        self.assertEqual(expected_title, self.ef_driver.title,
                         f'Expected title: ({expected_title}) differ from actual title ({self.ef_driver.title}) for page url {url}')


class LoginPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()

    def test_page_title_text(self):
        driver = self.ef_driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        header_element_title = driver.find_element(By.XPATH, '//*[@id="header_1"]')
        header_page_title = header_element_title.text

        expected_title = 'Wersja demonstracyjna serwisu demobank'

        self.assertEqual(expected_title, header_page_title,
                         f'Expected title: ({expected_title}) differ from \
                         actual title ({header_page_title}) for page url {url}')

    def test_if_continue_button_is_active(self):
        driver = self.ef_driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')

        login_next_button_element_disabled = login_next_button_element.get_property('disabled')
        print(f'Disabled value before: "{login_next_button_element_disabled}"')

        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.send_keys('123456789', Keys.ENTER)

        login_next_button_element_disabled = login_next_button_element.get_property('disabled')
        print(f'Disabled value after: "{login_next_button_element_disabled}"')

        login_input_element.clear()

    def test_button_activity_on_characters_lesser_than_required(self):
        driver = self.ef_driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.send_keys('12345', Keys.ENTER)

        additional_info_button = driver.find_element(By.XPATH, '//*[@id="login_id_container"]/div[3]/div/i')
        additional_info_button.click()

        login_id_error = driver.find_element(By.XPATH, '//*[@id="error_login_id"]')
        login_id_error_text = login_id_error.text
        print(login_id_error_text)

    def test_opening_next_page(self):
        driver = self.ef_driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        xpath = '//*[@id="login_id"]'

        login_input_element = driver.find_element(By.XPATH, xpath)
        login_input_element.send_keys('12345678', Keys.ENTER)
        oh2.visibility_of_element_wait(driver, xpath)

        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        login_next_button_text = login_next_button_element.text
        print(login_next_button_text)
