

initial_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Function to erase elements with specified index from the list
# parmeter: input_list - list containing all elements
# return: input_list - list containing list without specified elements
def newList (input_list):

    erase_index = [1, 4, 5]
    elements_to_erase = []

    for j in erase_index:
        elements_to_erase.append(input_list[j])

    for i in elements_to_erase:
        input_list.remove(i)

    input_list.sort()

    return input_list

# Create new list without specified elements
new_list = newList(initial_list)

print(new_list)

