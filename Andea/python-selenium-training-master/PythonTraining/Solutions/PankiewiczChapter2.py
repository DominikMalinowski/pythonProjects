# V 1.1 - 14.05.2019

"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

#importing of 'random' library, that allows to use pseudo-random numbers
import random

#checking if typed number is a postitive integer
try:
    #creating of 'unknow' variable, that has only one character
    for unknown in range(1):
        # draw of random number in the range from '1' to '9'
        unknown = random.randint(1,9)

# taking of a list from User
    #taking of one number from User
    number = int(input("Type number from range of '1' to '9': "))


    # checking, if number, that User has typed is in the range from '1' to '9'
    if (number >= 1 and number <= 9):
        # if Users number is equal to 'unknown'- print message
        if number == unknown:
            print("You guessed correctly!")

    # checking if Users number is bigger than  'unknown' variable, smaller or out of range from '1' to '9'
        elif number > unknown:
            print("Your number is too big!")
        else:
            print("Your number is too small!")
    else: 
        print("Your number is out of range!")

# if typed number NOT is a positive integer- print Error
except ValueError:
    print("That is NOT a number")


