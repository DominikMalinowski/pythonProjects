def Chapter1():
#User decision check
    cont = "YES"
    while cont=="YES":
#User input + validation
        while True:
            try:
                number=float(input("Type a number: "))
            except ValueError:
                print("Value is not a number.")
                continue
            else:
                break
#return entered value
        print("Entered value:")
        print(number)
#check
        if (number%2) == 0:
            if (number%4) == 0:
                print("Your value is dividable by 2 and 4.")
            else:
                print("Your value is dividable by 2.")
        else:
            print("Your number is not dividable by 2 or 4.")
        cont = input("Do you want to input next value? (YES/NO)")
        continue

def Chapter1Extra():
#User decision check
    cont = "YES"
    while cont=="YES":
    #User input + validation
        while True:
            try:
                number=float(input("Type a number: "))
            except ValueError:
                print("Value is not a number.")
                continue
            else:
                break
        while True:
            try:
                check=float(input("Type a number to be checked against: "))
            except ValueError:
                print("Value is not a number.")
                continue
            else:
                break
#return entered value
        print("Entered values:")
        print(number)
        print(check)
    #check
        if (number%check) == 0:
            print("Inputted number: "+str(number)+" is dividable by inputted number: "+str(check)+" evenly")
        else:
            print("Inputted number: "+str(number)+" is not dividable by inputted number: "+str(check)+" evenly")  
#User decision
        cont = input("Do you want to input next value? (YES/NO)")
        continue

Chapter1()
Chapter1Extra()
