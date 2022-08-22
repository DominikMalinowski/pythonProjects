
# import of selenium and webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def user_login(driver, user_mail, user_pass):
    """
    Method to log in user
    :param driver: path to webdriver instance
    :param user_mail: user email
    :param user_pass: user password
    """
    email_input_field = driver.find_element(By.XPATH, '//*[@type="email"]')
    email_input_field.send_keys(user_mail)

    password_input_field = driver.find_element(By.XPATH, '//*[@type="password"]')
    password_input_field.send_keys(user_pass)

    button_next_element = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
    button_next_element.click()


def use_search_bar(driver, xpath, product_name):
    """
    Method to use search field
    :param driver: webdriver instance
    :param xpath: xpath for search field
    :param product_name: product to search
    """
    search_field = driver.find_element(By.XPATH, xpath)
    search_field.clear()
    search_field.send_keys(product_name, Keys.ENTER)
