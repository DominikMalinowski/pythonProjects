# Function that removes specified list values and sort them
def list_converter(user_list):
    try:
        del user_list[5]
        del user_list[4]
        del user_list[1]
    except IndexError:
        try:
            del user_list[4]
            del user_list[1]
        except:
            try:
                del user_list[1]
            except:
                print('Yor list has only single element')
    user_list.sort(key=str.lower)
    print('List after conversion: \n' + str(user_list))


# Variables
ulist = []

# Ask user for a list

print('Please provide list  with ; as a delimiter:')
ulist = str(input()).split(';')  # Splitting text to list
for i in range(len(ulist)):
    ulist[i] = ulist[i].strip()  # Removing whitespaces
print('List before conversion: \n' + str(ulist))
print()

list_converter(ulist)
