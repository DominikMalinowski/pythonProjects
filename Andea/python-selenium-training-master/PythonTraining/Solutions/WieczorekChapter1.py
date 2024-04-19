"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
to the user. Implement also check if user put the number or string.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

print('Please enter a number: ')  # ask for a number
number = 0

while True:  # check if input is integer or string
    number = input()
    try:
        number = int(number)
        break
    except ValueError:
        print('Once again! Enter a number!')
        pass


if number % 2 == 0:
    print('Number ' + str(number) + ' is even.')
elif number % 4 ==0:

    print('Number ' + str(number) + ' is even and multiple of 4.')
else:
    print('Number ' + str(number) + ' is odd')

# Extras - divide by number
num = int(input('Please enter a number to check: '))
check = int(input('Please enter a number to divide by: '))

div = num / check

if div % 2 == 0:
    print('Check divides evenly into num!')
else:
    print("Check doesn't divide evenly into num")