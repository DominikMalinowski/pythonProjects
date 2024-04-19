#xxxxxxxxxxxxxxxx Exception Handling xxxxxxxxxxxxxxxxxxxxxxxx
#Write a function that will ask an user to provide a number. Then the function should divide 10.0 by the provided number and print out the string saying that "Division result is X" (X should be a floating number)
#a) In case user provides 0 as an input, function should print out that it is not possible to divide by 0 and ask an user to provide an input once again
#b) In case user provides a string, function should print out that division by string is not possible and ask an user to provide an input once again


#Here is the definition of a "main" function, which is checking if value provided is != 0. If 

def Chapter10():
#main loop
    while True:
        try:
            x = float(input("Provide a value: "))
            print("10 divided by your value is equal to: "+str(round(10/x,5)))
#using standard exceptions
#capturing first exception for NaN error
        except ValueError:
            print("Value is not a number.")
            #continue from the beginning of the loop
            continue
#capturing second error for divide by zero error
        except ZeroDivisionError:
            print("Can't divide by 0.")
            continue
#if instructions under try clause will be succesful, then break the loop
        else:
            break


Chapter10()