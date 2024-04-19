from selenium.webdriver.common.by import By

class HandyWrapper():
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'classname':
            return By.CLASS_NAME
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        else:
            print('Locator type ' + locatorType + ' not supported or incorrect.')
            return False
    
    def getElement(self, locator, locatorType ='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print('Element found')
        except:
            print('Element not found')
        return element

    def isElementPresent(self, locator, byType):
        element = self.driver.find_element(byType,locator)
        if element is not None:
            print('Element has been found')
            return True 
        else:
            print('Element has not been found')
            return False
        
    def isElementPresentCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print('Elements found')
                return True
            else:
                print('Elements has not been found')
                return False
        except:
            print('Elements has not been found')
            return False
