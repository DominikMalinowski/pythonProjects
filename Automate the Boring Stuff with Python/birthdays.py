birthdays = {'Alicja':'1 kwiecień', 'Bob':'12 grudzień', 'Karol':'4 marzec'}
while True:
    print('Podaj imię (pozostaw puste, aby zakończyc program)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' to dzien urodzin osoby o imieniu ' + name + '.')

    else:
        print('Nie znaleziono informacji o urodzinach oosby o imieniu ' + name)
        print('Kiedy przypadają te urodziny ?')
        bday = input()
        birthdays[name] = bday
        print('Baza danych o urodzinach została zaktualziowana')
        