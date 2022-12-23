#Write a Python program to print a specified list after removing the 1th, 4th and 5th elements. The results should be sorted.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Black', 'Red', 'White']




list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print (list)
print ("List length:" + str(len(list)) + "\n")

del list[5]
del list[4]
del list[1]

list.sort()

print (list)
print ("List length:" + str(len(list)))