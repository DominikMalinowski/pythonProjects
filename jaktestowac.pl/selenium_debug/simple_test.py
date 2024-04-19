
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))
driver.get('https://antoogle.testoneo.com/')
title = driver.title

button = driver.find_element(By.ID,'searchBtn')
button.click()

element_list = driver.find_elements(By.CSS_SELECTOR,'[id^="item"]')
number_of_founded_elements = len(element_list)
print(f'Result items: {number_of_founded_elements}')

for item in element_list:
    print(item.text)

driver.quit()

assert "The Antoogle Search Page", title
