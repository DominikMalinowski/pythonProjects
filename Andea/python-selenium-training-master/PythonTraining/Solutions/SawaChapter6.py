def nowalista(list):
    del list[5]
    del list[4]
    del list[1]
    list.sort()
    print(list)


print("Wprowadź dane do listy (zmiast przecinków użyj ;). Aby zakończyć wciśnij Enter")
dane = input()

dane2 = dane.replace(" ", "")
print('\n' + dane2)

lista = dane2.split(";")  # ze string'a robi Listę
print('\n')  # oraz usuwa znaki ';' zasępując je pustymi komórkami
print(lista)

lista = list(filter(None, lista))  # usuwa puste komórki z Listy

nowalista(lista)