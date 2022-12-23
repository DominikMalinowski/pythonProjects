# Ask user for a number

while True:
    print('Please type some number.')
    user_number = input()

    # Check if it is a number

    try:
        value = float(user_number)
        break
    except ValueError:
        print('This is not a number.')

# Check if it is divided by 2 and 4

if float(user_number) % 2 == 0 and float(user_number) % 4 == 0:
    print('Your number is: ' + user_number + ' and it is even and multiple of 4')
elif float(user_number) % 2 == 0:
    print('Your number is: ' + user_number + ' and it is even')
else:
    print('Your number is: ' + user_number + ' and it is odd')

# Extra check if (check) divides evenly into (num)

print('Please provide number to check')
num = float(input())

print('Please provide number to divide by')
check = float(input())

if num % check == 0:
    print('%s divides evenly into %s' % (check, num))
else:
    print('%s divides NOT evenly into %s' % (check, num))

