import random

number=random.randint(1,9)
guess=''

while number !=guess:
    while True:
        print('Enter your guess: ')
        try:
            guess=int(input())
            break
        except ValueError:
            print('It is not a number. Try again')
            print()

    if guess<number:
        print('Your guess is too low')
        print()

    elif guess>number:
        print('Your guess is to high')
        print()

    else:
        print('You guessed')
