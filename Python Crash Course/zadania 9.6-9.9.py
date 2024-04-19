#zadanie 9.6 
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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """nie wiem co tu ma byc"""

    def available_flavors(self): 
        flavors = ['czoko','smietankowe','owocowe']
        print(f'Dostępne są lody o nastepującym smaku:')
        for flavor in flavors:
            print(f'\t{flavor}')

blowjob = IceCreamStand('burdel','polską')
blowjob.available_flavors()

#zadanie 9.7 
from user import User



#    def show_privileges(self):
#        privileges = ['może dodać post','może usunąć post','może zbanować użytkownika']
#        print("Admin może wykonać nast. akcje:")
#        for privilege in privileges:
#            print(f'\t- {privilege}')

#my_admin = Admin('zenon','kowalczyk',35,'m')
#my_admin.greet_user()
#my_admin.show_privileges()

#zadanie 9.8 
class Privileges():
    def __init__(self):
        """Inicjalizacja klasy"""
        
    def show_privileges(self):
        privileges = ['może dodać post','może usunąć post','może zbanować użytkownika']
        print("Admin może wykonać nast. akcje:")
        for privilege in privileges:
            print(f'\t- {privilege}')

class Admin(User):

    privileges = Privileges()

    def __init__(self, first_name, last_name, age, sex):
        """Inicjalizacja klasy podrzędnej - Admin"""
        super().__init__(first_name,last_name, age, sex)
        """Inicjalizacja klasy nadrzędnej (superklasy) - User"""
        
you_admin = Admin('janina','kowalewska',45,'f')
you_admin.privileges.show_privileges()

#zadanie 9.9
class Car(): 
    """Prosta próba zaprezentowania samochodu"""
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self): 
        """Zwrot elegancko sformatowanego opisu samochodu"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informacje o przebiegu samochodu"""
        print(f"Ten samochód ma przejechane {self.odometer_reading}km")

    def update_odometer(self, mileage):
        """Przypisanie podanej wartości licznikowi przebiegu samochodu
            zmiana zostanie odrzucona w przypadku próby cofniecia licznika"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąc licznikia)")

    def increment_odometer(self, kilometers):
        """Inkrementacja wartości licznika przebiegu samochodu o podaną wartość"""
        self.odometer_reading += kilometers

class Battery():
    """Prosta próba modelowania akumulatora samochodu elektrycznego"""
    def __init__(self, battery_size = 75):
        """Inicjalizacja atrybutów akumulatora"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora"""
        print(f'Ten samochód ma akumulator o pojeności {self.battery_size} kWh')

    def upgrade_battery(self):
        if self.battery_size != 100: 
            self.battery_size = 100

class ElectricCar(Car):
    """Przedstawai cechy charakterystyczne samochodu elektrycznego"""
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów klasy nadrzędnej. 
        Nastepnie inicjalizacja atrybutów charakterystycznych dla 
        samochodu elektrycznego."""
        super().__init__(make,model,year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

second_tesla = ElectricCar('tesla','model k', 2018)

second_tesla.battery.describe_battery()
second_tesla.battery.upgrade_battery()
second_tesla.battery.describe_battery()
