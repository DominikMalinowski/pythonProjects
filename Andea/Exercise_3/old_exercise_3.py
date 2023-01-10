"""
Write a password generator in Python.
Be creative with how you generate passwords ->
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your generator in the separate function.
"""

import random
import string


def generate_password():
    print('Welcome to password generator')

    while True:
        print('Pleas provide how long password you want (minimum value is 8)')
        password_length = input()

        # validation of password length being number
        try:
            password_length = int(password_length)
        except ValueError:
            print('Password length must be a number')
            continue

        # validation of minimum required password length
        if password_length < 8:
            print('Minial number of characters for generated password is 8')
            continue
        else:
            break

    # setting up base for loop
    base = string.ascii_letters + string.digits + string.punctuation

    # password generation
    password = ''.join(random.choice(base) for _ in range(password_length))
    print('Your password is: ' + password)


generate_password()
