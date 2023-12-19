
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def take_screenshot(path):
    chromeDriver_path = 'C:\ChromeDriver\chromedriver.exe'
    driver = webdriver.Chrome(service=Service(chromeDriver_path))
    driver.get(path)
    driver.maximize_window()

    driver.find_element(By.ID,'email').send_keys('placeholder@placeholder.com')
    driver.find_element(By.ID,'login-password').send_keys('placeholder2')
    driver.find_element(By.ID,'login').click()
    destination_file_name = 'C:\\Users\\dmalinowski\\Desktop\\screenshot.png'

    time.sleep(5) 
    try:
        driver.save_screenshot(destination_file_name)
        print('Screenshot has been save in directory: ' + destination_file_name)
    except NotADirectoryError:
        print('Not a directory issue')
    


website_url = 'https://www.letskodeit.com/login' 
take_screenshot(website_url)