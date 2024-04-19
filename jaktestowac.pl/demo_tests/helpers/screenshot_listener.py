from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.events import AbstractEventListener
import time

class ScreenshotListener(AbstractEventListener):
    def SetUp(self):
        driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

    def on_exception(self, exception, driver):
        # PyCharm debugger cause exception so we need to ignore it
        pycharm_debugger_exceptions = [
            "'WebElement' object has no attribute '__len__'",
            "'WebDriver' object has no attribute '__len__'",
            "'WebDriver' object has no attribute 'shape'",
            "'WebElement' object has no attribute 'shape'"
        ]
        if str(exception) not in pycharm_debugger_exceptions:
            make_screenshot(driver, 'driver')

def make_screenshot(driver, producer):
    screenshot_path = rf"testResults\{producer}_exception_{time.time()}.png"
    driver.get_screenshot_as_file(screenshot_path)
    print(f'Screenshot save as {screenshot_path}')
