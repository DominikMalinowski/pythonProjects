#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.


import random
numberRand = random.randint(1,9)

numberInfo = "Enter the number"

def enterNumber(info):
    flag = None
    while not flag:
        print (info)
        number = input()
       
        try:
           val = int(number)
           flag = True
        except ValueError:
          print("That's not an int!")
          flag = None

    flag = None
    return number


def checkIfEqual():
    equal = None
    while not equal:
        number = enterNumber(numberInfo)
        number = int(number)
        if number > numberRand:
            print ("Your number is bigger.\n")
            flag = None
        elif number < numberRand:
            print ("Your number is smaller.\n")
            flag = None
        else:
            print ("Your number is equal.\n")
            equal = True

checkIfEqual()