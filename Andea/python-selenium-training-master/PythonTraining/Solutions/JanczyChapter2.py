import random

# Creating random number
random_number = random.randint(1, 9)

# Infinite loop
while True:

    # User enters number
    print("Guess a number:")
    guessed_number = int(input())

    # When entered number is equal to previously generated, proper message is displayed, and loop breaks
    if guessed_number == random_number:
        print("Correct!")
        break

    # When entered number is not equal to previously generated, proper message is displayed, and loop continues
    elif guessed_number > random_number:
        print("Too high!")
        continue

    elif guessed_number < random_number:
        print("Too low!")
        continue
