import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    """ unction to generate password
    :param size: size of the password
    :param chars: characters to generate, by default letters, digits and punctuation
    :return: generated password
    """
    return ''.join(random.choice(chars) for _ in range(size))

# user input - len of password
ln = input('How many characters in your password? ')

# try to cast input to int
try:
    ln = int(ln)
except:
    # print error message and end the program with error code
    print("{} is not correct password lenght!!!".format(ln) )
    exit(1)

# execute function to generate password and print it
print("Your password: {}".format(pw_gen(ln)) )

pw_gen()