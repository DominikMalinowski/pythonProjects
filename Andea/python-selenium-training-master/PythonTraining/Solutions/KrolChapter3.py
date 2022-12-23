# Library
import random


# Password Generator function

def password_generator():
    # Password and password length variables
    password = ''
    password_length = random.randint(10, 30)

    # Signs possible in password
    signs = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
             'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q', 'W', 'E', 'R', 'T', 'Y',
             'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '!',
             '@', '#', '$', '%', '^', '&', '*', '(', ')']

    for i in range(password_length):
        password += random.choice(signs)

    print('Your generated password is: ' + password)


# Password generator program
while True:
    print('Do you want me to generate password? (YES/NO)')
    answer = input()

    if answer.upper() == 'NO':
        # Exit generator
        print('Have a good day than.')
        break

    elif answer.upper() == 'YES':
        # Generate password
        password_generator()

    else:
        print('That is not a correct answer')
