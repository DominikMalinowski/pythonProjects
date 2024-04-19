#Write a program that:
#1. Creates a new file named 'data.txt' in the same directory as your program (check if it already doesn't exist) - use relative path!
#2. Opens the file in write mode and writes three words (e.g. 'one', 'two', 'three') to it - each one in new line
#3. Opens the file in read mode and reads all the lines, putting each word to list as a new element
#4. Deletes the created file

#import
import os


#words tuple, list, file alias
words = ('one', 'two', 'three')
list = []
file = "data.txt"

#create and open data.txt (if file exists, doesn't create)
def openFileWrite(file):
    textFile = open (file, "w+")
    return textFile

#write words tuple to file, word by word
def writeToFile(textFile):
    for x in words:
        textFile.write(x+"\n")
        
#close file
def closeFile(textFile):
    textFile.close()

#open file in read mode
def openFileRead(file):
    textFile = open(file, "r")
    return textFile

#read line by line from file, strip "\n",
def readFromFile(textFile):  
    for line in textFile:
        list.append(line.rstrip("\n"))
 
#print list
def printList():
    for x in list:
        print(x)

#check if file exists and delete file
def deleteFile(file):
    if os.path.exists(file):
        os.remove(file)
    else:
        print("Error. File doesn't exist!")



textFile = openFileWrite(file)
writeToFile(textFile)

closeFile(textFile)

textFile = openFileRead(file)
readFromFile(textFile)
printList()

closeFile(textFile)
deleteFile(file)