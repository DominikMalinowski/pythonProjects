import datetime
import time

def time_wrapper(function): # function invoke for wrapping
    def wrapper(*args): #wrapping function
        print(f'Start: {datetime.datetime.now()}')
        result = function(*args) #saving results to variable
        print(f'End: {datetime.datetime.now()}')
        return result #function return results saved as varaible
    return wrapper #upper function return whole wrapper

@time_wrapper #wrapping the functionality
def get_sum(value_1, value_2):
    time.sleep(2)
    return value_1 + value_2

@time_wrapper
def get_multiplication(value_1, value_2):
    time.sleep(2)
    return value_1 * value_2


value_1 = 2
value_2 = 3

# invoke wrapped function
print(f'Sum of {value_1} and {value_2} =')
print(get_sum(value_1, value_2))

print(f'Multiplication of {value_1} and {value_2} =')
print(get_multiplication(value_1, value_2))

