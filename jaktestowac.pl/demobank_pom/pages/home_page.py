
class HomePage:
    def __init__(self, driver):
        self.url = 'https://demobank.jaktestowac.pl/pulpit.html'
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)

    def get_messages_text(self):
        pass
