"""
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Implement also check if user put the number or string.

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

show how git works
"""


def even_odd():
    # getting number from the user
    while True:
        print('Please provide a value')
        user_number = input()

        # checking if provided values is numerical
        try:
            user_number = float(user_number)
            break
        except ValueError:
            print('Provided value must be a number\n')

    # checking if provided value is even or odd%
    if float(user_number) % 4 == 0:
        print('Provided value is even and it\'s multiplicity of 4')
    elif float(user_number) % 2 == 0:
        print('Provided value is even')
    else:
        print('Provided values is odd')


# calling the function
even_odd()


def num_check():
    while True:
        while True:
            # getting first value from user
            print("Please provide value to check")
            num = input()

            # validation if provided num is number
            try:
                num = float(num)
            except ValueError:
                print('Provided value must be a number')
                continue
            break

        while True:
            # getting second value from user
            print("Now please provide value to divide check by")
            check = input()

            # validation if provided check is number
            try:
                check = float(check)
            except ValueError:
                print('Provided value must be a number')
                continue
            break

        # modulo
        rest = num % check

        # checking validation
        if rest == 0:
            print('Second value divide first value without rest')
            break

        else:
            print('Rest from division is equal to: ' + str(rest))
            break


# calling the function
num_check()
