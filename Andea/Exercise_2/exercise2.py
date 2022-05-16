"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number,
Then tell them whether they guessed too low, too high, or exactly right.
"""
import random


def guess_the_number():
    # selecting random number and providing guessed number
    right_value = random.randint(1, 9)
    print(right_value)
    print('Try to guess randomly selected number in range from 1 to 9')
    print('Type "stop" to stop exercise')

    # setting counter for number of try
    attempt = 1

    # loop start
    while True:
        guess = input()

        if guess.lower() == 'stop':
            print('Exercise has been terminated')
            break
        else:
            # validation if provided value is number
            try:
                guess = int(guess)
            except ValueError:
                print('Provided value isn\'t number')
                continue

            # check if provided value is from 1-9 range
            if int(guess) not in range(1, 10):
                print('Provided value is outside of range from 1 to 9')
            else:

                # checking number and guessed number
                guess = int(guess)
                if right_value == guess:
                    print('***Jackpot***')
                    print('It takes you ' + str(attempt) + ' try to guess right')
                    break
                elif right_value > guess:
                    print('Too low')
                    attempt += 1
                    continue

                elif right_value < guess:
                    print('Too high')
                    attempt += 1
                    continue


guess_the_number()
