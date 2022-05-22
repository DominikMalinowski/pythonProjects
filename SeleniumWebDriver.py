
# import of selenium and webdriver
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# path to webdriver
driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

# opening provided website and saving it as "Title"
driver.get('https://jbzd.com.pl/')
title = driver.title

# test to check "Title" variable
assert 'Jbzd.com.pl - najgorsze obrazki w internecie!' == title

# closing currently open tab
#driver.close()

# closing the browser
driver.quit()

##
# checking if page exist

from selenium.common.exceptions import WebDriverException
driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

try:
    driver.get('https://xxxstwory.pln/')
except WebDriverException:
    print("Page doesn't exist")

##