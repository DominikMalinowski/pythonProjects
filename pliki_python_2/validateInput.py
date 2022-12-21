while True:
    print('podaj swój wiek')
    age = input()
    if age.isdecimal():
        break
    print('Wiek musi być liczbą')

while True:
    print('Wybierz nowe hasoło')
    password = input()
    if password.isalnum():
        break
    print('Hasło możę składać się jedynie z liter i cyfr')

