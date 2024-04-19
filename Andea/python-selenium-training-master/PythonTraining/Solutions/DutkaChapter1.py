# declaring variable
userNumber =''

while not userNumber.isdecimal():
    #loop to ask user for 3x unless the input is not a number
    for i in range(3):
        userNumber = input('Enter number\n')
        try:
            test_num = float(userNumber)
            #chec if number if dividec by 4
            if test_num % 4 == 0:
                print('This number is even and divided by 4')
            # check if number is even
            elif test_num % 2 == 0:
                print('This number is even')
            #else number is odd
            else:
                print('This number is odd')
        except ValueError:
            print('This is not a number')
        i = i+1



