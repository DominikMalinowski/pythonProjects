#requested_topping=("pieczarki","podwójny ser")
#if requested_topping != "anchois":
#    print("poproszę o anchois!")

#if "pieczarki" in requested_topping:
#    print("dodaję pieczarki")
#if "peperoni" in requested_topping:
#    print("dodaję peperoni")
#if "podwójny ser" in requested_topping:
#    print("dodaję podwójny ser")

#print("\n Twoja pizza jest gotowa\n")

#requested_toppings=("pieczarki", "boczek","podwójny ser")
#for requested_topping in requested_toppings:
#    if requested_topping == "boczek":
#        print("Niestety nie mamy boczku")
#    else:
#        print(f"Dodaję {requested_topping}.")
#print("\n Twoja pizza jest już gotowa")

#requested_toppings =[]
#if requested_toppings:
#    for requested_topping in requested_toppings: 
#        print(f"Dodaję {requested_topping}")
#    print("\n Twoja pizza jest gotowa")
#else:
#
available_toppings = ["pieczarki","oliwki","boczek","peperoni","ananas","podwójny ser"]
requested_toppings = ["pieczarki", "frytki","podwójny ser"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Dodaję {requested_topping}.")
    else:
        print(f"Niestety nie posiadamy obecnie dodatku - {requested_topping}")
print("Twoja pizza jest już gotowa")