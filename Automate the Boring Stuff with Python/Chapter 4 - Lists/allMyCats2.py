catNames=[]
while True:
    print('Podaj imie kota numer ' +  str(len(catNames)+1) + ' (lub nic nie wpisuj zeby zakonczyć działanie programu)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('Oto imiona kotów:')
for name in catNames:
    print(' '+name)