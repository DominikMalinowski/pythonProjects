
import unittest
import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@classmethod
def setUpClass(self):
    self.driver = webdriver.Chrome(service=Service(r'C:\ChromeDriver\chromedriver.exe'))