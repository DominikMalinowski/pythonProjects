import os
import shutil
import zipfile

# Function to create file
# parameter: file_path, string containing absolute, or relative path to file
def createFile(file_path):
    new_file = open(file_path, 'w')
    new_file.close()

# Function to check if given file already exists
# parameter: file_path, string containing absolute, or relative path to file
# return: result - Boolean containing information if file exists
def checkFileExist(file_path):
    result = os.path.exists(file_path)
    return result

# Function to delete specified file
# parameter: file_path, string containing absolute, or relative path to file
def deleteFile(file_path):
    os.unlink(file_path)

# Function to copy specified file into cuurent directory with new name
# parameter: current_path, string containing current working directory
# parameter: file_name, string containing name of the file to be copied
# parameter: copy_name, string containing name of teh copy
# return: string containing file path to created copy
def copyFile(current_path, file_name, copy_name):
    path_to_be_copied = current_path + '\\' + file_name
    path_copy = current_path + '\\' + copy_name

    copied_file_path = shutil.copy(path_to_be_copied, path_copy)
    return copied_file_path

# Function to compress file and add it to .zip file, if file doesn't exist it will be created
# parameter: file_name, string containing name of the file to be compressed
# parameter: archive_name, string containing name of the archive to which file will be added
def compressFile(file_name, archive_name):
    new_zip = zipfile.ZipFile(archive_name, 'a')
    new_zip.write(file_name, compress_type=zipfile.ZIP_DEFLATED)




# File name, words to be written into the file, file path
original_file_1 = 'f1.txt'
original_file_2 = 'f2.txt'
first_word = 'one'
second_word = 'two'
third_word = 'three'
copy_name_1 = 'f1-copy.txt'
copy_name_2 = 'f2-copy.txt'

# Create relative path to original files
relative_path_1 = '.\\' + original_file_1
relative_path_2 = '.\\' + original_file_2

# Get current working directory
working_directory_path = os.getcwd()

# Create original files
createFile(relative_path_1)
createFile(relative_path_2)

# Copy original files
copyFile(working_directory_path, original_file_1, copy_name_1)
copyFile(working_directory_path, original_file_2, copy_name_2)

# Delete original files
deleteFile(relative_path_1)
deleteFile(relative_path_2)

# Compress to .zip file
compressFile(copy_name_1, 'copies.zip')
compressFile(copy_name_2, 'copies.zip')

