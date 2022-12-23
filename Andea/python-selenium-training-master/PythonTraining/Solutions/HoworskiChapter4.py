
# initial list
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# remove 1, 4 and 5 element from the list
color = [x for (i,x) in enumerate(color) if i not in (1,4,5)]

# sort the list
color.sort()

# print the content of the list
print(color)

