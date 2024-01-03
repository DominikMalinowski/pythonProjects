import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class SwitchTo():
    def switch_window(self):
        base_url = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        parent_handle = driver.current_window_handle

        # opening new window
        open_window_button_id = 'openwindow'
        driver.find_element(By.ID, open_window_button_id).click()
        time.sleep(2)
        
        # all handles and switch
        handles = driver.window_handles
        for handle in handles:
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                search_field_xpath = '/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/form/div/input'
                driver.find_element(By.XPATH,search_field_xpath).send_keys('placeholder')
                time.sleep(2)
                driver.close()
                break

        #switch to parent handle 
        driver.switch_to(parent_handle)

        driver.close()

sw = SwitchTo()
sw.switch_window()
