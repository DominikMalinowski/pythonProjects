import os


old_file = os.path.join('testFiles', 'fileToRename.txt')
new_file = os.path.join('testFiles', 'renamedFile.txt')

if os.path.exists(old_file):
    os.rename(old_file, new_file)
else:
    print('Old file does not exist')

if not os.path.exists(new_file):
    os.rename(old_file, new_file)
else:
    print('New file already exist')