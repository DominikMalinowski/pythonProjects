# V 1.1 - 21.05.2019

"""
Write a program that:
1. Creates a new file named 'data.txt' in the same directory as your program (check if it already doesn't exist) - use relative path!
2. Opens the file in write mode and writes three words (e.g. 'one', 'two', 'three') to it - each one in new line
3. Opens the file in read mode and reads all the lines, putting each word to list as a new element
4. Deletes the created file
"""
import os

try:
    #creating new text file ("xt" - textfile (default))
    with open("data.txt", "xt") as f:
        #writing in file
        f.write("one")
        f.write("\ntwo")
        f.write("\nthree")
#if file already exists
except FileExistsError:
    print("File already exists")

#open file in reading mode
with open("data.txt", "r") as f:
#read content of this file. Each '\n' is treated as new line
    print(f.read().splitlines())
#removing textfile
os.remove("data.txt")

