## funkcja wyświetlająca na ekranie argument funkcji print
print('Hello')

## funkcja wyświetlająca ilość znaków w argumencie zmiennej
slowo = 'abecadlo'
print(len(slowo))

## sprowadzenie wartości do konkretnego rodzaju
print(int(1.99))
print('Ala ma ' + str(42) + ' koty')
print(float(10))

## zapisanie wproawdzonych danych jako wartości INTEGER
spam = input()
print(spam)
spam = int(spam)
print(spam +2)

## funkcja round() zaokrągla liczbę do konkretnej ilości miejsc po przecinku
x = round(456.2132, 2)
print(x)

## klazula if + else - sprawdza warunek jeżeli jest TRUE to go wykonuje, jeżeli FALSE to wykonuje else-a
print('Jak Ci na imie ?')
user_name = input()
if user_name == "Dominik":
    print('Hello Dominik')
else:
    print('Arka Gdynia Kurwa Swnia')

## klazula elif - sprawdza drug warunek tylko, jżeli pierwszy jest FALSE
print('Jak Ci na imie ?')
user_name = input()
print('Ile masz lat ?')
user_age = input()
if user_name == 'Dominik':
    print('Witam')
elif int(user_age) > 18:
    print('kutwa')
else:
    print('Wypad')

## petla while oczekujaca wpisania swojego imienia przez uzytkownika
name =''
while name != 'swoje imie':
    print('Prosze wpisac swoje imie')
    name = input()
print('Dziekuje')

## petla while z poleceniem break
while True:
    print('Prosze wpisac swoje imie')
    name = input()
    if name == 'swoje imie':
        break
print('Dziekuje')

## petla while z poleceniem continue
while True:
    print('Kim jestes ?')
    name = input()
    if name != 'Janek': #jezeli uzytkownik poda inne imie niz Janek to petla uruchomi sie od nowa
        continue
    print('Witaj Janek, jakie jest haslo ?')
    password = input()
    if password == 'miecznik':
        break
    print('Masz dostep')

## petla for + polecenie range()
total = 0
for i in range(101):
    total = total + int(i)
print(total)

## argumenty funkcji range()
for i in range(1, 10, 2): #od 1 do 10 z przeskokiem o 2
    print(i)

for i in range (1, -5, -1): # od 1 do -5 z przeskokiem o -1
    print(i)

## wyswietlanie randomowej liczby z przedzialu 1 do 10 za pomoca modulu "random"
import random
for i in range(5):
    print(random.randint(1,10))

##funkcja hello wyswietlajaca powitania
def hello():
    print("Czesc")
    print('Hello')
    print('Witajcie')

hello()

## wywołanie konkretnego elementu listy z innej listy
spam = [['kot','pies'],[10,20,30]]
print(spam[1][2])

## przypisanie wielu jednoczesnych operacji przypisania
kot = ['gruby','czarny','głośny']
size, color, disposition = kot
print(kot)
## odszukiwanie konkretnej wartości z listy
spam = ['witaj','czesc','siemasz','hej']
print(spam.index('hej'))

## dodawanie wartosci do listy (dodaje na koncu listy)
spam = ['kot','pies','nietoperz']
spam.append('łoś')
print(spam)

## dodawanie wartosci do listy (dodaje w konkretnej pozycji listy)
spam = ['kot','pies','nietoperz']
spam.insert(1,'łosoś')
print(spam)

## usuwanie wartosci z listy (tylko jeden rekord zostanie usuniety)
spam = ['kot','nietoperz', 'szczur', 'słoń', 'kot', 'kapelusz', 'kot']
spam.remove('kot')
print(spam)

# usuwanie wartosci z listy
spam2 = ['kot','nietoperz', 'szczur', 'słoń']
spam2.remove('nietoperz')
print(spam2)

## sortowanie zawartosci listy
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

## sortowanie zawartosci listy w odwrotnej kolejnosci
spam = [2, 5, 3.14, 1, -7]
spam.sort(reverse=True)
print(spam)

## sortowanie alfabetyczne listy
spam = ['a', 'Z', 'b', 'P']
spam.sort()
print(spam)

