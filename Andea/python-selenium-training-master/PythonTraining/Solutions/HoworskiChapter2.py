import random

# initialise the variables
randomNum = random.randint(1, 9)
userInput = 0
count = 0

# while input is not randomNum or input is not 'exit'
while userInput != randomNum and userInput != 'exit':
    userInput = input("Enter the number between 1 and 9 (type 'exit' for end the game) : ")

    # if user enter exit then break
    if userInput.lower() == "exit":
        print("Thank you for the game!")
        break

    # check if userInput cam be cast to integer
    try:
        userInput = int(userInput)
    except:
        print("%s is not an integer!" % userInput)
        continue

    # increase count of tries
    count += 1

    # game logic: too low, too high else on point
    if userInput < randomNum:
        print("It's too low!")
    elif userInput > randomNum:
        print("It's too high!")
    else:
        print("You got it!\n It took %s tries!" % count)