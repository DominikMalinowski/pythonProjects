#Write a password generator in Python.
#Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
#The passwords should be random, generating a new password every time the user asks for a new password.
#Include your generator in the seperate function.
import random

characters = list(map(chr, range(33,120)))

def passGen():
    counter = 0
    password = ""
    length = random.randint(10,25)
    
    while counter < length:
        charRand = random.randint(33,120-34)
        password += characters[charRand]
        counter += 1

    return password


def userChoice():

    while True:                                          #do-while alternate
        flag = input()
        if flag == 'y' or flag== 'q':
            break

    while flag != 'q':
        
        print ("\n"+passGen())
        print ("\nEnter \"y\" to generate new password. Enter \"q\" to quit.\n")
        flag = input()

print ("Welcome in password generator. \nEnter \"y\" to generate new password. Enter \"q\" to quit.\n")
userChoice()