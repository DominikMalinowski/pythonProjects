

# Function asks user to enter number
# return: is_good_ask - Boolean value depending on the return value of divideByTen function, returned if no exception has been raised inside the function
# return: False - Boolean value, returned if the exception has been raised inside the function
def askNumber():
    try:
        print('Enter a number: ')
        entered_number = float(input())

        is_good_divide = divideByTen(entered_number)

        if is_good_divide:
            is_good_ask = True
        else:
            is_good_ask = False

        return is_good_ask

    except ValueError:
        print('It is not possible to divide by string! Enter the number again.')
        return False

# Function divides 10.0 by given float number and prints the result on the screen
# parameter: number -  float conataining number by which 10.0 will be divided
# return: Boolean value - set to False if an exception has been raised, or to True, if not
def divideByTen(number):
    try:
        result = 10.0 / number
        print(result)
        return True
    except ZeroDivisionError:
        print('It is not possible to divide by 0! Enter the number again.')
        return False

# Infinite loop ask for input as long as user provides invalid values
while True:
    if askNumber():
        break
    else:
        continue