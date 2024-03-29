
## modyfikacja katalogu roboczego
import os
os.chdir('<sciezka>')

## tworzenie nowego katalogu
import os
os.makedirs('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn', exist_ok=True)

## zwrocenie bezwzglednej sciezki argumentu
import os
print(os.path.abspath('newborn'))

## zwrocenie True jezeli argument jest bezwzgledna sciezka
import os
print(os.path.isabs('newborn'))

## zwrocenie wzglednej sciezki argumentu
import os
print(os.path.relpath('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn', 'Desktop'))

## zwrocenie nazwy katalogu i nazwy bazowej (rozdziela je ostatni ukośnik)
import os
print(os.path.dirname('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn'))

print(os.path.basename('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn'))

## zapisanie do zmiannej lokalizacji podzielonej ostatnim ukośnikiem
import os
path =('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn')
print(os.path.split(path))

## zapisanie do zmiannej lokazliacji podzielonej ukośnikami
import os
path =('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn')
print(path.split(os.path.sep))

## wyswietlenie zawartosci katalogu
import os
path =('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn')
print(os.listdir(path))

## pobranie wagi pliku (bajty)
import os
path =('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn\\reg.ex.png')
print(os.path.getsize(path))

## wyswietlenie wagi całego folderu
path = 'E:\\PyCharm\\PyCharm Community Edition 2021.2.3'
totalSize = 0
for file in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path, file))
print(totalSize)

## sprawdzenie czy sciezka istnieje
import os
path =('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn\\reg.ex.png')
print(os.path.exists(path))

## sprawdzenie czy sciezka prowadzi do pliku
import os
path =('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn\\reg.ex.png')
print(os.path.isfile(path))

## sprawdzenie czy sciezka prowadzi do katalogu
import os
path =('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn\\reg.ex.png')
print(os.path.isdir(path))

## otwieranie, odczytywanie danych z pliku
import os
path = './pliki_python_2/hello.txt'
hello_file = open(path)

hello_content = hello_file.read()
print(hello_content)

path2 = './pliki_python_2/Lorem Ipsum.txt'
print(open(path2).readlines())

## otwieranie w róznych trybach
path = 'C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\pliki_python_2\\hello.txt'
file_read = open(path, 'r')
file_write = open(path, 'w')
file_add = open(path, 'a')

## zmiana nazwy plikó
import os
old_file = os.path.join('testFiles', 'fileToRename.txt')
new_file = os.path.join('testFiles', 'renamedFile.txt')
os.rename(old_file, new_file)

## bezpieczne usuwanie plików
import os

file_path = os.path.join('testFiles', 'fileToRemove.txt')

if os.path.exists(old_file):
    os.remove(file_path)
else:
    print('File to remove does not exist')

## kopiowanie plików
import shutil
import os

file_path = os.path.join('testFiles', 'fileToCopy.txt')
new_file_path = os.path.join('testFiles', 'copiedFile.txt')

shutil.copy(file_path, new_file_path)
