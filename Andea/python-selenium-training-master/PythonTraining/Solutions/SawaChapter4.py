def nowalista(list):
    del list[5]
    del list[4]
    del list[1]
    list.sort()
    print(list)


lista = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
nowalista(lista)

