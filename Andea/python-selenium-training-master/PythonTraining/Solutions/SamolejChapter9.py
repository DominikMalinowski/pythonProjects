#Write a program that:
#1. Creates two new files ('f1.txt' and 'f2.txt') in the same directory as your program (you can use code from Chapter 8)
#2. Copies these files to the same directory but with different names ('f1-copy.txt' and 'f2-copy.txt')
#3. Deletes files 'f1.txt' and 'f2.txt'
#4. Creates a .zip file with added files 'f1-copy.txt' and 'f2-copy.txt'

#imports
import os 
from shutil import copyfile
import zipfile 

#aliases
file1 = "f1.txt"
file2 = "f2.txt"
file1copy = "f1-copy.txt"
file2copy = "f2-copy.txt"

#creates new file, deletes old which has the same name
def createFileDeleteOld(file):
    if os.path.exists(file):
        os.remove(file)
    textFile = open (file, "x")
    return textFile

#copy file
def copyFile(file, copy):
    copyfile(file, copy)
    print ("File " + file + " has been deleted.")
    return copy

#close file
def closeFile(textFile):
    textFile.close()

#delete file
def deleteFile(file):
    if os.path.exists(file):
         os.remove(file)
    else:
        print("Error. File doesn't exist!")



#zip files
def zipFiles(file, zipFile):
    zipFile.write(file, compress_type=zipfile.ZIP_DEFLATED)     #(file, parameter)
    



textFile1 = createFileDeleteOld(file1)
textFile2 = createFileDeleteOld(file2)

textCopy1 = copyFile(file1, "file1-copy")
textCopy2 = copyFile(file2, "file2-copy")

closeFile(textFile1)
closeFile(textFile2)

deleteFile(file1)
deleteFile(file2)


zipFile = zipfile.ZipFile('aZipFile.zip', "w")
zipFiles(textCopy1, zipFile)
zipFiles(textCopy2, zipFile)
zipFile.close()