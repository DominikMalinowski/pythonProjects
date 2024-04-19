"""
Write a Python program to print a specified list after removing the 1th, 4th and 5th elements.
The results should be sorted.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Black', 'Red', 'White']
"""

sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
elements_to_remove = [1,4,5]
erase_list = []

# creating list of elements that have to be removed 
for i in range(len(sample_List)):
    if i in elements_to_remove:
        erase_list.append(sample_List[i])

# removing selected elements from the list 
for element in erase_list:
    if element in sample_List:
        sample_List.remove(element)

# sorting list 
sample_List.sort()
print(sample_List)

