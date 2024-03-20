import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import page_factory


class QuickPaymentPageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        quic_payment_page = page_factory.quick_payment(self.driver)
        quic_payment_page.visit()

        page_title_text = quic_payment_page.page_title()

        self.assertEqual('Brak wiadomości', page_title_text,
                         f'Actual text is different than expected: {page_title_text}')

    # def test_successful_quick_payment(self, amount, title):
    def test_successful_quick_payment(self):
        amount = '108,50'
        title = 'placeholder'
        receiver = 'Chuck Demobankowy'

        quic_payment_page = page_factory.quick_payment(self.driver)
        quic_payment_page.visit()

        quic_payment_page.select_receiver(receiver)
        quic_payment_page.provide_amount(amount)
        quic_payment_page.provide_title(title)
        quic_payment_page.click_execute_button()
        time.sleep(3)

        payment_message = quic_payment_page.page_title()
        self.assertEqual(f'Przelew wykonany! {receiver} - {amount}PLN - {title}', payment_message,
                         f'Actual message differs than expected. Actual message: {payment_message}')
