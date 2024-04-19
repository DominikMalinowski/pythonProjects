def collatz(number):
    try:
        number % 2
    except ValueError:
        print('No chyba Cie pojabło koleś')

    if number % 2 == 0:
        result = number/2
        print(str(number) + ' // 2 = ' + str(result))
    else:
        result = 3 * number + 1
        print('3 * '+str(number)+' + 1 = '+ str(result))

    if result == 1:
        print(1)
    else:
        collatz(int(result))

def repeat():
    print('Prosze podać liczbę')
    try:
        number = int(input())
        collatz(number)
    except ValueError:
        print('No chyba Cie pojabło koleś')

repeat()

