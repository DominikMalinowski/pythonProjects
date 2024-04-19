import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class QuiCkPaymentPage:
    def __init__(self, driver):
        self.url = 'https://demobank.jaktestowac.pl/quick_payment.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def page_title(self):
        message_element = self.driver.find_element(By.ID, 'show_messages')
        return message_element.text

    def select_receiver(self,receiver_name):
        receiver_field = self.driver.find_element(By.ID, 'widget_1_transfer_receiver')
        receiver_field.click()
        receiver_select = Select(receiver_field)
        receiver_select.select_by_visible_text(receiver_name)
        return self

    def provide_amount(self, amount):
        amount_field = self.driver.find_element(By.ID, 'widget_1_transfer_amount')
        amount_field.clear()
        amount_field.send_keys(amount)
        return self

    def provide_title(self, title):
        title_field = self.driver.find_element(By.ID, 'widget_1_transfer_title')
        title_field.clear()
        title_field.send_keys(title)
        return self

    def click_execute_button(self):
        execute_button = self.driver.find_element(By.ID, 'execute_btn')
        execute_button.click()
        return self

    def make_payment(self, receiver_name, amount, title):
        # combine previous methods to log in
        self.select_receiver(receiver_name)
        self.provide_amount(amount)
        self.provide_title(title)
        self.click_execute_button()
        time.sleep(3)
        return self


