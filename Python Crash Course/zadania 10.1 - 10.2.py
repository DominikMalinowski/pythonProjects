#zadanie 10.1 
#odczytanie całego pliku 
filename = 'learning_python.txt' 
with open (filename) as file_object: 
    content = file_object.read()
print(content.rstrip())
print(f'\n')

#odczytanie po wierszach 
filename = 'learning_python.txt' 
with open (filename) as file_object: 
    for line in file_object: 
        print(line.rstrip())
print(f'\n')

#odczytanie przez liste wierszy 
filename = 'learning_python.txt' 
with open (filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

message = "Moje ulubione zwierze to kot"
print(message.replace('kot','pies'))
