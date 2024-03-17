import time

from selenium.webdriver.common.by import By
class QuiCkPaymentPage:
    def __init__(self, driver):
        self.url = 'https://demobank.jaktestowac.pl/quick_payment.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def payment(self, amount, title):
    #
    #     receiver_field = self.driver.find_element(By.ID, 'widget_1_transfer_receiver')
    #     receiver_field.click()
    #
    #     amount_field = self.driver.find_element(By.ID, 'widget_1_transfer_amount')
    #     amount_field.clear()
    #     amount_field.send_keys(amount)
    #
    #     title_field = self.driver.find_element(By.ID, 'widget_1_transfer_title')
    #     title_field.clear()
    #     title_field.send_keys(title)
    #
    #     execute_button = self.driver.find_element(By.ID, 'execute_btn')
    #     execute_button.click()
    #     time.sleep(3)
    #
        message_element = self.driver.find_element(By.ID, 'show_messages')
        return message_element.text
