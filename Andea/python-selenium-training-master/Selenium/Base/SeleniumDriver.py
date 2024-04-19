from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui as UI
from selenium.common.exceptions import *
import Selenium.Utilities.Logger as ml


class SeleniumDriver:
    """
    SeleniumDriver class stores all methods that can be used for proper selenium webdriver's behaviour.
    Also Selenium WebDriver is created here.
    """

    # Create logger object
    logs = ml.MESlogger()

    def __init__(self, driver):
        self.driver = driver


    def getTitle(self):
        """ Return title of the page """
        return self.driver.title

    # def getElement(self, locator):
    #     """ Return element for given locator and locator type """
    #     element = None
    #     try:
    #         element = self.driver.find_element(locator)
    #         self.logs.info("Element Found. Locator: " + str(locator))
    #     except Exception as ex:
    #         self.logs.warning("Element not found. Locator: " + str(locator) + "\nFollowing exception has been occured: " + str(ex))
    #     return element

    def elementClick(self, locator, timeout=7):
        """ Click element for given locator and locator type """
        try:
            element = self.waitForElement(locator=locator, timeout=timeout, pollFrequency=0.5)
            element.click()
            self.logs.info("Clicked on element with locator: " + str(locator))
        except Exception as ex:
            self.logs.error("Cannot click on the element with locator: " + str(locator) + "\nFollowing exception has been occured: " + str(ex))

    def sendKeys(self, data, locator, timeout=7):
        """ Send given data to element with given locator and locator type """
        try:
            element = self.waitForElement(locator=locator, timeout=timeout, pollFrequency=0.5)
            element.clear()
            element.send_keys(data)
            self.logs.info("Sent to element with locator: " + str(locator))
        except Exception as ex:
            self.logs.error("Cannot send data to the element with locator: " + str(locator) + "\nFollowing exception has been occured: " + str(ex))

    def isElementPresent(self, locator, timeout=7):
        """ Return True if element with given locator and locator type exists, False if not """
        try:
            element = self.waitForElement(locator=locator, timeout=timeout, pollFrequency=0.5)
            if element is not None:
                self.logs.info("Element Found")
                return True
            else:
                self.logs.warning("Element not found")
                return False
        except Exception as ex:
            self.logs.error("Element not found. \nFollowing exception has been occured: " + str(ex))
            return False

    def isElementVisible(self, locator, timeout=7):
        """ Return True if element with given locator and locator type is visible, False if not """
        try:
            if self.waitForElement(locator=locator, timeout=timeout, pollFrequency=0.5).is_displayed():
                self.logs.info("Element is visible (" + str(locator) + ")")
                return True
            else:
                self.logs.warning("Element is not visible (" + str(locator) + ")")
                return False
        except Exception as ex:
            self.logs.warning("Element is not visible\nException occured: " + str(ex))

    def areElementsPresent(self, *locators):
        """ Return True if all elements for given locators and one locator type exist, False if not """
        results = []
        try:
            for locator in locators:
                element = self.waitForElement(locator=locator, timeout=7, pollFrequency=0.5)
                if element is not None:
                    results.append("YES")
                    self.logs.info("Element has been found. Locator: '" + str(locator))
                else:
                    results.append("NO")
                    self.logs.warning("Element has NOT been found. Locator: '" + str(locator))
        except Exception as ex:
               self.logs.error("Cannot execute 'areElementsPresent' method. Exception occured." + "\nException message: " + str(ex))

        if "NO" in results:
            self.logs.info("One of required elements has NOT been found")
            return False
        else:
            self.logs.info("All required elements have been found")
            return True

    def getElementText(self, locator, timeout=7):
        """ Return text of element """
        try:
            text = self.waitForElement(locator=locator, timeout=timeout, pollFrequency=0.5).text
            self.logs.info("Text value from element has been received. Text: " + text)
            return text
        except Exception as ex:
            self.logs.error("Cannot get text value from element. Locator: " + str(locator) + "\nException occured: " + str(ex))
            return None

    def waitForElement(self, locator, timeout=7, pollFrequency=0.5):
        """ Return element if it is visible. Wait max for <timeout> """
        element = None
        try:
            self.logs.info("Waiting for element. Max time: " + str(timeout) + " seconds. ")
            wait = WebDriverWait(self.driver, timeout, pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located(locator))
            self.logs.info("Element appeared on the web page (" + str(locator) + ")")
        except:
            self.logs.error("Element not appeared on the web page")
        return element

    def waitForElementText(self, locator, expected_text, timeout=7, pollFrequency=0.5):
        """ Wait for available element """
        try:
            self.logs.info("Waiting for element text (max " + str(timeout) + " seconds)")
            WebDriverWait(self.driver, timeout, pollFrequency).until(EC.text_to_be_present_in_element(locator, expected_text))
        except Exception as ex:
            self.logs.error("Waiting for element text has been failed\nException occured: " + str(ex))

    def getAllDropdownOptions(self, locator, timeout=7):
        """ Return all options from dropdown """
        options = []
        try:
            element = self.waitForElement(locator=locator, timeout=timeout, pollFrequency=0.5)
            select = UI.Select(element)

            for option in select.options:
                options.append(option.text)
                self.logs.info("New option from dropdown (locator: '" + str(locator) + ") has been received: " + option.text)

        except Exception as ex:
            self.logs.error("Cannot get options from dropdown. Locator: " + str(locator) + "\nException: " + str(ex))

        return options

    def setDropdownOptionByText(self, locator, value, timeout=7):
        """ Set value on dropdown by text """
        try:
            element = self.waitForElement(locator=locator, timeout=timeout, pollFrequency=0.5)
            select = UI.Select(element)

            select.select_by_visible_text(value)
            self.logs.info("Value (" + value + ") has been set on dropdown (" + str(locator) + ")")
        except Exception as ex:
            self.logs.error("Cannot set value (" + value + ") on dropdown (" + str(locator) + ")\nException occured: " + str(ex))

    def checkIsCheckboxSelected(self, locator, timeout=7):
        """ Return True if checkbox is selected, False if not """
        try:
            element = self.waitForElement(locator=locator, timeout=timeout, pollFrequency=0.5)

            if element.is_selected():
                self.logs.info("Checkbox (" + str(locator) + ") has been found as selected")
                return True
            else:
                self.logs.error("Checkbox (" + str(locator) + ") has been found as NOT selected")
                return False
        except Exception as ex:
            self.logs.error("Cannot check if checkbox (" + str(locator) + ") is selected. Exception occured: " + str(ex))

    def switchToStandardFrame(self, iframe_locator, timeout=7):
        """ Switch to given iframe """
        #iframe = self.waitForElement(locator=(By.XPATH, "//iframe[@class='apr-fullscreen-tab']"), timeout=timeout, pollFrequency=0.5)
        #iframe = self.waitForElement(locator=(By.XPATH, "//iframe[@class='apr-screen-frame-with-bar']"), timeout=timeout, pollFrequency=0.5)

        iframe = self.waitForElement(locator=iframe_locator, timeout=timeout, pollFrequency=0.5)

        self.driver.switch_to.frame(iframe)

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()

    def clickElementFromList(self, locator, element_index):
        """
        Create list of all elements with given locator and click on the chosen one
        :param locator: locator of element
        :param element_index: index of the element to click on
        """
        try:
            # Get string containing xpath from locator
            locator = str(locator)
            locator_list = locator.split(",")
            xpath = locator_list[1].strip("\") ")

            list_of_elements = self.driver.find_elements_by_xpath(xpath)
            list_of_elements[element_index].click()
            self.logs.info("Clicked on element no " + str(element_index) + " from list with locator: (\"" + locator + "\")")
        except Exception as ex:
            self.logs.error("Cannot click on element no " + str(element_index) + " from list with locator: (\"" + locator + "\")" + "\nException occured: " + str(ex))

    def getTextFromList(self, locator, element_index):
        """
        Create list of all elements with given locator and obtain text from the chosen one
        :param element_index: index of the element to get the text from
        :param locator: locator of element
        :return text from element
        """
        text = None
        try:
            # Get string containing xpath from locator
            locator = str(locator)
            locator_list = locator.split(",")
            xpath = locator_list[1].strip("\") ")

            list_of_elements = self.driver.find_elements_by_xpath(xpath)
            text = list_of_elements[element_index].get_attribute("value")
            self.logs.info("Text value from element no " + str(element_index) + " has been received. Text: " + text)
        except Exception as ex:
            self.logs.error("Cannot get Text from element no " + str(element_index) + " from list with locator: (\"" + locator + "\")" +
                            "\nException occured: " + str(ex))
        return text

    def getNumberOfElements(self, locator):
        """
        Create list of all elements with given locator, and obtains its length
        :param locator: locator of element
        :return: number of elements with given xpath
        """
        number_of_elements = None
        try:
            # Get string containing xpath from locator
            locator = str(locator)
            locator_list = locator.split(",")
            xpath = locator_list[1].strip("\") ")

            list_of_elements = self.driver.find_elements_by_xpath(xpath)
            number_of_elements = len(list_of_elements)
            self.logs.info("Number of elements = " + str(number_of_elements) + ", locator: (\"" + locator + "\")")
        except Exception as ex:
            self.logs.error("Cannot get number of elements with locator: (\"" + locator + "\")" +
                            "\nException occured: " + str(ex))
        return number_of_elements

    def getElementAttribute(self, locator, attribute):
        """
        Obtain value of specified attribute from element with given locator
        :param locator: locator of element
        :param attribute: name of the attribute
        :return: value of attribute
        """
        element_attribute = None
        try:
            # Get string containing xpath from locator
            locator = str(locator)
            locator_list = locator.split(",")
            xpath = locator_list[1].strip("\") ")

            element = self.driver.find_element_by_xpath(xpath)
            element_attribute = element.get_attribute(attribute)
            self.logs.info("Value of attribute \"" + attribute + "\" has been received. Value: " + element_attribute)
        except Exception as ex:
            self.logs.error("Cannot get value of attribute \"" + attribute + "\" for element with locator: (\"" + locator + "\")" +
                            "\nException occured: " + str(ex))

        return element_attribute















                                                                ########## OLD VERSION ##########
