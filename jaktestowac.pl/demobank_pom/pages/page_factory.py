
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.quick_payment_page import QuiCkPaymentPage
def login(driver):
    return LoginPage(driver)

def home(driver):
    return HomePage(driver)

def quick_payment(driver):
    return QuiCkPaymentPage(driver)