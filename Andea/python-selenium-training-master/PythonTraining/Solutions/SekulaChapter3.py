import random


def randchar(num):

    for i in range(num):

        char=chr(random.randint(33,126))
        print(char, end='')
    print()
        


print('Enter the number of characters:')
num=int(input())
print('Your new password is:')
randchar(num)




