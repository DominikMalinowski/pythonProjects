#Method for conversion of pyobdc.Row to list

def convertSingleColumnToList(pyobject):
    row_to_list = []
    for row in pyobject:
        row_to_list = [elem for elem in row]
    return row_to_list