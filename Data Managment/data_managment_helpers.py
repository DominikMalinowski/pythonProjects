
import os 
import shutil

# creating new directory 
def create_directory(new_folder_name):
    main_directory = os.getcwd()
    new_folder_path = os.path.join(main_directory, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    return new_folder_path

# displaying file content 
def display_file_content(path_to_file):
    with open (path_to_file, 'r') as readed_file: 
        content = readed_file.read()
        print(f'\n' + content)

# displaying directory content and it size 
def display_directory_content(path):
    content = os.listdir(path)
    print(f"\nDirectory containes below items: ")
    for item in content: 
        item_path = os.path.join(path, item)
        size = os.path.getsize(item_path)
        print(item + " : " + str(size) + " kb")

# creating copy of the file 
def copy_file(file_to_copy, destination_for_copy):
    if os.path.exists(file_to_copy) == True:
        if os.path.exists(destination_for_copy) == False:
            shutil.copy(file_to_copy, destination_for_copy)
        else:
            print('Copy of the file already exist')
    else:
        print('File to copy dont exist')

# renaming the file 
def rename_file(old_name, new_name):
    if os.path.exists(old_name) == True:
        if os.path.exists(new_name) == False:
            os.rename(old_name, new_name)
        else:
            print("There is already file with provided name")
    else:
        print("There isn't any file with that name in given location")

# removing the file
def file_remove(file_to_remove):
    if os.path.exists(file_to_remove):
        os.remove(file_to_remove)
    else:
        print('File to remove does not exist')

# checking if the file exist 
def exist_check(file):
    if os.path.exists(file) == True:
        pass
    else:
        print("There isn't any file with that name in given location")

        
# adding data to file 
def add_to_file(file, input):
    exist_check(file)
    with open (file, 'a') as file_1: 
        file_1.write(input)