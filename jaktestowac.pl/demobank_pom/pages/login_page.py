
class LoginPage:
    def __init__(self, driver):
        self.url = 'https://demobank.jaktestowac.pl/logowanie_etap_2.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def log_in(self, user, password):
        pass
