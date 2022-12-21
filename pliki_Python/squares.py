#tworzenie listy składajacej się z kwadratów liczb 1-10
squares =[] #utworzenie pustej listy 
for value in range(1,11): #nadanie zakresu dla Pythona 
	square=value**2 #utworzenie zmiennej square bez s której wartosciami są kwadraty liczb 
	squares.append(square) #doadnie zmiennej square bez s do listy squares 
print(squares) #wyswietlenie listy kwadratów 

#to samo co wyżej z pominięciem tworzenie osobnej zmiennej (zakres od 2 do 15 bez 15, kazda liczba do potegi 3)
squares_2 =[]
for value in range (2,15):
	squares_2.append(value**3)
print(squares_2)

#lista składana - efekt ten sam co wyżej 
squares_3=[value**2 for value in range(1,20)]
print(squares_3)
