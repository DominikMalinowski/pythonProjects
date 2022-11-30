import os

dir_path = os.path.join('testFiles','testDataSet')
file_to_copy = os.path.join('testFiles', 'dataSets', 'dataSetBase.txt')
copied_file_path = os.path.join(dir_path,'dataSet1.txt')
backup_copy = os.path.join(dir_path,'dataSet1copy.txt')
new_file_name = os.path.join(dir_path,'dataSet1copyRenamed.txt')

all_file = [
dir_path,
copied_file_path,
backup_copy,
new_file_name,
]

for file in all_file:
    if os.path.exists(file):
        os.remove(file)