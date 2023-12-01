
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
