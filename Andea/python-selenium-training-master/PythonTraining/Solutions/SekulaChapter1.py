

while True:
    print('Enter number: ')
    try:
        number=int(input())
        break
    except ValueError:
        print('It is not a number. Try again')
        print()


if number%2==0:
   
    if number%4==0:
        print('Your number is multiple of 4')
    else:
         print('Your number is even')

else:
    print('Yuor number is odd')



########################################## Extra ##########################################################################

print('Enter first number:')
num=float(input())

while True:
   print('Enter second number:')
   try:
        check=float(input())
        break
   except ValueError:
        print('Second number cannot be 0. Try again')
        print()

if num%check==0:
    print('Divides evenly')
else:
    print('Divides not evenly')

