#sortowanie listy 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#sorotowanie listy w kolejnosci odwrotnie alfabetycznej 
cars.sort(reverse=True)
print(cars)

#sortowanie listy tymczasowe 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Oto lista początkowa:')
print(cars)

print('Oto lista posortowana:')
print(sorted(cars))

print("Znowu lista nieposortowana:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
#odwracanie zawartości listy 
cars.reverse()
print(cars)
cars.reverse()
print(cars,"\n")

#okreslanie rozmiaru listy czyli ilosc rekordów
len(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

