# V 1.1 - 14.05.2019
"""
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your generator in the seperate function.
"""

#importing of 'random' library, that allows to use pseudo-random numbers
import random
#importing of 'random' library, that allows to use string related methods
import string

#new function
def genPass():
    #variable, that will keep lenght of the password
    lenght1 = 0
    #taking of lenght of the password. It will be repeted, untill 'lenght1' >= 8
    while lenght1 < 8:
        lenght1 = int(input("Type lenght of password, but not shorten than 8: "))
    else:
        przyk2 = ''
        #while lenght of empty variable 'przyk2' is NOT bigger, than 8
        while len(przyk2) < lenght1:
            # draw of random number in the range of all characters (including white characters like SPACE or NEW LINE)
            random1 = random.choice(string.printable)
            # this adds draw number to the 'przyk2' variable
            przyk2 += random1
            #if character at the start or at the end of 'przyk2' variable is a white character- it is deleting it, simultaneously shortening its lenght by one
            przyk2 = (" ".join(przyk2.split()))
        print("Password: ")
        print(przyk2)

#calling of function
genPass()


