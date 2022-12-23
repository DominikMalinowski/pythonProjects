#zadanie 9.13 
from random import randint

class Die():
     
    def __init__(self):
        """Inicjalizacja"""

    def roll_die(self,sides): 
        self.sides = sides
        print(randint(1,sides))

six_die = Die()
six_die.roll_die(6)

ten_die = Die()
ten_die.roll_die(10)

twnety_die = Die()
twnety_die.roll_die(20)

#zadanie 9.14 

from random import choice 

lista = ['a','k','r','p','b',1,56,23,78,99,25,44,69,85,31]
wygrane = set([])


class Losowanko(): 
    def __init__(self):
        """Inicjalizowanko"""
    def losowanie(self):
        while len(wygrane) < 4:
            los = choice(lista)
            wygrane.add(los)

losowanie = Losowanko()
losowanie.losowanie()
print(wygrane)


#zadanie 9.15 
ticket = set(['a',23,'r',99])
ilosc = 0 

#c = wygrane.issuperset(ticket)
#while c == False:
#    ilosc += 1
#print(ilosc)
