import os, shutil, zipfile


# Create file function
def create_file(file_name):
    try:
        file = open(file_name, 'x')
        file.close()
        print('File ' + file_name + ' has been created')
    except:
        print('File ' + file_name + ' already exist')


# Copy and rename file function
def copy_file(file_name, new_file_name):
    try:
        shutil.copy(file_name, new_file_name)
        print(file_name + ' has been copied to ' + new_file_name)
    except:
        print(file_name + ' does not exist and can\'t be copied')


# Remove file function
def remove_file(file_name):
    try:
        os.unlink(file_name)
        print(file_name + ' has been deleted')
    except:
        print(file_name + ' does not exist and can\'t be deleted')


# Zip file creation function
def zip_file(file_list, zip_Name):
    new_Zip = zipfile.ZipFile(zip_Name, 'w')
    for i in file_list:
        try:
            new_Zip.write(i, compress_type=zipfile.ZIP_DEFLATED)
            print(i + ' has been added to zip file')
        except:
            print(i + ' does not exist and can\'t be added to .zip file')
    new_Zip.close()



# Creation of files
create_file('f1.txt')
create_file('f2.txt')

# Copying files
copy_file('f1.txt', 'f1-copy.txt')
copy_file('f2.txt', 'f2-copy.txt')

# Deleting files
remove_file('f1.txt')
remove_file('f2.txt')

# Creation of .zip file
zip_file(['f1-copy.txt', 'f2-copy.txt'], 'ZIP.zip')