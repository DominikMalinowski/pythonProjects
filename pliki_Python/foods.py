my_foods=["pizza", "falafel", "ciasto z czekoladą", "biszkopt", "naleśniki"]
friend_food = my_foods[:]

print(f"Moje ulubione potrawy to:\n{my_foods}")
print(f'\nUlubione potrawy mojego przyjaciela to: {friend_food}')

my_foods.append("lody")
friend_food.append("canoli")

print(f"\nMoje ulubione potrawy to:\n{my_foods}")
print(f'\nUlubione potrawy mojego przyjaciela to: {friend_food}')

print(f"Pierwsze trzy elementy listy to:{my_foods[:3]}")
print(len(my_foods))
print(f"Trzy środkowe elementy listy to: {my_foods[1:4]}")
print(f"Ostatnie trzy elementy listy to: {my_foods[-3:]}")

for food in my_foods: 
	print(food)
for f_food in friend_food: 
	print(f_food)
