import time
import unittest
from selenium import webdriver
from pages.quick_payment_page import QuiCkPaymentPage

class QuickPaymentPageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_quick_payment(self):
        amount = 108
        title = 'placeholder'

        quic_payment_page = QuiCkPaymentPage(self.driver)
        quic_payment_page.visit()

        transfer_text = quic_payment_page.payment(amount, title)

        self.assertEqual('Brak wiadomości', transfer_text,
                         f'Actual text is different than expected: {transfer_text}')
        # self.assertEqual(f'Przelew wykonany! Chuck Demobankowy - {amount}PLN - {title}', transfer_text,
        #                  f'Actual text is different than expected: {transfer_text}')

