"""
Zestw klas przeznaczonych do zaprezentowania samochodu, 
zarówno o napędzie tradycyjnym, jak i elektrycznym
"""

class Car():
    """Prosta próba zaprezentowania samochcoud"""
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

#my_new_car = Car('audi','a4','2019')
#print(my_new_car.get_descriptive_name())

"""bezpośrednia modyfikacaj wartości atrybutu"""
#my_new_car.odometer_reading = 23 
#my_new_car.read_odometer()

"""modyfikacja wartości atrybutu za pomocą metody"""
#my_new_car.update_odometer(35) # 
#my_new_car.read_odometer()

"""inkrementacja wartości atrybutu za pomocą metody"""
#my_new_car.increment_odometer(22)
#my_new_car.read_odometer()
