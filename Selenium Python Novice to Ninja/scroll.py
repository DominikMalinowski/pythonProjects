
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By

class ScrollingElement():
    def scroll(self):
        path = 'https://www.letskodeit.com/practice'

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(path)
        # driver.implicitly_wait(3)

        # scroll down 
        driver.execute_script("window.scrollBy(0,500)")
        time.sleep(3)

        # scroll up
        driver.execute_script("window.scrollBy(0,-500)")
        time.sleep(3)

        # scroll into element 
        mouse_hover_element = driver.find_element(By.ID, 'mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);", mouse_hover_element)
        time.sleep(3)

        # native way to scroll 
        driver.refresh()
        driver.execute_script("window.scrollBy(0,-1000);")
        mouse_hover_element = driver.find_element(By.ID, 'mousehover')
        location = mouse_hover_element.location_once_scrolled_into_view
        print(location)

        driver.quit()

se = ScrollingElement()
se.scroll()