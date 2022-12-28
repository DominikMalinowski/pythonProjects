"""
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Implement also check if user put the number or string.

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""


def number_validation():
    while True:
        user_number = input()
        try:
            user_number = float(user_number)
            return user_number
        except ValueError:
            print("Provided value isn't a number")


def even_or_odd():

    print('Please provide number to check')
    user_number = number_validation()

    # checking if provided number is even, odd or multiple of 4 
    if float(user_number)%4 == 0:
        print(f'Value provided by the user is multiple of 4')
    elif float(user_number)%2 == 0:
        print(f'Value provided by the user is even') 
    else:
        print(f'Value provided by the user is odd')

# calling the function 
even_or_odd()



def check_and_divide():
    print('Please provide number to check')
    num = number_validation()

    print('Please provide number divide by')
    check = number_validation()
    
    # check if values divide without rest 
    if num % check == 0:
        print('Second value divide first value without rest')
    else:
        print('Rest from division is equal to: ' + str(num % check))

# calling the function 
check_and_divide()



        