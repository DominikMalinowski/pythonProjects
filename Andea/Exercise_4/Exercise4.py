"""
Write a Python program to print a specified list after removing the 1th, 4th and 5th elements.
The results should be sorted.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Black', 'Red', 'White']
"""
#
colors_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
elements = [1, 4, 5]


def remove_element(input_list, removed_elements):

    # code to remove 1st, 4th and 5th element
    for i in reversed(removed_elements):
        input_list.remove(input_list[i])

    # sorting edited list
    input_list.sort()

    # printing finished list
    print(input_list)


remove_element(colors_list, elements)
