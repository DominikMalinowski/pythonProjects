"""Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your generator in the separate function."""

import string
import random


def password(userInput):
    # random.choice: Return a random  element from the non-empty sequence
    symbols = [random.choice(string.punctuation) for symbol in range(userInput)]
    lowercase = [random.choice(string.ascii_lowercase) for lower in range(userInput)]
    uppercase = [random.choice(string.ascii_uppercase) for upper in range(userInput)]
    numbers = [random.choice(string.digits) for number in range(userInput)]
    # check what above lists contain
    """print(symbols)
    print(lowercase)
    print(uppercase)
    print(numbers)"""

    # password created from symbols, lower/upper cases, which were generated as many times as userInput was
    generatedPassword = ''.join(symbols + lowercase + uppercase + numbers)

    #  password created from symbols, lower/upper cases which were generated above
    generatedPassword = ''.join(random.choice(generatedPassword) for value in range(userInput))

    return generatedPassword


passwordlength = int(input('Enter the password length: '))
newPassword = password(passwordlength)
print('\n' + 'New password has been generated: ', newPassword)
