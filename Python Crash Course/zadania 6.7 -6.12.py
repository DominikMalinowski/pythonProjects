Kitku = {
    "firt_name": "Kitku",
    "last_name": "Kociakowa",
    "age": 18,
    "city": "kielce",
    }

Mietek = {
    "firt_name": "Karol",
    "last_name": "Gałka",
    "age": 25,
    "city": "kielce",
    }

Bartek = {
    "firt_name": "Bartek",
    "last_name": "Rubak",
    "age": 25,
    "city": "kielce",
    }

people = [Kitku,Mietek,Bartek]

for osoba in people:
    print(osoba)

#zadanie 6.8

kot = {
    "rozmiar": "mały",
    "jedzenie": "mięso",
    "udomowiony": "tak",
    }
żyrafa = {
    "rozmiar": "duży",
    "jedzenie": "rośliny",
    "udomowiony": "nie",
    }
owca = {
    "rozmiar": "średni",
    "jedzenie": "rośliny",
    "udomowiony": "tak",
    }

pets =[kot,żyrafa, owca]
for pet in pets: 
    print(pet)

#zadanie 6.9
favorite_places = {
    "ania": ["anglia","hiszpania","australia"], 
    "andrzej": ["japonia","kazahstan","norwegia"],
    "zenon":["rzym", "alaska","meksyk"],
    }
for osoba, miejsca in favorite_places.items():
    print(f'Ulubionymi miejscami użytkownika {osoba.title()} są:')
    for miasta in miejsca:
        print(f'\t {miasta.title()}')

#zadanie 6.10
ulubione_liczby = {
    "Marjan" : [8,13,25],
    "Dominik" : [9],
    "Andrzej" : [5,56],
    "Karol" : [3,56,78,90] ,
    "Ola" : [1],
    }
for osoba, liczby in ulubione_liczby.items():
    if len(liczby) >1:
        print(f'Ulubionymi liczbami użytkownika {osoba.title()} są:')
        for liczba in liczby:
            print(f"\t{liczba}")
    if len(liczby) == 1:
        print(f'Użytkownik {osoba.title()} ma jedną ulubioną liczbę czyli:')
        print(f"\t{liczby[0]}")

#zadanie 6.11
cities = {
    'warszawa': {
        'country':'polska',
        'population':'mała',
        'fact':"była rozjebana",
        },
    'berlin': {
        'country': 'niemcy',
        'population': 'średnia',
        'fact': 'naziści',
        },
    'moskwa': {
        'country': 'rosja',
        'population': 'duża',
        'fact': 'alkoholicy',
        },
    }
for miasta, fakty in cities.items():
    print(f'\nInformacje o mieście {miasta.title()}:')
    kraj = fakty['country']
    populacja = fakty['population']
    fakt = fakty['fact']
    print(f'\tMiasto znajduje się w kraju o nazwie: {kraj.title()}')
    print(f'\tJego populację szacuje się na wartość: {populacja}')
    print(f'\tCiekaweosta o nim to: {fakt}')
    