import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))

# get all sheets name 
print(wb.get_sheet_names())

#saving specyfic sheet as variable
sheet_3 = wb.get_sheet_by_name('Sheet3')
print(sheet_3.title)

# getting active sheet from the file 
active_sheet = wb.active
print(active_sheet.title)

# getting value from specyfic cell 
A1 = active_sheet['A1']

print(A1.coordinate)
print(A1.value)
print(A1.row)
print(A1.column)

for i in range (1, 8, 2):
    print(i, active_sheet.cell(row=i, column=2).value)
