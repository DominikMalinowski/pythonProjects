#name = input("Podaj swoje imię: ")
#print(f"Witaj {name}")

#prompt = "Jeżeli powiesz nam kim jesteś, spersonalizujemy wyświetlany komunikat"
#prompt += "\n Jak masz na imię ?"

#name = input(prompt)
#print(f"\n Witaj, {name}!")

def greet_user(username): 
    """Wyświetl proste powitanie""" 
    print(f"Witaj, {username.title()}") 

greet_user('janek')

def get_formated_name(first_name, last_name): 
    """Zwraca elegancko sformatowane imie i nazwisko""" 
    full_name = f'{first_name} {last_name}'
    return full_name

#ta pętla działa w nieskończonośc
while True: 
    print("\nProszę podać imię i nazwisko")
    f_name = input("Imię: ")
    l_name = input("Nazwisko: ")

    formated_name = get_formated_name(f_name, l_name)
    print(f"\nWitaj, {formated_name}")
    
