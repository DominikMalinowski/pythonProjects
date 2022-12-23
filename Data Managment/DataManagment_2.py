import os 

new_folder_name = 'data_managment_text_file'
different_path = 'xxxxxxxxxxxxx' #<-place for destination directory  

# change your directory 
# os.chdir('different_path')

# getting current working directory
main_directory = os.getcwd()

# genearate path for new file in cwd 
new_folder_path = os.path.join(main_directory, new_folder_name)

# create new dir if not exist 
os.makedirs(new_folder_path, exist_ok=True)

new_folder_abspath = os.path.abspath(new_folder_path)
new_folder_relpath = os.path.relpath(new_folder_path)

new_folder_dirname = os.path.dirname(new_folder_path)
new_folder_basename = os.path.basename(new_folder_path)

# # displaying directory content and it size 
# content = os.listdir(new_folder_path)
# print(f"\nDirectory containes items: [item size]")
# for item in content: 
#     item_path = os.path.join(new_folder_path, item)
#     size = os.path.getsize(item_path)
#     print(item + " : " + str(size) + " kb")

# if os.path.isabs(new_folder_path) == True:
# 	print('co?')
# else: 
# 	print('test has failed!')