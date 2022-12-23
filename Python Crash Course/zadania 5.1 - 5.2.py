cars = ("subaru", "toyota", "BMW", "renault")
for car in cars:
    if car == "bmw":
        print(f"{car.title()} jest marką niemiecką")
    else:
        print(f"{car.title()} jest inna marką")

#conditiona_test

#sprawdzenie równości i nierówności ciągów tekstowych 
for car in cars: 
    if car == "bmw".upper():
        print("jest dobrze")
    else:
        print("jest zle")

for car in cars:
    if car != "toyota":
        print("nie toyota")
    else:
        print("to jest toyota")

#test z użciem funkcji lower()


#równości i nierówności; większy niż i mniejszy niż; większy niz lub równy i mniejszy niż lub równy; 
wartosci = 14, 56
if wartosci > 18:
    print("wait that's ilegal") 
else:
    print("prokurator")

#test słów kluczowych and i or 

#sprawdzanie elementu na liście 


#sprawdzanie czy elementu nie ma na liście 
