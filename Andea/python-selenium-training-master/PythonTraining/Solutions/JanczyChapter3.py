import random

# Function to generate password
# parameter: password_len - length of password to be created
# return: new_password - string containing password

def passwordGenerator(password_len):

    # Strings containing symbols of each type

    special_signs = ',.<>/?;:[]{}\|!@#$%^&*()-_+=`'
    upper_case_letters = 'ABCDEFGHIJKLMNOPQRSTUWVXYZ'
    lower_case_letters = 'abcdefghijklmnopqrstuwvxyz'
    numbers = '0123456789'
    all_symbols = special_signs + upper_case_letters + lower_case_letters + numbers

    # Declararion of list used to store generated symbols
    password_list = []

    # Strong password should have at least one number, one upper case letter, one lower case letter and one special sign.
    # To ensure that, system randomly generates positions on which one mandatory symbol of each type will be placed in the password
    # Taken positions will be excluded from next generation, to avoid overwriting

    # Declaration of list used to store numbers which will be excluded from next generation
    taken_index = []

    number_index = random.randint(0, password_len)
    taken_index.append(number_index)

    lower_case_index = random.choice([i for i in range(0, password_len) if i not in taken_index])
    taken_index.append(lower_case_index)

    upper_case_index = random.choice([j for j in range(0, password_len) if j not in taken_index])
    taken_index.append(upper_case_index)

    special_signs_index = random.choice([k for k in range(0, password_len) if k not in taken_index])

    # Loop generating the password
    # In each iteration system checks if current index is one of the previously generated indexes reserved for certain kind of symbol
    # If yes, system adds to password random symbol of proper type
    # If no, system generates random symbol from pool of all available symbols

    for k in range(password_len):

        if k == number_index:
            password_list.append(random.choice(numbers))

        elif k == lower_case_index:
            password_list.append(random.choice(lower_case_letters))

        elif k == upper_case_index:
            password_list.append(random.choice(upper_case_letters))

        elif k == special_signs_index:
            password_list.append(random.choice(special_signs))

        else:
            password_list.append(random.choice(all_symbols))

    # In each iteration string variable containing password is concatenated with generated symbol
        if k != 0:
            new_password = new_password + password_list[k]
        else:
            new_password = password_list[k]

    return new_password


# User is asked to enter length of the password, if value is correct method generating password is called
while True:
    print("Enter length of the password:")
    password_length = int(input())

    if password_length >= 4:
        password = passwordGenerator(password_length)
        print("Your new password = " + password)
        break
    else:
        print("Password must be at least 4 characters long!")
        continue
