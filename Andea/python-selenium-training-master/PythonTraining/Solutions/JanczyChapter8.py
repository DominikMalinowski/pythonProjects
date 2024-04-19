import os

# Function to delete given file
# parameter: file_path - string containing path to file
def deleteFile(file_path):
    os.unlink(file_path)

# Function to read from specific file
# parameter: file_path - string containing path to file
# return: content_list - list with each line from the file as separate element
def readFile(file_path):
    new_file = open(file_path)
    content_list = new_file.readlines()
    new_file.close()
    return content_list

# Function to write to specified file three words, if file doesn't exist it will be created
# parameter: file_path - string containing path to file
# parameter: first_word, second_word, third_word - strings containing words to be written to the file
def writeFile(file_path, first_word, second_word, third_word):
    new_file = open(file_path, 'w')
    new_file.write(first_word + '\n' + second_word + '\n' + third_word)
    new_file.close()

# Function to check if given file already exists
# parameter: file_path - string containing path to file
# return: result - Boolean containing information if file exists
def checkFileExist(file_path):
    result = os.path.exists(file_path)
    return result


# File name, words to be written into the file, file path
file_name = 'data.txt'
first_word = 'one'
second_word = 'two'
third_word = 'three'
file_path = '.\\' + file_name

# Information if the file with given name exists
if checkFileExist(file_path):
    print("File " + file_name + " already exists!")
else:
    print("File " + file_name + " doesn't exist")

# Write given words to file
writeFile(file_path, first_word, second_word, third_word)

# Create a list with words read form the file
content = readFile(file_path)

# Print content of the list
print(content)

# Delete the file
deleteFile(file_name)
