names = "Karol", "Bartek", "Aleksandra", "Oskar", " Weronika " 
print(names)
print(names[0].upper())
print(names[-2].lower())
print(names[2].title())
print(names[1].upper())
#można dodawać modyfikacje wartości po kropce 
print(names[4].upper().strip())

# f jako ciąg tekstowy, cudzysłów i tekst, zakres, nazwa listy, w kwadratowym pozycja na liscie, zamknąc zakres
print(f"Dzień dobry {names[0].upper()}U")
print(f"Miłego dnia {names[-3].lower()}")
print(f'Pozdrawiam {names[4].title()}')

pojazd = "rower", "samochód", "statek", "szybowiec", "katapulta"
marka = "góral", "maybach", "titanic", "lot", "kapatulta" 
print(f"Chciałbym mieć {pojazd[4]} marki {marka[2].upper()}")

motorcycles = ["honda", "yamaha","suzuki"]
print(motorcycles)

#zmiana wartości w liscie 
motorcycles[0] = "ducati"
print(motorcycles)
#dodawanie rekordów poprzez "append"
motorcycles=["honda", "yamha", "suzuki"]
motorcycles.append('ducati')
print(motorcycles)

motorcycles =[]
motorcycles.append('suzuki')
motorcycles.append('yamaha')
motorcycles.append('honda')

#dodawanie rekordów poprzez "insert"
motorcycles.insert(0, 'ducati')

#usuwanie na stałe rekordów z listy 
del motorcycles[1]
print (motorcycles)

#usuwanie rekordów tymczasowe 
popped_motorcycles=motorcycles.pop()
print(popped_motorcycles)
motorcycles.append('honda')
last_owned = motorcycles.pop(1)
print(last_owned)
motorcycles.append('yamaha')
motorcycles.insert(2, 'suzuki')

#usuwanie rekordu na podstawie jego wartości 
motorcycles.remove('suzuki')
zbyt_drogi='yamaha'
motorcycles.remove(zbyt_drogi)
print(f"\n Zbyt drogi jest dla mnie motor {zbyt_drogi.title()}")

