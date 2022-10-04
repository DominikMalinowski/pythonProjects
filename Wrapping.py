import datetime

def datetime_wrapper(function):
    def wrapper():
        print(datetime.datetime.now())
        function()
        print(datetime.datetime.now())

    return wrapper

# @datetime_wrapper
def print_greetings():
   workers = ['Eve', 'Bob', 'Jess', 'Pat', 'Andrea', 'Gary']
   for worker in workers:
       print(f'Hello {worker}!')

# print_greetings()

datetime_wrapped_greeting = datetime_wrapper(print_greetings)
datetime_wrapped_greeting()