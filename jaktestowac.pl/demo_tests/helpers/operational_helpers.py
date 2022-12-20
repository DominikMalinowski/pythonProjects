import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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


def visibility_of_element_wait(driver, xpath, timeout=3) -> WebElement :
    """
    Checking if single element specyfi by xpath is visible on the page
    :param driver: webdriver or event firing webdriver instance
    :param xpath: xpath for element
    :param timeout: how long system will wait in seconds for element (default = 5s)
    :return: element if it was visible
    """
    error_message = f'Element for xpath: {xpath}, and page {driver.current_url} has not been found in time of {timeout}s'
    locator = (By.XPATH, xpath)
    element_located = EC.visibility_of_element_located(locator)
    # wait = WebDriverWait(driver, timeout) # using EventFiringWebDriver
    if hasattr(driver, 'wrapped_driver'):
        unwrapped_driver = driver.wrapped_driver
        wait = WebDriverWait(unwrapped_driver, timeout)
    else:
        wait = WebDriverWait(driver, timeout)

    return wait.until(element_located, error_message)
