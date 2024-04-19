#zadanie 4.10 wykonane jest w programie my_foods

#zadanie 4.11 
pizzas = ['dracula', '4 sery', 'mięsna']
for pizza in pizzas:
	print(f'Dzis polecamy pizze o nazwie {pizza.title()}')
print("Ale bym opierdzielił pizze\n")

zwierzeta = ['słoń', 'pies', 'krokodyl']
for zwierze in zwierzeta:
	print(f'{zwierze.title()} opierdzieliłby pizze')
print(f'Wszystkie wymienione zwierzęta opierdzieliłyby pizze')

friends_pizza=pizzas[:]
pizzas.append("hawajska")
friends_pizza.append("z rukolą")
print(pizzas)
print(friends_pizza)

for pizza in pizzas:
	print(f"Moje ulubione rodzaje pizzy to {pizza}")
for f_pizza in friends_pizza:
	print(f"Ulubione rodzaje pizzy mojego przyjaciela to {f_pizza}")

#zadanie 4.12 wykonane programie "food"