from random import randint 
print(randint(1,100))

from random import choice
lista = ['a','k','r','p','b',1,56,23,78,99,25,44,69,85,31] #utworzenie listy z warotściami 
wygrane = set([]) #utworzenie set-u o nazwie "wygrane" 
while len(wygrane) < 4: #jeżeli długość set-u wygrane jest mniejsza niż 4 to:
    los = choice(lista) #wywołanie randomowej wartości z listy "lista" 
    wygrane.add(los) #dodanie do set-y "wygrane" zmiennej "los"
print(wygrane)