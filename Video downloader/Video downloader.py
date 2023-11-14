
# import of selenium and webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import urllib.request

# path to webdriver
driver = webdriver.Chrome(service=Service(r'D:\ChromeDriver\chromedriver.exe'))

# opening new tab in chrome
web_page = 'https://www.cda.pl/video/15443583ca'
driver.get(web_page)

# locate video src 
player_xpath = '//*[@class="pb-video-player"]'
link_to_player = driver.find_element(By.XPATH, player_xpath)
link_to_video = link_to_player.get_attribute('src')

# download
urllib.request.urlretrieve(link_to_video, 'video.mp4')
print('Done')
