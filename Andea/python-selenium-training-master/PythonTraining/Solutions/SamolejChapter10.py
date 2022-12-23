"""
xxxxxxxxxxxxxxxx Exception Handling xxxxxxxxxxxxxxxxxxxxxxxx
Write a function that will ask an user to provide a number. Then the function should divide 10.0 by the provided number and print out the string saying that "Division result is X" (X should be a floating number)
a) In case user provides 0 as an input, function should print out that it is not possible to divide by 0 and ask an user to provide an input once again
b) In case user provides a string, function should print out that division by string is not possible and ask an user to provide an input once again
"""
ten = 10.0

def inputNumber():
    number = float(input("Input number:"))
    if number == 0:
        raise Exception("Error, dividing by zero is impossible")
    else:
        print(str(number) + "/" + str(ten) + "=" + str(ten / number))

#loop
while True:
    try:
        inputNumber()
        break
    except Exception as error:
        print(str(error))