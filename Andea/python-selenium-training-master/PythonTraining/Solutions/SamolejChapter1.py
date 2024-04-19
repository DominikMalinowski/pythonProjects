#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#Implement also check if user put the number or string.
#Hint: how does an even / odd number react differently when divided by 2?
#
#Extras:
#
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
numberInfo = "Enter the number"
dividerInfo ="Enter the divider"

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



def checkFirstNumber(number):
    number = int(number)
    if (number % 4) == 0:
        print ("This number is a multiple of four (and it's even).")
    elif (number % 2) == 0:
        print ("This number is even")
    else:
        print ("This number is odd")


def checkDivider(number, divider):
    if (number % divider) == 0:
        print ("Number " + str(number) + " is devisible by " + str(divider) + "\n")
    else:
        print ("Number " + str(number) + " is not devisible by " + str(divider) + "\n")




number = enterNumber(numberInfo)
checkFirstNumber(number)
number = enterNumber(numberInfo)
divider = enterNumber(dividerInfo)
    
number = int(number)
divider = int (divider)

checkDivider(number,divider)