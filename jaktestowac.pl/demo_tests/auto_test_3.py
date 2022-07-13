# import of selenium and webdriver
import unittest

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainTests(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def test_demo_login(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title : {title}')
        expected_title = 'Demobank - Bankowość Internetowa - Logowanie'
        self.assertEqual(expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')

    def test_demo_accounts(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/konta.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title : {title}')
        expected_title = 'Demobank - Bankowość Internetowa - Konta'
        self.assertEqual(expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')

    def test_demo_desktop(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/pulpit.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title : {title}')
        expected_title = 'Demobank - Bankowość Internetowa - Pulpit'
        self.assertEqual(expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')

    def test_demo_transfer(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title : {title}')
        expected_title = 'Demobank - Bankowość Internetowa - Przelew'
        self.assertEqual(expected_title, title,
                         f'Expected title: ({expected_title}) differ from actual title ({title}) for page url {url}')

    # def tearDown(self):
    # self.driver.quit()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


class LoginPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def test_page_title_text(self):

        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        header_element_title = driver.find_element(By.XPATH, '//*[@id="header_1"]')
        header_page_title = header_element_title.text

        expected_title = 'Wersja demonstracyjna serwisu demobank'

        self.assertEqual(expected_title, header_page_title,
                         f'Expected title: ({expected_title}) differ from \
                         actual title ({header_page_title}) for page url {url}')

    def test_if_continue_button_is_active(self):

        driver = self.driver
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

        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.send_keys('12345', Keys.ENTER)

        additional_info_button = driver.find_element(By.XPATH,'//*[@id="login_id_container"]/div[3]/div/i')
        additional_info_button.click()

        login_id_error = driver.find_element(By.XPATH,'//*[@id="error_login_id"]')
        login_id_error_text = login_id_error.text
        print(login_id_error_text)

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()
