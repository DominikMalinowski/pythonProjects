#zadanie 8.3 
def make_shirt(size="L",text="Pyhon_lover"):
    """Funkcja wyświetlajaća wybrany rozmiar i nadruk na koszulce"""
    print(f"Wybrałeś rozmiar {size.upper()} oraz nadruk w postaci tekstu '{text.title()}'.")

make_shirt("m","dooopa")
make_shirt(size="s",text="beniz")

#zadanie 8.4 
make_shirt("s")
make_shirt("l")
make_shirt(text="6969")

#zadanie 8.5 
def describe_city(city, country="Polska"):
    print(f"Miasto o nazwie: '{city.title()}' leży w kraju o nazwie'{country.title()}'")

describe_city("Kielce")

