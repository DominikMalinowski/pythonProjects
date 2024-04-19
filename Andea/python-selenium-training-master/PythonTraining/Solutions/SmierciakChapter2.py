def Chapter2():
    import random
#User decision check
    cont = "YES"
    while cont=="YES":
        x = random.randint(1,10)
#User input + validation
        while True:
            try:
                y=float(input("Guess number from 1 to 9: "))
            except ValueError:
                print("Value is not a number.")
                continue
            else:
                break
#Value check
        if x<y:
            print("Inputted value is higher than randomized value ("+str(x)+")")
        elif x>y:
            print("Inputted value is lower than randomized value ("+str(x)+")")
        elif x==y:
            print("That's correct number!")
#User decision
        cont = input("Do you want to input next value? (YES/NO)")
        continue

Chapter2()
