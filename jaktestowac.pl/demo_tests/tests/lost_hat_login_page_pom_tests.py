# import of selenium and webdriver

from helpers.wrappers import screenshot_decorator
from helpers.base_test_class import BaseTestClass
from pages.login_page import LoginPage
from pages.home_page import HomePage
import config_reader as cr


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
        user_name = 'mail@mail.com'
        password = 'passwordnigga'
        expected_text = 'place holder'

        login_page = LoginPage(self.conf_driver)
        login_page.visit()
        login_page.log_in(user_name, password)
        logged_user = HomePage.get_user_name()
        self.assertEqual(expected_text, logged_user, f'Actual user differ from expected. Actual user: {logged_user}')

    @screenshot_decorator
    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        user_name = "dupa@dupa.com"
        password = "israel_is_a_country"

        login_page = LoginPage(self.conf_driver)
        login_page.visit()
        login_page.log_in_invalid(user_name,password)
        header_text = login_page.get_warning_text()
        self.assertEqual(expected_text, header_text,
                         f'Actual header differs from expected. Actual header: {header_text}')


    # def assert_expected_text(self, driver, xpath, expected_text, current_url_page):
    #     header_element = driver.find_element(By.XPATH, xpath)
    #     header_element_text = header_element.text
    #     self.assertEqual(expected_text, header_element_text,
    #                      f'Expected text differ than actual. Page: {current_url_page}')