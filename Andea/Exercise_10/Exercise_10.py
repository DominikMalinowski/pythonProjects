"""
xxxxxxxxxxxxxxxx Exception Handling xxxxxxxxxxxxxxxxxxxxxxxx

- Write a function that will ask an user to provide a number. 
- Then the function should divide 10.0 by the provided number and print out the string saying that "Division result is X" (X should be a floating number)
a) In case user provides 0 as an input, function should print out that it is not possible to divide by 0 and ask an user to provide an input once again
b) In case user provides a string, function should print out that division by string is not possible and ask an user to provide an input once again


"""

def divide_number():
    while True:  
        print('daj mi ten numer')  
        number = input()
        try:
            result = (10/float(number))
            break
        except ValueError:
            print("Division by string is not possible")
        except ZeroDivisionError:
            print("It is not possible to divide by 0")

    print(f"Division result is {result}")

divide_number()