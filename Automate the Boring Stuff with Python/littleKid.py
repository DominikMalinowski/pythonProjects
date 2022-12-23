print('Podaj swoje imie')
user_name = input()
if user_name == 'Alicja':
    print('Czesc Alicja')
else:
    print('Podaj swoj wiek')
    user_age = input()
    user_age = int(user_age)
    if user_age < 12:
        print('Nie jestes Alcją, dzieciaku')
    else:
        print('Nie jestes ani Alicja, ani dzieciakiem')
