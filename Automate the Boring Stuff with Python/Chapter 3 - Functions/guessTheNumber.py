import random
secretNumber = random.randint(1,20)
print('Myslę o pewnej liczbie z przedziału od 1 do 20')

for guessTaken in range (1,7):
    print('Spróbuj odgadnać liczbe')
    guess = int(input())

    if guess < secretNumber:
        print("Podana wartość jest mniejsza niz liczba")
    elif guess > secretNumber:
        print('Podana wartosc jest wieksza niz liczba')
    else:
        break
if guess == secretNumber:
    print('Udało Ci się w ' + str(guessTaken) + 'prob')
else:
    print("Sorry, tajemnicza liczba to " + str(secretNumber))



