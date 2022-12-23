def remove_items(list_):
    try:
        del list_[4]
        del list_[3]
        del list_[0]
    except IndexError:
        return
    sorted_list = list_.sort()
    return sorted_list


before_list = input('Enter at least 5 items (use ; as a delimiter) which will be added to the list\n')
before_list = before_list.replace(' ', '')
after_list = before_list.split(';')

print(after_list)

input_len = len(after_list)
print('Your list has ' + str(input_len) + ' elements and contains: ' + str(after_list))

if input_len < 5:
    print('You\'re list is too short to remove elements')
else:
    remove_items(after_list)
    print('Your list after removing operation:' + str(after_list))