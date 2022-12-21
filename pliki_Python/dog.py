class Dog(): 
    """Prosta próba modelowania psa"""
    def __init__(self, name, age): 
        """Inicjalizacja atrybutów name i age"""
        self.name = name
        self.age = age

    def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecenia"""
        print(f'{self.name.title()} teraz siedzi')

    def roll_over(self):
        """Symulacja,  zę pies kładzie się na plecy po otrzymaniu polecenia"""
        print(f'{self.name.title()} teraz położył się na plecach')


my_dog = Dog('willie',6)
print(f'Mój pies ma na imię {my_dog.name.title()}')
print(f'Mój pies ma {my_dog.age} lat')

my_dog = Dog('willie',6)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy',5)
print(f'\nMój pies ma na imię {your_dog.name.title()}')
print(f'Mój pies ma {your_dog.age} lat')
your_dog.sit()
your_dog.roll_over()
