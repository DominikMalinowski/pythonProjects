"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number,
Then tell them whether they guessed too low, too high, or exactly right.
"""

import random
def guess_number():
    # setting the range of value to pick from and number of tries
    generated_value = random.randint(1,9)
    number_of_tries = 3 

    print('There is hidden number in range from 1 to 9 - try to guess it')
    # loop for repeating guess for the user
    for i in range(0,int(number_of_tries)):
        print(f"You have {int(number_of_tries)-i} changes left")
        guess = int(input())

        # validation if user guesss number right 
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