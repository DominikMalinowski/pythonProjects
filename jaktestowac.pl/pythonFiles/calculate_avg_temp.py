import os.path
from calculate_avg_temp_mock import calc_average

directory_name = 'pythonFiles'
folder_name = 'testFiles'
file_name = 'temperature.txt'
path = os.path.join(folder_name, file_name)

with open(path, 'r') as file:
    content = file.readlines()

average_value = calc_average(content)
print(f'Average value: {average_value}')

result_file_name = 'temperature_avg.txt'
result_path = os.path.join(folder_name, result_file_name)
with open(result_path, 'a') as result:
    result.write(f'\nAverage value: {average_value}')
    print('Average saved')

