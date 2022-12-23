#zadanie 7.1 
marka = input("Jakiej marki samochód chciałbyś wypozyczyć ?")
print(f"Chwileczkę, sprawdzę czy mamy dostępny samochód marki {marka}")

#zadanie 7.2
stolik = input("Na ile osób chcesz zarezerwować stolik ?")
stolik = int(stolik)

if stolik >= 8:
    print("Proszę poczekać na wolny stolik")
else: 
    print("Stolik jest gotowy")

#zadanie 7.3 
liczba = input("Prosze podać dowolną liczbę")
liczba = int(liczba)
if liczba % 10 ==0:
    print("Ta lcizba jest wielokrotnością 10-ciu")
else:
    print("Ta liczba nie jest wielokrotnoscią 10-ciu")