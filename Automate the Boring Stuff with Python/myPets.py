print('siemasz' in ['witaj', ' czesc', 'siemasz', ' hejska'])

spam = ['witaj', ' czesc', 'siemasz', ' hejska']
print('kot' in spam)

print('siemasz' not in spam)

print('kot' not in spam)

##
myPets = ['Zophie','Pooka','Fat-tail']
print('Podaj imie zwierzaka')
name = input()
if name not in myPets:
    print('Nie mamy zwierzaka o imieniu ' +name)
else:
    print(name + ' to mój zwierzak')

##
kot = ['gruby','czarny','głośny']
size, color, disposition = kot

##
spam = ['witaj','czesc','siemasz','hej']
print(spam.index('hej'))