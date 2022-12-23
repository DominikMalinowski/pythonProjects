#przechowywanie informacji o pizzy zamówionej przez klienta 
#pizza = {
#    "crust": "grubym",
#    "toppings": ["pieczarki","podwójny ser"],
#    }

#podsumowanie zamówienia 
#print(f"Zamówiłes pizze na {pizza['crust']} cieście"
#    "wraz z następującymi dodatkami:")
#for topping in pizza['toppings']:
#    print(f"\t {topping}")

def make_pizza(size, *toppings):
    print(f"\nPrzygotowywuje pizzę o wielkości {size} cm, z nast. dodatkami:")
    for topping in toppings:
        print(f"-{topping}")

#make_pizza(40, 'pieczarki')
#make_pizza(30, 'pieczarki','zielona papryka', 'podwójny ser') 

