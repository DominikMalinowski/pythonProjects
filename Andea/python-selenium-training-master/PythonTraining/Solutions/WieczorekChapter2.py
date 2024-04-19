""" Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. """

import random

number = random.randint(1, 10)
# print(number) # to check what number has been randomize

userNumber = 0
c = 0

while userNumber != number:
    userNumber = int(input('Guess the number between 1-9: '))  # number entered by user
    c += 1
    if userNumber > number:
        print('Try again, your number is too high!')
    elif userNumber < number:
        print('Try again, your number is too low!')
    else:
        break  # end of while loop if number is the same as randomized

print('Your number is exactly right! You guessed my number in ' + str(c) + ' guesses!')
