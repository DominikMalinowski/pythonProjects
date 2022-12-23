"""xxxxxxxxxxxxxxxx Exception Handling xxxxxxxxxxxxxxxxxxxxxxxx

Write a function that will ask an user to provide a number. Then the function should divide 10.0 by the provided number and print out the string saying that "Division result is X" (X should be a floating number)
a) In case user provides 0 as an input, function should print out that it is not possible to divide by 0 and ask an user to provide an input once again
b) In case user provides a string, function should print out that division by string is not possible and ask an user to provide an input once again"""


#  function definition
def example():
    while True:
        try:
            x = float(input("Enter a number: "))
            y = float(input("Enter another number: "))
            print(x, '/', y, '=', x / y)
            #  while True - program will do te division, and go outside from the loop
            break
        #  if the zero division error occurs, system will display the message and go to the beginning of the loop
        except ZeroDivisionError:
            print("Cannot divide by 0!")
        except ValueError:
            print("It is not a number! Division by string is not possible.")


example()
