import random


def enter_number(usernumber):
    if not usernumber.isdecimal():
        print('This is not a number')
    userumber = input()
    try:
        usernumber = int(usernumber)
    except ValueError:
        print('This is not a number. Please enter the proper value')


theChosenNumber = random.randint(0, 9)
print('Welcome to Random Number Game. Guess the number (0-9) \n')
guessedNumber = ''
i = 0
while guessedNumber != theChosenNumber:
    # guessedNumber = int(enter_number())
    guessedNumber = int(input())
    i = i+1
    if guessedNumber > 9 or guessedNumber < 0:
        print('Please choose number between 0-9')
    elif guessedNumber > theChosenNumber:
        print('Too high. Try again')
    elif guessedNumber < theChosenNumber:
        print('Too low. Try again')
    else:
        print('You\'re right! The chosen number was ' + str(theChosenNumber) + ' and it took you ' + str(i) + ' tries to guess')



