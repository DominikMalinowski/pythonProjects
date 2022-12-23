# V 1.1 - 14.05.2019

"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Implement also check if user put the number or string.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

#checking if number and divider are actually numbers (float type)
try:
    #collecting of number (floating point)
    num = float(input("Type some number: "))
    print("It is actually a number")

    # collecting of divider (floating point)
    check = float(input("Type divider:"))
    print("It is actually a number")

    #if number can be divided by 4 without change
    if num % 4 == 0:
        print("Number can be divided by 4")
    # if number can be divided by 2 - print it is even number
    elif num % 2 == 0:
        print("Number is even")
    # if number can NOT be divided by 2 - print it is odd number
    else:
        print("Number is odd")

    #if number can be divided by divider without change- print message about it
    if num % check == 0:
        print("Number can be divided by divider without change")
    #if it is otherwise- print message about it
    else:
        print("Number can NOT be divided by divider without change")

#if one of typed variables is not a number (float type)- print Error message about it
except ValueError:
    print("It is NOT a number")

