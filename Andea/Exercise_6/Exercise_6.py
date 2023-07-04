"""
adjust your solution for chapter 4, and allow user to put the list with ; as a delimiter.
You should also remove white spaces from the imput.
"""
# Input list with ; as delimiter
sample_List_2 = [' Red; Green; White; Black; Pink; Yellow ']
elements_to_remove = [1,4,5]
erase_list = []

# Change list into string, strip and replace ; 
sample_List_string = sample_List_2[0]
list_stripped = sample_List_string.replace(' ','')
list_stripped_and_replaced = list_stripped.replace(';',',')
sample_List = list_stripped_and_replaced.split(',')

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