spam2 = ['a', 'Z', 'b', 'P']
spam2.sort(key=str.lower)
print(spam2)

## kontynuacjia działania w nowym wierszu
print('Cztery dwudziestki i siedem' + \
      ' lat temu...')

## działania na ciągu można uzywać również na liście
name = 'Zophie'
print(name[-2])
print(name[0:4])
print('zo' in name)
print('p' not in name)
for i in name:
    print('*** '+ i + ' ***')

## krotka (w nawiasach okrągłych i niemodyfikowalna)
eggs = ('witaj', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

## zamiana listy na krotke i vice versa
print(tuple(['kot','pies',5]))
print(list(('kot','pies',5)))
print(list('witaj'))

##
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Witaj'
print(spam)
print(cheese)

## kopiowanie listy (duplikat)
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

##
spam = {'color':'red', 'age':'42'}
print(spam.keys())
print(spam.values())
print(spam.items())

## metoda get() pobiera wartosć ze słownika, a jezeli jej nie znajdzie to podaje wpisaną
picnicItems = {'apples':'5', 'cups':'2'}
print('Przyniosę '+ str(picnicItems.get('cups',0)) + ' kubki')
print('Przyniosę '+ str(picnicItems.get('eggs',0)) + ' jajka')

## metoda setdefault()
spam = {'name':'Pooka','age':'5'}
print(spam.setdefault('color','czarny'))#przypisanie wartości 'czarny' jezeli nie ma nic dla klucza color

spam = {'name':'Pooka','age':'5','color':'czarny'}
print(spam.setdefault('color','biały'))

## ładne wyświetlenie zawartosci słownika
import pprint
message = 'Był jasny, zimny  dzien kwietniowy i zegary biły trzynastą'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

pprint.pprint(count)

##Literały ciągu tekstowego
print("To jest pies Pana O'Hary") #użycie cudzysłowiu
print('To jest pies Pana O\'Hary') #użycie znaku sterującego
print(f'To jest kot Pana O\Hary') #niezmodyfikowany ciąg tekstowy (raw string)

## wyświetlanie wszystkich znaków jako duże litery
spam = 'witaj świecie'
print(spam.upper())

## wyświetlanie wszystkich znaków jako małe litery
spam = 'witaj świecie'
print(spam.upper())

## sprawdzenie czy wszystkie litery są
spam = 'witaj świecie'
print(spam.islower()) #duże
print(spam.isupper()) #małe
print(spam.isalnum()) #alfanumryczne
print(spam.isalpha()) #numeryczne
print(spam.isdecimal()) #zmiennoprzecinkowe
print(spam.istitle()) #Tytułem

## sprawdzanie rozpoczęscia/ zakończenia
spam = 'Witaj świecie'
print(spam.startswith('Witaj'))
print(spam.endswith('świecie'))

## łączenie ciągów tekstowych
print(', '.join(['koty','psy','ptaki']))
print(' '.join(['Mam','na','imię','Janusz']))
print('-Kurwa-'.join(['Arka','Gdynia','Kurwa','Świnia']))

## rozdzielanie ciągów tekstowych
spam = 'Ala ma kota'
print(spam.split())
print('Arka-Kurwa-Gdynia-Kurwa-Kurwa-Kurwa-Świnia'.split('-Kurwa-')) #podzielenie znakiem '-kurwa-'

## justowanie prawe/lewe/środkowe
spam = 'Chuj'
print(spam.rjust(20, '*'))
print(spam.ljust(12,'-'))
print(spam.center(15,'='))

## usuwanie białych znaków
spam = '......Witaj Świecie......'

print(spam.strip('.'))
print(spam.lstrip('.'))
print(spam.rstrip('.'))

## wywoływanie ściezki
import os
print(os.path.join('user','bin','spam'))

## pobieranie bieżącego katalogu roboczego
import os
print(os.getcwd())

## modyfikacja katalogu roboczego
import os
os.chdir('<sciezka>')

## tworzenie nowego katalogu
import os
os.makedirs('C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\newborn')

## zwrocenie bezwzglednej sciezki argumentu
os.path.abspath('newborn')

## zwrocenie True jezeli argument jest bezwzgledna sciezka
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
path = 'C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\pliki_python_2\\hello.txt'
hello_file = open(path)

hello_content = hello_file.read()
print(hello_content)

path2 = 'C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\pliki_python_2\\Lorem Ipsum.txt'
print(open(path2).readlines())

## otwieranie w róznych trybach
path = 'C:\\Users\\Dominik Malinowski\\Desktop\\pythonProject\\pliki_python_2\\hello.txt'
file_read = open(path, 'r')
file_write = open(path, 'w')
file_add = open(path, 'a')

# utworzenie pliku z otwarciem go w trybie pisania
bacon_file = open('bacon.txt', 'w')
bacon_file.write('Hello World\n')

bacon_file.close()
bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bekon is not a wegetable\n')

bacon_file.close()
bacon_file = open('bacon.txt')
content = bacon_file.read()
print(content)

## zapisanie zmiennej do pliku
import shelve
shel_file = shelve.open('mydata')
cats = ['Sophie', 'Pooka', 'Simon']
shel_file['cats'] = cats
shel_file.close()

## wywołanie zmiennej z pliku
shel_file = shelve.open('mydata')
print(type(shel_file))
print(shel_file['cats'])
shel_file.close()

## kopiowanie pliku do folderu i do folderu ze zmianą nazwy
import shutil, os
os.chdir('C:\\')

shutil.copy('C:\\spam.txt', 'C:\\Users\\DELL\\Desktop\\delicious')
shutil.copy('C:\\spam.txt', 'C:\\Users\\DELL\\Desktop\\delicious\\spam2.txt')

##  kopiowanie folderu z zawartością
import shutil, os
os.chdir('C:\\')
shutil.copytree('C:\\bacon', 'C:\\Users\\DELL\\Desktop\\backon_backup')

##  kopiowanie folderu z zawartością
import shutil, os
os.chdir('C:\\')
shutil.move('c:\\bacon', 'C:\\Users\\DELL\\Desktop')

## usuwanie plików i katalogu
import shutil, os
os.chdir('C:\\')
os.unlink('path') # usunięcie pliku z podanej ścieżki
os.rmdir('path') # usunięcie pustego katalogu z podanej ścieżki
os.rmtree('path') # usunięcie katalogu i jego plików z podanej ścieżki

## bezpieczne usuwanie plików
import send2trash

baconfile = open('bacon.txt', 'a')
baconfile.write('Becon isn"t vegetable')
baconfile.close()
send2trash.send2trash('bacon.txt')

## wyświetlanie katalogów i folderów przechodząć przez ścieżke
import os
for folder_name, sub_folders, file_names in os.walk('C:\\Users\\DELL\\Desktop\\pythonProject\\Andea'):
    print('Curren dictionary: ' + folder_name)
    for sub_folder in sub_folders:
        print('Subfolder of the folder: ' + folder_name + ':' + sub_folder)
        for file_name in file_names:
            print('Catalog file: ' + folder_name + file_name)

## dane dot. plików zip
import zipfile, os
os.chdir('C:\\Users\\DELL\\Desktop\\pythonProject\\Andea')
example_Zip = zipfile.ZipFile('example.zip')
print(example_Zip.namelist())
spamInfo = example_Zip.getinfo('example/spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Skompresowany plik jes %sx mniejszy!' %(round(spamInfo.file_size/spamInfo.compress_size, 2)))
example_Zip.close()

## rozpakowanie pliku zip
import zipfile, os
os.chdir('C:\\Users\\DELL\\Desktop\\pythonProject\\Andea')
example_Zip = zipfile.ZipFile('example.zip')
example_Zip.extractall() #rozpakowanie wszystkiego do bieżącego katalogu
example_Zip.extract('spam.txt','C:\\Users\\DELL\\Desktop\\pythonProject') #rozpakowanie konkretnego pliku do konkretnego katalogu
example_Zip.close()

## tworzenie pliku zip
import zipfile
newZip = zipfile.ZipFile('new.zip', 'w') #utworzenie pliku w trybie zapisu (nadpisanie wszystkiego)
newZip2 = zipfile.ZipFile('new.zip', 'a') #utworzenie pliku w trybie dołączania (dopisanie )
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip2.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

##
