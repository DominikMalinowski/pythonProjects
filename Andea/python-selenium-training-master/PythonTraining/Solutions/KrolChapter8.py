import os,re

# Creating a data.txt file in current directory (If it not exist)
if os.path.isfile(r'./data.txt'):
    print('File already exists - it will be rewrite')  # Do it if file exist
    open_file = open('./data.txt', 'w')  # Open and write on existing file
else:
    print('File does not exists - Creating new one')  # Do it if file not exist
    open_file = open('./data.txt', 'w')  # Create and open file in write mode

# Writing in file
open_file.write('One\nTwo\nThree')
open_file.close()

# Open file in read mode and save all words in to table
open_file = open('./data.txt')
wordRe = re.compile(r'\w+')  # Regex to find words
table_of_words = wordRe.findall(open_file.read())
print(table_of_words)
open_file.close()

# Deleting the file
os.unlink('data.txt')
print('File is deleted')