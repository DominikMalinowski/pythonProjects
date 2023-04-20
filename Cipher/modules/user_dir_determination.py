import os 

def user_dir_determination():
    file_path = input()

    user_directory = os.path.basename(file_path)
    dir = os.path.dirname(file_path)

    print(user_directory)
    print(dir)

user_dir_determination()