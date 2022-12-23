"""Import poszczególnych metod z modułu"""
from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('volkswagen','beetle','2019')
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla','roadster','2019')
print(my_tesla.get_descriptive_name())

print(f'\n')

"""Import całego modułu wraz ze wszystkii klasami w środku"""
import car
import electric_car 

my_beetle = car.Car('volkswagen','beetle','2019')
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla','roadster','2019')
print(my_tesla.get_descriptive_name())

print(f'\n')