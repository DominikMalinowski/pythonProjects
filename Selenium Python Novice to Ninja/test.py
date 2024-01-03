
city = 'nyc'
event = 'show'

print("Welcome to %s and enjoy the %s" %(city,event))


l1 = [1,2,3]
l2 = [4,5,6,7,8]

for a,b in zip(l1,l2):
    print(a,b)

# %%
def add(a1,a2):
    return(a1+a2)

print(add(2,4))

# %%

a = 10 

def change():
    global a 
    print('2. Value of "a" is:' + str(a))
    a = 2 
    print('3. Value of "a" is:' + str(a))

print('1. Value of "a" is:' + str(a))
change()
print('4. Value of "a" is:' + str(a))
# %%

def largest(*args):
    print(max(args))
    
a = [1,2,3,4]
b = [2,3,6]
c = [20,30,50]

largest(a,b)

# %%

class Fruit(object):
    def __init__(self) -> None:
        print('This is a Fruit')
    
    def nutrition(self):
        print('Yummy')

    def fruit_shape(self):
        print('Shape')

class Apple(Fruit):
    def __init__(self) -> None:
        super().__init__()
        print('Specifically an apple')

    def nutrition(self):
        print('Better')

    def color(self):
        print('Red')

f1 = Fruit()
f1.nutrition()
f1.fruit_shape()

a1 = Apple() 
a1.nutrition()
a1.fruit_shape()
a1.color()
# %%
 
def exceptionHandle():
    a = 10
    b = 20
    c = 0 

    try:
        d = (a+b)/c
        print(d)
        
    except ZeroDivisionError:
        print('Dived by zero')
        # raise Exception("This is a exception")
    except TypeError:
        print('Wrong type')  
    else:
        print('No exception has been found')
    finally:
        print('Fin')


exceptionHandle()
# %%

d = {'make':'bmw','model':550, 'year': 2023}

def get_key(key):
    try:
        print(d[key])
    except KeyError:
        print('There is no key as: ' + key)      
    finally:
        print('Fin')

get_key('color')
# %%

my_write = open('text.txt','w')
my_write.write('placeholder')
my_write.close()

my_read = open('text.txt','r')
print(my_read.read())

# %%

with open('placeholder.txt','w') as as_write:
    as_write.write('extra placeholder')

with open('placeholder.txt','r') as as_read:
    print(as_read.read())
# %%
