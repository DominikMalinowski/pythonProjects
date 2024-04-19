#zadanie 9.1
class Restaurant(): 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restauracja nazywa się "{self.restaurant_name}"')
        print(f'Restauracja serwuje kuchnię {self.cuisine_type}')

    def open_restaurant(self):
        print("Restauracja otwarta jest od pon. do pt. w godzinach 7:00 - 20:00")

kuciak = Restaurant('w dupie na oto','chińską')
kuciak.describe_restaurant()
kuciak.open_restaurant()

#zadanie 9.2 
baran = Restaurant('tez w dupie','węgierską')
baran.describe_restaurant()

ryba = Restaurant('na oko','fińską')
ryba.describe_restaurant()

rak = Restaurant('pyramyda','egipską')
rak.describe_restaurant()

#zadanie 9.3 
class User(): 
    def __init__(self, first_name, last_name, age, sex): 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    def describe_user(self):
        print(f'Witaj, {self.first_name.title()} {self.last_name.title()},twój wiek to {self.age}, a płeć to {self.sex}')
    def greet_user(self):
        print(f'Dzień dobry {self.first_name.title()} {self.last_name.title()}')

ja = User('dominik','malinowski',25, 'M')
ja.describe_user()
ja.greet_user()        
