import os
import shutil

file_path = os.path.join('testFiles','fileToCopy.txt')
new_file_path = os.path.join('testFiles', 'copiedFile.txt')

shutil.copy(file_path, new_file_path)
