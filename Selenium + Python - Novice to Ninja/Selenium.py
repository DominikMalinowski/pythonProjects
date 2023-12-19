
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def diff_action(path):
    chromeDriver_path = 'C:\ChromeDriver\chromedriver.exe'
    driver = webdriver.Chrome(service=Service(chromeDriver_path))
    driver.get(path)

    # get page title 
    title = driver.title
    print('Page title is: ' + title)

    # browser refresh 
    driver.refresh()
    driver.maximize_window()

    # click the element 
    # select_class_example_dropdown_id = 'carselect'
    # dropdown = driver.find_element(By.ID,select_class_example_dropdown_id)
    # select_element = Select(dropdown)
    # select_element.select_by_value('benz')
    # time.sleep(2)
    # select_element.select_by_index(2)
    # time.sleep(2)
    # select_element.select_by_visible_text('BMW')
    # time.sleep(2) 
    # dropdown.click()

    # # waiting for element 
    # multiple_select_example_id = 'multiple-select-example'

    # wait = WebDriverWait(driver,timeout= 10, poll_frequency=1,ignored_exceptions=
    #                      [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
    
    # element = wait.until(EC.visibility_of_element_located((By.ID, multiple_select_example_id)))

    # autocomplete field
    

    


    # # typing in text field 
    # auto_suggest_example_text_field_id = 'autosuggest'
    # auto_suggest_text_field = driver.find_element(By.ID,auto_suggest_example_text_field_id)
    # auto_suggest_text_field.send_keys('placeholder')

    # # 3s wait to see action
    # time.sleep(3)
    # auto_suggest_text_field.clear()
    # time.sleep(3)

    # # check and change element state 
    # enable_button_id = 'enabled-button'
    # disable_button_id = 'disabled-button'
    # enable_disable_field_id = 'enabled-example-input'

    # enable_button = driver.find_element(By.ID, enable_button_id)
    # disable_button = driver.find_element(By.ID, disable_button_id)
    # enable_disable_field = driver.find_element(By.ID, enable_disable_field_id)

    # button_status = enable_disable_field.is_enabled()
    # print(button_status) 

    # disable_button.click()
    # button_status = enable_disable_field.is_enabled()
    # print(button_status)
    
    # enable_button.click()
    # button_status = enable_disable_field.is_enabled()
    # print(button_status)        

    # # list of elements 
    # radiobutton_list_xpath = '//*[@type="radio"]'
    # radio_button_list = driver.find_elements(By.XPATH,radiobutton_list_xpath)

    # for radio_button in radio_button_list:
    #     is_selected = radio_button.is_selected()

    #     if not is_selected:
    #         radio_button.click()
    #         time.sleep(1)

    # # hidden element 

    # hide_button_id = 'hide-textbox'
    # show_button_id = 'show-textbox'
    # hidden_field_id = 'displayed-text'

    # hide_button = driver.find_element(By.ID, hide_button_id)
    # show_button = driver.find_element(By.ID, show_button_id)
    # hidden_field = driver.find_element(By.ID, hidden_field_id)

    # hidden_field_state = hidden_field.is_displayed()

    # print('Text is visible ?')
    # print(hidden_field.is_displayed())

    # hide_button.click()
    # print('Text is visible ?')
    # print(hidden_field.is_displayed())

    # show_button.click() 
    # print('Text is visible ?')
    # print(hidden_field.is_displayed())

    # # getting attribute 
    # open_window_button_id = 'openwindow'   
    # open_window_button = driver.find_element(By.ID, open_window_button_id)
    # on_click_attribute = open_window_button.get_attribute('onclick')
    # print(on_click_attribute)

    driver.back()
    driver.forward()

    driver.quit()

website_path = 'https://www.letskodeit.com/practice'
diff_action(website_path)