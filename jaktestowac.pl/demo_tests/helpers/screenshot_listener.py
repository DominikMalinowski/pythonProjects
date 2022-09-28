from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.events import AbstractEventListener
import time

class ScreenshotListener(AbstractEventListener):
    def SetUp(self):
        driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def on_exception(self, exception, driver):
        screenshot_path = rf"testResults\screenshot_{time.time()}.png"
        driver.get_screenshot_as_file(screenshot_path)
        print(f'Screenshot save as {screenshot_path}')
