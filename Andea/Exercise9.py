#! python 3
"""
Write a program that:
1. Creates two new files ('f1.txt' and 'f2.txt') in the same directory as your program (you can use code from Chapter 8)
2. Copies these files to the same directory but with different names ('f1-copy.txt' and 'f2-copy.txt')
3. Deletes files 'f1.txt' and 'f2.txt'
4. Creates a .zip file with added files 'f1-copy.txt' and 'f2-copy.txt'
"""
import os, shutil

def create_file(path, content):
    # checking if file already exist
    if os.path.exists(path):
        print('File already exist')
    else:
        with open(path, 'w') as file:
            file.write(content)
            file.close()

create_file('.f1.txt', 'placeholder')
create_file('.f2.txt', 'this_2')


def copy_file(source,destination):
   shutil.copy(source, destination + 'copy')