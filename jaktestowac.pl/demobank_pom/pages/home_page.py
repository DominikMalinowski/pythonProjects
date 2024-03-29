
from selenium.webdriver.common.by import By
from pages import page_factory

class HomePage:
    def __init__(self, driver):
        self.url = 'https://demobank.jaktestowac.pl/pulpit.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        print('Visiting: ', self.driver.title)
        return self

    def get_messages_text(self):
        message_element = self.driver.find_element(By.ID,'show_messages')
        return message_element.text

    def log_out(self):
        log_off_button = self.driver.find_element(By.ID,'log_out')
        log_off_button.click()
        return page_factory.login(self.driver)
