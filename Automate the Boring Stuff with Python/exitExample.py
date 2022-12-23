import sys

while True:
    print('Wpisz Exit aby zakonczyc dzialanie programu')
    response = input()
    if response == 'Exit':
        sys.exit()
    print('Wpisałes ' + response + '.')
