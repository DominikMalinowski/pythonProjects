filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("Uwielbiam ciostka\n")
    file_object.write("\tUwielbiam też czoko\n")
    
with open (filename, "a") as file_object:
    file_object.write("Dodawanie elementów w ogromnych zbiorach danych\n")
