# opening excel file 
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')

# getting active spreadsheet 
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')
active_sheet = workbook.get_active_sheet()

# getting spreadsheet by name 
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')
sheet = workbook.get_sheet_by_name('{sheet_name}')

# gettin cell and it's value from spreadsheet 
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')
sheet = workbook.get_sheet_by_name('{sheet_name}')
cell = sheet['A1']
cell2 = sheet(row=1, column =2)
cell.value 
cell2.value

# gettin coordiante and value from spreadsheet 
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')
sheet = workbook.get_sheet_by_name('{sheet_name}')
cell = sheet['A1']
coordinate = cell.coordinate 
value = cell.value  

# changing spreadsheet name
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')
sheet = workbook.get_sheet_by_name('{sheet_name}')
sheet.title = '{new title}'

# saving spreadsheet
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')
sheet = workbook.get_sheet_by_name('{sheet_name}')
workbook.save('{new_file_name_with_extension}')

 # creating spreadsheet 
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')
workbook.create_sheet('{new_sheet_name}')

# removing spreadsheet
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')
workbook.remove_sheet('{sheet_to_remove}')

# populating cell 
import openpyxl
workbook = openpyxl.load_workbook('{file_name}')
sheet = workbook.get_sheet_by_name('{sheet_name}')
sheet['A1'] = 'Placeholder'
