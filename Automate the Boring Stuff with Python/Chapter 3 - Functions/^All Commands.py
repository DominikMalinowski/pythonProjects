
# Content:
# - function definition + invoking 
# - function with parmaters 
# - return 
# - arguments for print() 
# - try except 


# function definition + invoking 
def hello():
    print('Hello')

hello()

# function with parmaters 
def hello(name):
    print(f'Hello {name}')

hello('John')

# return 
import random 

def roll(answer):
    if answer == 1:
        return 'That a one'
    elif answer == 2:
        return 'That\'s two'
    else:
        return 'Nor one or two'

print(roll(random.randint(1,3)))

# arguments for print() 
print('Hello', end =' ')
print('World')

print('cat','mouse','dog',sep=', ')

# try except 

def spam(divideBy):
    try:
        result = 10/float(divideBy)
        return result
    except ValueError:
        print('Inccorect data provided')
    
    
print(spam(4))
print(spam('ass'))