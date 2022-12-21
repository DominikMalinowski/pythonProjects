
# import of selenium and webdriver
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

# path to webdriver
driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

# opening new tab in chrome
driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
#driver.get('https://demobank.jaktestowac.pl/logowanie_prod.html')
# getting webpage title
title = driver.title
print(title)

# assertion for checkin webpage title
assert 'Demobank - Bankowość Internetowa - Logowanie' == title

#closing current tab
driver.close()

#closing the broser
driver.quit()

print("test")