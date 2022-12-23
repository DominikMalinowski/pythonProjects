#zadanie 7.8 
sandwiches_orders = ["bekonowy sumo", "kanapka z pastrami", "jebaka", 
    "kanapka z pastrami", "drugi_jebaka", "kanapka z pastrami", "śledz do ryja", 
    "suchy chleb dla konia" ]
finished_sandwiches = [] 

#while sandwiches_orders: 
#    in_progress = sandwiches_orders.pop()
#    print(f"Przygotowano kanapkę: {in_progress.title()}")
#    finished_sandwiches.append(in_progress)
#print(f"Zrobiono nast. kanapki: {finished_sandwiches}")

#zadanie7.9
print("\nObecnie w kuchni brakuje: 'kanapka z pastrami'")

while "kanapka z pastrami" in sandwiches_orders:
    sandwiches_orders.remove("kanapka z pastrami")
print(sandwiches_orders)

#zadanie 7.10 
imie = input("Jak masz na imię ?")
miejsce = input("Jakie miejsce chciałbyś odwiedzić ?")
wyniki_ankiety[imie] = miejsce

print(f"{name} chciałby odwiedzić {miejsce} ")
        