#from selenium.webdriver.common.by import By
#from traceback import print_stack
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support import ui as UI
#from selenium.common.exceptions import *
#import Selenium.Utilities.Logger as ml
#from selenium import webdriver
#import os
#from os.path import dirname
#
#class SeleniumDriver():
#    """
#    SeleniumDriver class stores all methods that can be used for proper selenium webdriver's behaviour.
#    Also Selenium WebDriver is created here.
#    """
#
#    # Create logger object
#    logs = ml.MESlogger()
#
#    # Create Selenium WebDriver (it's static, so there is only one driver per all Tests)
#    try:
#        driverLocation = dirname(__file__) + "\\SeleniumDrivers\\IEDriverServer.exe"
#        os.environ["webdriver.ie.driver"] = driverLocation
#        driver = webdriver.Ie(driverLocation)
#        #TODO: is implicitly wait needed? check it. //Checked - probably only explicitly should be used (it's better)
#        driver.implicitly_wait(2)
#        driver.maximize_window()
#        logs.info("IE WebDriver has been created - implicitly wait set, maximize window")
#    except Exception as ex:
#        logs.error("IE WebDriver creating has been failed. Exception occured: " + str(ex))
#
#    def getTitle(self):
#        """ Return title of the page """
#        return self.driver.title
#
#    def getByType(self, locatorType):
#        """ Return proper locator type  """
#        locatorType = locatorType.lower()
#        if locatorType == "id":
#            return By.ID
#        elif locatorType == "name":
#            return By.NAME
#        elif locatorType == "xpath":
#            return By.XPATH
#        elif locatorType == "css":
#            return By.CSS_SELECTOR
#        elif locatorType == "class":
#            return By.CLASS_NAME
#        elif locatorType == "link":
#            return By.LINK_TEXT
#        else:
#            self.logs.error("Locator type " + locatorType + " not correct/supported")
#        return False
#
#    def getElement(self, locator, locatorType="xpath"):
#        """ Return element for given locator and locator type """
#        element = None
#        try:
#            locatorType = locatorType.lower()
#            byType = self.getByType(locatorType)
#            element = self.driver.find_element(byType, locator)
#            self.logs.info("Element Found. Locator: " + locator + " and LocatorType: " + locatorType)
#        except Exception as ex:
#            self.logs.warning("Element not found. Locator: " + locator + " and LocatorType: " + locatorType + "\nFollowing exception has been occured: " + str(ex) )
#        return element
#
#    def elementClick(self, locator, locatorType="xpath"):
#        """ Click element for given locator and locator type """
#        try:
#            element = self.getElement(locator, locatorType)
#            element.click()
#            self.logs.info("Clicked on element with locator: " + locator + " and locatorType: " + locatorType)
#        except Exception as ex:
#            self.logs.error("Cannot click on the element with locator: " + locator + " and locatorType: " + locatorType + "\nFollowing exception has been occured: " + str(ex))
#
#    def sendKeys(self, data, locator, locatorType="xpath"):
#        """ Send given data to element with given locator and locator type """
#        try:
#            element = self.getElement(locator, locatorType)
#            element.clear()
#            element.send_keys(data)
#            self.logs.info("Sent to element with locator: " + locator + " and locatorType: " + locatorType)
#        except Exception as ex:
#            self.logs.error("Cannot send data to the element with locator: " + locator + " and locatorType: " + locatorType + "\nFollowing exception has been occured: " + str(ex))
#
#    def isElementPresent(self, locator, locatorType="xpath"):
#        """ Return True if element with given locator and locator type exists, False if not """
#        try:
#            element = self.getElement(locator, locatorType)
#            if element is not None:
#                self.logs.info("Element Found")
#                return True
#            else:
#                self.logs.error("Element not found")
#                return False
#        except Exception as ex:
#            self.logs.error("Element not found. \nFollowing exception has been occured: " + str(ex))
#            return False
#
#    def isElementVisible(self, locator, locator_type="xpath"):
#        """ Return True if element with given locator and locator type is visible, False if not """
#        try:
#            if self.getElement(locator).is_displayed():
#                self.logs.info("Element is visible (" + locator + ")")
#                return True
#            else:
#                self.logs.warning("Element is not visible (" + locator + ")")
#                return False
#        except Exception as ex:
#            self.logs.warning("Element is not visible\nException occured: " + str(ex))
#
#    """ Check if all sent elements are visible. Can be execute only for the same locator type """
#    def areElementsPresent(self, locator_type="xpath", *locators):
#        """ Return True if all elements for given locators and one locator type exists, False if not """
#        results = []
#        try:
#            for locator in locators:
#                element = self.getElement(locator, locator_type)
#                if element is not None:
#                    results.append("YES")
#                    self.logs.info("Element has been found. Locator: '" + locator + "', using type: " + locator_type)
#                else:
#                    results.append("NO")
#                    self.logs.warning("Element has NOT been found. Locator: '" + locator + "', using type: " + locator_type)
#        except Exception as ex:
#               self.logs.error("Cannot execute 'areElementsPresent' method. Exception occured." + "\nException message: " + str(ex))
#
#        if "NO" in results:
#            self.logs.info("One of required elements has NOT been found")
#            return False
#        else:
#            self.logs.info("All required elements have been found")
#            return True
#
#    def getElementText(self, locator, locator_type="xpath"):
#        """ Return text of element """
#        try:
#            text = self.getElement(locator, locator_type).text
#            self.logs.info("Text value from element has been received. Text: " + text)
#            return text
#        except Exception as ex:
#            self.logs.error("Cannot get text value from element. Locator: " + locator + ", using type: " + locator_type + "\nException occured: " + str(ex))
#            return None
#
#    def waitForElement(self, locator, locatorType="xpath",
#                       timeout=5, pollFrequency=0.5):
#        """ Return element if it is visible. Wait max for <timeout> """
#        element = None
#        try:
#            byType = self.getByType(locatorType)
#            self.logs.info("Waiting for maximum :: " + str(timeout) +
#                          " :: seconds for element to be clickable")
#            wait = WebDriverWait(self.driver, timeout, pollFrequency,
#                                 ignored_exceptions=[NoSuchElementException,
#                                                     ElementNotVisibleException,
#                                                     ElementNotSelectableException])
#            element = wait.until(EC.visibility_of_element_located((byType, locator)))
#            self.logs.info("Element appeared on the web page (" + locator + ")")
#        except:
#            self.logs.error("Element not appeared on the web page")
#        return element
#
#    #TODO: do poprawienia, szukamy tekst jest obecnie staly
#    def waitForElementText(self, locator, locator_type="xpath", timeout=5, pollFrequency=0.5):
#        """ Wait for available element """
#        try:
#            by_type = self.getByType(locator_type)
#            self.logs.info("Waiting for element (max " + str(timeout) + " seconds)")
#            WebDriverWait(self.driver, timeout, pollFrequency).until(EC.text_to_be_present_in_element((locator_type, locator), "Released"))
#        except Exception as ex:
#            self.logs.error("Waiting for element text has been failed\nException occured: " + str(ex))
#
#    def getAllDropdownOptions(self, locator, locator_type="xpath"):
#        """ Return all options from dropdown """
#        options = []
#        try:
#            element = self.getElement(locator, locator_type)
#            select = UI.Select(element)
#
#            for option in select.options:
#                options.append(option.text)
#                self.logs.info("New option from dropdown (locator: '" + locator + "', using type: " + locator_type + ") has been received: " + option.text)
#
#        except Exception as ex:
#            self.logs.error("Cannot get options from dropdown. Locator: " + locator + ", type: " + locator_type + "\nException: " + str(ex))
#
#        return options
#
#    def setDropdownOptionByText(self, locator, value, locator_type="xpath"):
#        """ Set value on dropdown by text """
#        try:
#            element = self.getElement(locator, locator_type)
#            select = UI.Select(element)
#
#            select.select_by_visible_text('')
#            self.logs.info("Value (" + value + ") has been set on dropdown (" + locator + ")")
#        except Exception as ex:
#            self.logs.error("Cannot set value (" + value + ") on dropdown (" + locator + ")\nException occured: " + str(ex))
#
#    def checkIsCheckboxSelected(self, locator, locator_type="xpath"):
#        """ Return True if checkbox is selected, False if not """
#        try:
#            element = self.getElement(locator, locator_type)
#
#            if element.is_selected():
#                self.logs.info("Checkbox (" + locator + ") has been found as selected")
#                return True
#            else:
#                self.logs.error("Checkbox (" + locator + ") has been found as NOT selected")
#                return False
#        except Exception as ex:
#            self.logs.error("Cannot check if checkbox (" + locator + ") is selected. Exception occured: " + str(ex))
#
#    def switchToStandardFrame(self):
#        iframe = self.getElement("//iframe[@class='apr-fullscreen-tab']")
#        self.driver.switch_to.frame(iframe)
#
#    def switchToDefaultContent(self):
#        self.driver.switch_to.default_content()