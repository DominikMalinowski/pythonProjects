'''
Write a program that:
1. Creates two new files ('f1.txt' and 'f2.txt') in the same directory as your program (you can use code from Chapter 8)
2. Copies these files to the same directory but with different names ('f1-copy.txt' and 'f2-copy.txt')
3. Deletes files 'f1.txt' and 'f2.txt'
4. Creates a .zip file with added files 'f1-copy.txt' and 'f2-copy.txt'
'''
import os
import zipfile
from shutil import copyfile

def Chapter9():
#Creating originals
    mylist = ["one","two","three","four","six","seven"]
    filenames = ["f1","f2"]
    try:
        for ind in filenames:
            file = open(ind+".txt","x+")
            for j in range(3):
                file.write(mylist[j]+"\n")
                j += 1
            file.close()
    except FileExistsError:
        print("File already exists.")

#Copying the files and removing originals
    for ind in filenames:
        copyfile(ind+".txt", ind+" - copy.txt")
        os.remove(ind+".txt") 

#Creating Archive
    print("Creating archive")
    zf = zipfile.ZipFile("zipfile_write.zip", mode="w")
    try:
        for ind in filenames:
            print("adding "+ind+"- copy.txt")
            zf.write(ind+" - copy.txt")
    finally:
        print("closing")
        zf.close()
        
Chapter9()