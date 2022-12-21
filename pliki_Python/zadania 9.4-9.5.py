#zadanie 9.4 
class Restaurant(): 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restauracja nazywa się "{self.restaurant_name}"')
        print(f'Restauracja serwuje kuchnię {self.cuisine_type}')

    def open_restaurant(self):
        print("Restauracja otwarta jest od pon. do pt. w godzinach 7:00 - 20:00")

    def served(self):
        print(f'Restauracja obsłużyła {self.number_served} osób')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment): 
        self.number_served += increment

kuciak = Restaurant('w dupie na oto','chińską')
kuciak.describe_restaurant()
kuciak.open_restaurant()

restaurant = Restaurant('PizzaFast','włoska')
restaurant.served()

"""bezpośrednie nadawnie wartości"""
restaurant.number_served = 15
restaurant.served()

"""nadanie wartości z wykorzystaniem metody"""
restaurant.set_number_served(34)
restaurant.served()

restaurant.set_number_served(2346)
restaurant.served()

"""nadanie wartości poprzez inkrementację"""
restaurant.increment_number_served(475)
restaurant.served()

restaurant.increment_number_served(234567)
restaurant.served()

#zadanie 9.5
class User(): 
    def __init__(self, first_name, last_name, age, sex): 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0 

    def describe_user(self):
        print(f'Witaj, {self.first_name.title()} {self.last_name.title()},twój wiek to {self.age}, a płeć to {self.sex}')
    def greet_user(self):
        print(f'Dzień dobry {self.first_name.title()} {self.last_name.title()}')
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'Ilość prób logowania wynosi: {self.login_attempts}')
    def reset_login_attempts(self): 
        self.login_attempts = 0
        print(f'Ilość prób logowania wynosi {self.login_attempts}, bo została wyzerowana')

ja = User('dominik','malinowski',25, 'M')
ja.describe_user()
ja.greet_user()        

ja.increment_login_attempts()
ja.reset_login_attempts()

ty = User('Jan','kowalski','45','M')
ty.greet_user()
ty.increment_login_attempts()
ty.increment_login_attempts()
ty.increment_login_attempts()
ty.reset_login_attempts()
print(ty.login_attempts)