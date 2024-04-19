##
print('Jak sie nazywasz')
user_name = input()

if user_name == 'Alicja':
    print('Czesc Alicja')
else:
    print('Ile masz lat ?')
    user_age = input()
    user_age = int(user_age)
    if user_age < 12:
        print('Nie jestes Alicją, gwoniarzu')
    elif user_age > 2000:
        print('Alicja nie jest wampirem')
    elif user_age > 100:
        print('Nie jestes Alicja, dziadku')