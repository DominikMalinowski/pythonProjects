import unittest
from selenium import webdriver
from pages import page_factory


class LoginPageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        test_username = 'placeholder'
        test_password = 'password'

        login_page = page_factory.login(self.driver)
        login_page.visit()
        home_page = login_page.log_in(test_username, test_password)
        messages_text = home_page.get_messages_text()
        self.assertEqual('Brak wiadomości', messages_text,
                         f'Expected login button text differ from actual: {messages_text}')

    def test_display_error_message_when_user_submit_less_than_8_signs(self):
        test_wrong_username = 'test'
        test_password = 'password'

        login_page = page_factory.login(self.driver)
        login_page.visit()
        login_page.log_in_invalid(test_wrong_username, test_password)
        warning_message_text = login_page.get_warning_text_for_id()
        self.assertEqual('identyfikator ma min. 8 znaków', warning_message_text,
                         f'Actual message differs from expected one. Actual message: {warning_message_text}')
