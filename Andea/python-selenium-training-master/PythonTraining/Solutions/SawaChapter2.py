import random
num = random.randint(1, 9)
print('Myślę o liczbie z przedziału od 1 do 9. Zgadniesz jaka to liczba?')

odp = 0
liczbaOdp = 0
while odp != num:
    odp = int(input("Podaj liczbę: "))
    liczbaOdp += 1                   # licznik odpowiedzi do daje 1 za kazdą próbą odgadnięcia

    if odp < num:
        print('Za mało.')
    elif odp > num:
        print('Za dużo.')
    else:
        break                       # Dobra odpowiedź!

if odp == num:
    print('Udało Ci się za ' + str(liczbaOdp) + ' razem!')
