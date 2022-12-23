class User(): 
    def __init__(self, first_name, last_name, age, sex): 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0 

    def describe_user(self):
        print(f'Witaj, {self.first_name.title()} {self.last_name.title()},twój wiek to {self.age}, a płeć to {self.sex}\n')
    def greet_user(self):
        print(f'Dzień dobry {self.first_name.title()} {self.last_name.title()}')
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'Ilość prób logowania wynosi: {self.login_attempts}')
    def reset_login_attempts(self): 
        self.login_attempts = 0
        print(f'Ilość prób logowania wynosi {self.login_attempts}, bo została wyzerowana')