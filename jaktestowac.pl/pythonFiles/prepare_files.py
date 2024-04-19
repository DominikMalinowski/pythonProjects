import os
import shutil


dir_path = os.path.join('testFiles','testDataSet')
file_to_copy = os.path.join('testFiles', 'dataSets', 'dataSetBase.txt')
copied_file_path = os.path.join(dir_path,'dataSet1.txt')
backup_copy = os.path.join(dir_path,'dataSet1copy.txt')
new_file_name = os.path.join(dir_path,'dataSet1copyRenamed.txt')


# creating dictionary
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# copy to testDataSets
if not os.path.exists(copied_file_path):
    shutil.copy(file_to_copy, copied_file_path)

# creating backup
if not os.path.exists(backup_copy):
    shutil.copy(copied_file_path, backup_copy)

# renaming backup
if os.path.exists(backup_copy):
    os.rename(backup_copy,new_file_name)
