# V 1.1 - 14.05.2019
"""
Write a Python program to print a specified list after removing the 1th, 4th and 5th elements. The results should be sorted.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Black', 'Red', 'White']
"""
#creating of the new list
S_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(S_List)

my_list = S_List

#deleting of [5] element from the list
my_list.remove(my_list[5])

#deleting of [4] element from the list
my_list.remove(my_list[4])

#deleting of [1] element from the list
my_list.remove(my_list[1])

#sorting of the list
my_list.sort()
print(my_list)