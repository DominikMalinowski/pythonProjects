"""
Write a program that:
1. Creates a new file named 'data.txt' in the same directory as your program (check if it already doesn't exist) - use relative path!
2. Opens the file in write mode and writes three words (e.g. 'one', 'two', 'three') to it - each one in new line
3. Opens the file in read mode and reads all the lines, putting each word to list as a new element
4. Deletes the created file
"""

import os

def create_file(path):
    # checking if file already exist
    if os.path.exists(path):
        print('File already exist')
    else:
        with open(path, 'w') as file:
            file.write('one, \ntwo, \nthree')
            file.close()

# reading all lines of file in read-only mode and putting each word to list as new element
def split_file(path):
    with open(path, 'r') as word_list:
        words = list(word_list.read().splitlines())
    print(words)

# deleting created file
def delete_file(path):
    os.remove(path)


create_file('.\data.txt')
split_file('.\data.txt')
delete_file('.\data.txt')