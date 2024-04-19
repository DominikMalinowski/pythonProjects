""" Write a program that:
1. Creates a new file named 'data.txt' in the same directory as your program (check if it already doesn't exist) - use relative path!
2. Opens the file in write mode and writes three words (e.g. 'one', 'two', 'three') to it - each one in new line
3. Opens the file in read mode and reads all the lines, putting each word to list as a new element
4. Deletes the created file """

import os

# create a .txt file in write mode
file = open('data.txt', 'w')

# write three words to this file each in new line
file.write('one line\n''two\n''three\n')

# open .txt file in read only mode
file = open('data.txt', "r")

# define empty list
fileList = []

# put each word to list as new element
# splitlines() method splits the string at line breaks and returns a list of lines in the string.
# fileList = open('data.txt').read().splitlines() - other way
for line in file:
    fileList += line.splitlines()
print(fileList)

# close opened file
file.close()

# deleting file: check if file exist and remove it - removing depends on user decision
if os.path.isfile('data.txt'):
    decision = input("\nDo you want to delete the following file '%s'? Press y/n. " % file.name)
    if decision == 'y':
        os.remove('data.txt')
        print("Your file has been removed")
    else:
        print("Your file has not been removed")
else:
    print("Error: %s file not found" % file)
