
# Content:
# - list index
# - multilist list 
# - element count for the list 
# - changing values in the list 
# - delete value from the list 
# - index() for list 
# - append() and insert() for list 
# - remove() for list 
# - sort() for list 
# - tuple

# list index 
list = ['cat','dog','bird','mouse','moose']
print(list[0])
print(list[3])
print(list[-1])

# multilist list 
multilist = [['cat','dog','bird','mouse','moose'],[0,1,2,3]]
print(multilist[0][-3])
print(multilist[1][3])

# element count for the list 
list = ['cat','dog','bird','mouse','moose']
print(len(list))

# changing values in the list 
list = ['cat','dog','bird','mouse','moose']
list[2] = 'gorilla'
print(list)

# delete value from the list 
list = ['cat','dog','bird','mouse','moose']
del list[2]
print(list)

# index() for list
list = ['cat','dog','bird','mouse','moose']
print(list.index('cat'))

# append() and insert() for list 
list = ['cat','dog','bird','mouse','moose']
list.append('gorilla')
list.insert(1,'gorilla',)
print(list)

# remove() for list 
list = ['cat','dog','bird','mouse','moose']
list.remove('dog')
print(list)

# sort() for list 
list = ['cat','dog','bird','mouse','moose']
list.sort()
print(list)

# tuple 
tuple = ('cat','dog','bird','mouse','moose')

# list() and tuple() 
tuple = ('cat','dog','bird','mouse','moose')
list(tuple)
