import random


def generate_password():
    letters = 'abcdefghijklmnoprstuwxyzq/!><)(*&^%$#@/?'
    r = random.randint(0, 10)
    letter = ''
    letter_up = ''
    for i in range(3):
        letter = letter + random.choice(letters)
        letter_up = (letter_up + random.choice(letters)).upper()

    password = list(str(r) + letter + str(r+3) + letter_up)
    random.shuffle(password)
    password = ''.join(password)

    return password


print(generate_password())

# password: mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.

