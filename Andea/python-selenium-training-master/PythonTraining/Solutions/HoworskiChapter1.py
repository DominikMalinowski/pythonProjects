

def userInputNumeric(message):
    """
    Function to input and check if user input isnumeric or not
    :param message: Message to present (question for e number)
    :return: entered value or None (if it's not numeric)
    """

    # value as an input
    value = input(message)

    # check if value is numeric
    if not value.isnumeric():
        print("%s is not a number!" % value)
        # return None (entered value is not numeric)
        return None

    # return the value
    return value

# call input and assign the result to num
num = userInputNumeric("Enter the number: ")

# if modulus 2 is 0 = it's even, if not = it's odd
if float(num) % 2 == 0:
    print("%s is even number" % num)
elif float(num) % 4 == 0:
    print("%s is a multiple of 4" % num)
else:
    print("%s is odd number" % num)

# call input and assign the result to check
check = input("Enter number to divide by: ")

# check if num is devides evenly into check
if float(num) % float(check)==0:
    print("%s divides evenly into %s" % (check, num))
else:
    print("%s divides NOT evenly into %s" % (check, num))

