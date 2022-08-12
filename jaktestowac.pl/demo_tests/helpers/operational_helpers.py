import time
from selenium.webdriver.common.by import By


def wait_for_elements(driver, xpath, max_seconds_to_wait=5, number_of_expected_elements=1):
    """
    Checking every second if list of elements under specified xpath was found
    :param driver: path for selenium driver
    :param xpath: xpath for list of elements
    :param max_seconds_to_wait: maximum time in seconds to wait for element (default: 5)
    :param number_of_expected_elements: specifies minimum number of  elements to be found
    """
    for seconds in range(max_seconds_to_wait):
        elements = driver.find_elements(By.XPATH, xpath)

        print(f'Waiting time: {seconds} s')

        if len(elements) >= number_of_expected_elements:
            return elements

        if seconds == (max_seconds_to_wait - 1):
            print('End of wait')
            assert len(elements) >= number_of_expected_elements, \
                f'Expected {number_of_expected_elements} elements but found {len(elements)} ' \
                f'for xpath {xpath} in time of {max_seconds_to_wait}s'
        time.sleep(1)
