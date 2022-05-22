

# import of selenium and webdriver
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

# path to webdriver
driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

# opening provided website and saving it as "Title"
try:
    driver.get('https://xxxstwory.pln/')
except WebDriverException:
    print("Page doesn't exist")

# closing currently open tab
driver.close()


