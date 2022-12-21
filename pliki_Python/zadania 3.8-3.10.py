swiat = ['rosja', 'ameryka', 'japonia', 'kazachstan', 'rpa']
print("początkowa lista:")
print(swiat)

print("Tymczasowo posortowana lista:")
print(sorted(swiat))

print('znowu lista początkowa:')
print(swiat)

#sorotowanie odwrotne z fukncji sorted
print('posortowana odwrotnie lista')
print(sorted(swiat, reverse=True))

#zmiana kolejnosci listy
print("zmiana kolejnosci listy")
swiat.reverse()
print(swiat)

#powrót listy do starej kolejności 
print("powrót do starej kolejnosci")
swiat.reverse()
print(swiat)

#alfabetycznie posortowan lista 
print('alfabetycznie posortowana lista')
swiat.sort()
print(swiat)

#alfabetycznie odwortnie posortowana lista 
print('odwrotnie anlfabetycznie posortowan lista')
swiat.sort(reverse=True)
print(swiat)

#zadanie 3.9 jeswt zrobione w pliku z zadniami 3.4-3.7

#zadanie 3.10 - nowa lista 
print('Tutaj zaczyna sie zadanie 3.10')
jezyki=['hiszpański','chiński', 'angielski', 'włoski', 'rosyjski']
#wyswietlanie konkretnego rekordu z listy 
print(jezyki[3].upper())
#użycie rekordu z listy w ciagu tekstowym 
print(f'Obecnie uczę się nowego języka, kórym jest język {jezyki[0]}')
#dodawanie rekordów do listy
jezyki.append('nowerski')
#wstawianie elementów na liste 
jezyki.insert(3, 'niemiecki')
print(jezyki)
#pernamentne usuwanie elementów z listy 
del jezyki[1]
print(jezyki)
#wyciąganie elementów z listy 
poped_jezyki = jezyki.pop(4)
print('Jezyki poped')
print(poped_jezyki)
print(jezyki)
#usuniecie elementu na podstawie jesgo wartosci 
jezyki.remove('angielski')
#trwałe sortowanie listy 
jezyki.sort()
print(jezyki)
#tymczasowe sortowanie listy + sortowanie odwrotnie niz alfabetycznie 
print(sorted(jezyki, reverse=True))
