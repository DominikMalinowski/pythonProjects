##zadanie pierwsze
backpack = {'strzały':12,'złote monety':42,'lina':1,'pochodni':6,'sztylet':1}

def displayInventory(inventory):
    print("Inventarz:")
    item_total = 0
    for k,v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print('Całkowita liczba przedmiotów: '+ str(item_total))

displayInventory(backpack)

##zadanie drugie
backpack = {'złote monety':42,'lina':1}

dragonLooot = ['złote monety','sztylet','złote monety','złote monety','rubin']

def displayInventory(inventory):
    print("Inventarz:")
    item_total = 0
    for k,v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print('Całkowita liczba przedmiotów: '+ str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] += 1
    return inventory

addToInventory(backpack,dragonLooot)
displayInventory(backpack)

