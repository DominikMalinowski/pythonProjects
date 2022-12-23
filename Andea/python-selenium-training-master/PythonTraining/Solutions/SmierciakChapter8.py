'''
Write a program that:
1. Creates a new file named 'data.txt' in the same directory as your program (check if it already doesn't exist)
use relative path!
2. Opens the file in write mode and writes three words (e.g. 'one', 'two', 'three') to it - each one in new line
3. Opens the file in read mode and reads all the lines, putting each word to list as a new element
4. Deletes the created file

'''
import os

def Chapter8():
    mylist = ["one","two","three"]
    try:
        file = open("karolfile.txt","x+")
        for i in range(3):
            file.write(mylist[i]+"\n")
            i += 1
        file.close()
    except FileExistsError:
        print("File already exists.")

    try:
        lineList = [line.rstrip('\n') for line in open("karolfile.txt","r")]
    except FileNotFoundError:
        print("File does not exists.")

    print(lineList)

    os.remove("karolfile.txt") 

Chapter8()