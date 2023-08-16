
# import of selenium and webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# path to webdriver
driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

# opening new tab in chrome
web_page = 'https://inne.wbijam.pl/fmab.html'
driver.get(web_page)

players_xpath = '//*[@class="lista_hover"]'
links_to_players = driver.find_elements(By.XPATH, players_xpath)

for i in links_to_players:
    xpath = '//*[@class="odtwarzacz_link"]'
    episodes = driver.find_elements(By.XPATH, players_xpath)
    print(episodes)
