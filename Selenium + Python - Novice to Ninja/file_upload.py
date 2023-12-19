import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

driver = webdriver.Chrome()
driver.maximize_window()

# # native way 
# driver.get('https://www.plupload.com/examples/')
# element = driver.find_element(By.XPATH,"//div[@id='uploader_buttons']/div/input")
# element.send_keys(r'C:\Users\dmalinowski\Desktop\screenshot.png')
# time.sleep(5)
# driver.close()

# file explorer 
driver.get('https://www.plupload.com/examples/')
driver.find_element(By.ID,'uploader_browse').click()
time.sleep(3)

path = r'C:\Users\dmalinowski\Desktop\screenshot.png'
keyboard = Controller()
keyboard.type(path)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)

