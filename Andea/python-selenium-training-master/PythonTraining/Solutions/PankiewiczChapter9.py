# V 1.0 - 15.05.2019
"""
Write a program that:
1. Creates two new files ('f1.txt' and 'f2.txt') in the same directory as your program (you can use code from Chapter 8)
2. Copies these files to the same directory but with different names ('f1-copy.txt' and 'f2-copy.txt')
3. Deletes files 'f1.txt' and 'f2.txt'
4. Creates a .zip file with added files 'f1-copy.txt' and 'f2-copy.txt'
"""

import os
import shutil
import zipfile

#creating new text files ("xt" - textfile (default))
f = open("f1.txt", "xt")
f = open("f2.txt", "xt")

#copying of text files
shutil.copyfile("f1.txt", "f1-copy.txt")
shutil.copyfile("f2.txt", "f2-copy.txt")

#closing of this text file- we can not read from it, but we can remove it
f.close()

#removing textfile
os.remove("f1.txt")
os.remove("f2.txt")

#creating of a new zip file- write mode
newZip = zipfile.ZipFile('AP_new.zip', 'w')

#additing textfiles to the zip file
newZip.write("f1-copy.txt")
newZip.write("f2-copy.txt")

#closing of a zip file
newZip.close()