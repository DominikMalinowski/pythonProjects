""" Write a program that:
1. Creates two new files ('f1.txt' and 'f2.txt') in the same directory as your program (you can use code from Chapter 8)
2. Copies these files to the same directory but with different names ('f1-copy.txt' and 'f2-copy.txt')
3. Deletes files 'f1.txt' and 'f2.txt'
4. Creates a .zip file with added files 'f1-copy.txt' and 'f2-copy.txt' """

import os
import shutil
import zipfile

# create a .txt files in the same directory as your program
file1 = open('f1.txt', "w")
file2 = open('f2.txt', "w")


# copy files to the same destination but with different names
shutil.copy('f1.txt', 'f1-copy.txt')
shutil.copy('f2.txt', 'f2-copy.txt')

# close files
file1.close()
file2.close()

# deleting file: check if file exist and remove it - removing depends on user decision
decision = input("\nDo you want to delete the following files: '%s', '%s'? Press y/n. " % (file1.name, file2.name))
if decision == 'y':
    os.remove('f1.txt')
    os.remove('f2.txt')
    print("Your .txt files have been removed.")
else:
    print("Your .txt file has not been removed.")

# creating .zip files with the zip module
newZip = zipfile.ZipFile('new_zip.zip', "w")

# adding to .zip file
# first argument is a string of the filename to add. The second argument is the compression type parameter
newZip.write('f1-copy.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('f2-copy.txt', compress_type=zipfile.ZIP_DEFLATED)

# A ZipFile method (namelist()) - returns a list of strings for all the files and folders contained in the ZIP file
print('\nNew .zip file has been created. You compressed following files: ' + '\n' + str(newZip.namelist()))
