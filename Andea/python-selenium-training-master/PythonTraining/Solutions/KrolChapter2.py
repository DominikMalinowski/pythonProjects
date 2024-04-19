import random

print('Hello. What is your name??')
name = input()
print('Well, ' + name + ', I am thinking of number between or equal to 1 and 9')

# Number generation (1 to 9)
secretNumber = random.randint(1, 9)

# Guesses counter
guessesTaken = 1

while True:
    while True:
        try:
            print('Take a guess.')
            guess = int(input())
            break
        except ValueError:
            print('This is not a integer number between or equal to 1 and 9')

    # For guess that is too low

    if guess < secretNumber:
        print('Your guess is too low.')
        guessesTaken = guessesTaken + 1

    # For guess that is too high

    elif guess > secretNumber:
        print('Your guess is too high.')
        guessesTaken = guessesTaken + 1

    # This conditions is for correct guess

    else:
        break

print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses')
