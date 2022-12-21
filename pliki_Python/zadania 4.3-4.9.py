#zadanei 4.3 
#for values in range(1,21):
#	print(values)

#zadanie 4.4 
#milion=list(range(1,1000001))
	#print(milion)

#zadanie 4.5 - sumowanie do miliona 
#milion = list(range(1,1000001)) #zapisanie do listy liczb z zakresu od jednego do miliona 
#print(min(milion), max(milion)) #wyświetlenie minimalnej i maxymalnej wartości ze zbioru "milion"
#print(sum(milion)) #wyświetlenie zsumowanej zawartości listy "milion"

#zadanie 4.6
#odd=(list(range(1,21,2)))
#for odd in range(1,21,2):
#	print(odd)

#zadanie 4.7 
#squares_3=[] #utworzenie pustej listy 
#for values in range(3,30): #dla zmiennej values w zakresie od 3 do 30 wykonaj:
#	square_3 = values**3 #utwórz zmienna square_3 gdzie zmienna values bedzie podnoszona do 3 potęgi 
#	squares_3.append(square_3) #do listy squares_3 dodaj zmienną square_3 
#print(squares_3) #wyświetl liste squares_3 

#zadanie 4.8 
for values in range(1,11):
	print(values**3)

#zadanie 4.9 
potega=[ values**3 for values in range(1,11)]
print(potega)
