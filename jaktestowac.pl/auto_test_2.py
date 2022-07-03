
# import of selenium and webdriver
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

# path to webdriver
driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))