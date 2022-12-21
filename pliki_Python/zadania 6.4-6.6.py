#zadanie 6.4 - glosariusz_2
glosariusz = {
    "pętla": "powtórzenie",
    "iteracja": "przejście przez",
    "blok kodu": "frakment kodu zapisany po 'for'",
    "zmienna": "obiekt w kodowaniu który ma wartość możliwą do zmiany",
    "wcięcie": "obszaru odsunięcia kodu od lewej granicy",
    "tabulacja": "odsunięcie od lewej krawędzi 4 spacjami",
    "słownik": "zbiór klamrowy z kluczami i odpowiadającymi im wartoścami",
    "kwerenda": "nieedytowalny zbiór wartości",
    "lista": "edytowany zbiór danych",
    "polecenie": " fragment kodu do wykonania przez kompilator",
    }

for key,value in glosariusz.items():
    print(f"'{key}' oznacza w Pythonie '{value}'")
print("\n")

# zadanie 6.5 
rzeki = {
    "nil":"egipt",
    "wisła": "polska",
    "amazonka": "brazylia",
    }

for key,value in rzeki.items():
    print(f"Rzeka {key.title()} przepływa min. przez kraj o nazwie {value.title()}")
print("\n")

for nazwy_rzek in rzeki.keys():
    print(nazwy_rzek.title())
print("\n")

for nazwy_krajów in rzeki.values():
    print(nazwy_krajów.title())

#zadanie 6.6 
favorite_languages = {
    'janek':'python',
    'sara':'c',
    'edward': 'ruby',
    'paweł': 'python',
    }
lista_ankieta = ("janek", "sara", "andrzej", "edward", "roman", "paweł", "ola")
for osoba in lista_ankieta:
    if osoba in favorite_languages.keys():
        print(f"{osoba.title()}, dziękujemy za zaangażowanie.")
    else:
        print(f"{osoba.title()} - proponuję wziąć udział w ankecie.")