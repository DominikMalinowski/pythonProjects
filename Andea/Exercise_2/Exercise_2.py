"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number,
Then tell them whether they guessed too low, too high, or exactly right.
"""

import random
def guess_number():
    generated_value = random.randint(1,9)

    print('There is hidden number - try to guess it')
    for i in range(1,4):
        print(f"You have {4-i} changes left")
        guess = int(input())

        if guess == generated_value:
            print('You guess it right')
            break
        elif guess > generated_value:
            print('Your guess is too big')
            continue
        else:
            print('Your guess is too small')
            continue

guess_number()