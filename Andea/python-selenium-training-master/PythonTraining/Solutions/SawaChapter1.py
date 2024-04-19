try:
    num = float(input("Podaj liczbę: "))
    check = float(input("Podaj dzielnik: "))
                                                    #sprawdzenie parzystości i podatność na dzielenie prze 4 i podany dzielnik "check"
    if num % 4 == 0:
        print(str(num) + " dzieli się przez 4")
    elif num % 2 == 0:
        print(str(num) + " to liczba parzysta")
    else:
        print(str(num) + " to liczba jest nieparzysta")

    if num % check == 0:
        print(str(num) + " dzieli się przez " + str(check) + " bez reszty")
    else:
        print(str(num) + " nie dzieli się przez " + str(check) + " bez reszty")

except ValueError:
    print("To nie jest liczbą. Spróbój jeszcze raz.")