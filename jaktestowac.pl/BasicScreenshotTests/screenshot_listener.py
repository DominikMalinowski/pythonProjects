from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.events import AbstractEventListener


class ScreenshotListener(AbstractEventListener):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def on_exception(self, exception, driver):
        screenshot_name = "screenshot.png"
        driver.get_screenshot_as_file(screenshot_name)
        print(f'Screenshot save as {screenshot_name}')
