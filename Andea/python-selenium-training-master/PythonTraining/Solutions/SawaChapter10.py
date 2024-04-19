while True:
    print("Enter the number by which the number 10 will be divided")
    try:
        num = float(input("Your number: "))
        div = round(10.0/num,4)
        print("10 divided by " +str(num)+ " is equal to " +str(div))
    except ValueError:
        print("Division by string is not possible. Provide an input once again.")

    except ZeroDivisionError:
        print("It is not possible to divide by 0. Provide an input once again.")

    else:
        break