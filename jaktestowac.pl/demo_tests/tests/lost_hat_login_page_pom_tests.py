# import of selenium and webdriver

from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass
import config_reader
from pages.login_page import LoginPage
from pages.home_page import HomePage


class LostHatLoginPomTest(BaseTestClass):


    @screenshot_decorator
    def test_header_element_title(self):
        expected_text = 'Log in to your account'

        login_page = LoginPage(self.conf_driver)
        login_page.visit()
        header_text = login_page.get_header()
        self.assertEqual(expected_text, header_text,
                         f'Actual header differs from expected. Actual header: {header_text}')

    @screenshot_decorator
    def test_correct_login(self):
        config = config_reader.load()
        user_name = config['correct_mail']
        password = config['correct_pass']
        expected_text = config['correct_user_fullname']

        login_page = LoginPage(self.conf_driver)
        login_page.visit()
        home_page = login_page.log_in(user_name, password)
        logged_user = home_page.get_user_name()
        self.assertEqual(expected_text, logged_user, f'Actual user differ from expected. Actual user: {logged_user}')

    @screenshot_decorator
    def test_incorrect_login(self):
        config = config_reader.load()
        expected_text = 'Authentication failed.'
        user_name = config['incorrect_mail']
        password = config['incorrect_pass']

        login_page = LoginPage(self.conf_driver)
        login_page.visit()
        login_page.log_in_invalid(user_name,password)
        header_text = login_page.get_error_text()
        self.assertEqual(expected_text, header_text,
                         f'Actual header differs from expected. Actual header: {header_text}')
