print('Witaj w generatorze haseł. Podaj swoje imię żeby kontynułować')
imie = input()
print('Witaj ' + str(imie))
print('Czy nadal chczesz zmienić hasło? (wpisz tak/nie)')
odp = input()

if odp == "tak":
    import string
    import random
    characters = string.ascii_letters + string.punctuation  + string.digits

    password = ""
    password_length = random.randint(8, 16)

    for x in range(password_length):
        char = random.choice(characters)
        password = password + char

    print('To Twoje nowe hasło: ' + str(password))

if odp == 'nie':
    print("Hasło zostaje niezmienione")