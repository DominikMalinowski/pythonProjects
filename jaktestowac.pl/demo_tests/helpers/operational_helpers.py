import time
from selenium.webdriver.common.by import By

def wait_for_elments(driver, xpath):
    """
    Checking every second if list of elements under specified xpath is greater than 0
    :param driver: path for selenium driver
    :param xpath: xpath for list of elements
    """
    for second in range(5):
        elements = driver.find_elements(By.XPATH, xpath)
        number_of_founded_elements = len(elements)

        print(f'Waiting time: {second} s')

        if number_of_founded_elements > 0:
            print('Element found')
            print(f'System found: {number_of_founded_elements} \n')
            return elements
        time.sleep(1)