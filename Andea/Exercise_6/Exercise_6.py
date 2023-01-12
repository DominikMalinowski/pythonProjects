"""
adjust your solution for chapter 4, and allow user to put the list with ; as a delimiter.
You should also remove white spaces from the imput.
"""


sample_List = [' Red ; Green ; White ; Black ; Pink ; Yellow ']
elements_to_remove = [1,4,5]
erase_list = []
remodeled_item_list = []

input_list = input()
new_list = [remodeled_item_list.strip() for item in input_list]


# # creating list of elements that have to be removed 
# for i in range(len(sample_List)):
#     if i in elements_to_remove:
#         erase_list.append(sample_List[i])

# # removing selected elements from the list 
# for element in erase_list:
#     if element in sample_List:
#         sample_List.remove(element)

# # sorting list 
# sample_List.sort()
# print(sample_List)

