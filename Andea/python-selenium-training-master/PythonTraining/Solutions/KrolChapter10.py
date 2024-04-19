def ten_divide_by(number):
    try:
        print('10 divided by ' + number + ' is equal to: ' + str(10 / (float(number))))
        return True
    except ValueError:
        print('Division by string is not possible.')
        return False
    except ZeroDivisionError:
        print('It is not possible to divide by 0.')
        return False


while True:
    print('Please provide a number:')
    answer = ten_divide_by(input())
    if answer:
        break
