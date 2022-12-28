import os 
import data_managment_helpers as dmh

new_folder_name = 'data_managment_text_file'
file_1_name = 'text_file.txt'
file_1_input= 'placeholder'
file_1_additional_input = ' add text \nnew line text \nanother new line text'

# change your directory 
# os.chdir('different_path')

#creating new folder 
new_folder_path = dmh.create_directory(new_folder_name)

# saving absolute and relative path to variable 
new_folder_abspath = os.path.abspath(new_folder_path)
new_folder_relpath = os.path.relpath(new_folder_path)

# saving directory and base name to variable 
new_folder_dirname = os.path.dirname(new_folder_path)
new_folder_basename = os.path.basename(new_folder_path)

dmh.display_directory_content(new_folder_path)

# creating new file with it content on set path 
file_1_path = os.path.join(new_folder_path, file_1_name)

with open (file_1_path, 'w') as file_1:
    file_1.write(file_1_input)

# displaying file content 
dmh.display_file_content(file_1_path)

# adding data to file and displaying it content 
with open (file_1_path, 'a') as file_1: 
    file_1.write(file_1_additional_input)

dmh.display_file_content(file_1_path)





