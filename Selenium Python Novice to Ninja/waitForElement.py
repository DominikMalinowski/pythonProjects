
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
from HandyWrappers import HandyWrapper

class ExplicitWaitType():
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrapper

    def waitForElement(self, locator, locatorType ='id', timeout = 10, pollFrequency = 0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print('Waiting for maximum ::' + str(timeout) + ' :: second for element to be clickable')

            wait = WebDriverWait(self.driver, timeout= timeout, poll_frequency=pollFrequency, ignored_exceptions=
                         [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            print('Element appeared on the web page')
        except:
            print('Element not appeared on the web page')
            print_stack()
        return element

    
    
