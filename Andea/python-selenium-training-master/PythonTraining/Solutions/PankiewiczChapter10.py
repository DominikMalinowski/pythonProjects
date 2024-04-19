# V 1.0 - 15.05.2019
"""
# xxxxxxxxxxxxxxxx Exception Handling xxxxxxxxxxxxxxxxxxxxxxxx

# Write a function that will ask an user to provide a number. Then the function should divide 10.0 by the provided number and print out the string saying that "Division result is X" (X should be a floating number)
# a) In case user provides 0 as an input, function should print out that it is not possible to divide by 0 and ask an user to provide an input once again
# b) In case user provides a string, function should print out that division by string is not possible and ask an user to provide an input once again
"""
is_done = 0

# do it as long, as
while is_done == 0:
    number = input("Type your number: ")
    # if input consist of numbers only
    if number.isdigit():
        if int(number) == 0:
            print("Number cannot be divided by '0'")
        else:
            print("Yes, input string is an Integer.")
            is_done = 1
    else:
        try:
            float(number)
            if float(number) == 0:
                print("Number cannot be divided by '0'")
            else:
                is_done = 1
                print("Yes, input string is an Float.")
        # if 'number' can not be saved as 'float' type, because of ValueError
        except ValueError:
            print("Number cannot be divided by 'string'. Provide number.")
print("Division result is " + str(10.0 / float(number)))
