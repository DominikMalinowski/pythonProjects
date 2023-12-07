
# import unittest
# import pytest


# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

# @classmethod
# def setUpClass(self):
#     self.driver = webdriver.Chrome(service=Service(r'C:\ChromeDriver\chrome.exe'))

# %%
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def open(path):
    chromeDriver_path = 'C:\ChromeDriver\chromedriver.exe'
    driver = webdriver.Chrome(service=Service(chromeDriver_path))
    driver.get(path)
    time.sleep(5)
    driver.implicitly_wait(10)

    element_id = 'openwindow'
    element = driver.find_element(By.ID,element_id)
    if element is not None:
        print('Element found by ID: '+ element_id)


website_path = 'https://www.letskodeit.com/practice'
open(website_path)