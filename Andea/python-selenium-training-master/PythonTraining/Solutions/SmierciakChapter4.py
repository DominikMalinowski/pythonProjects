def Chapter4(inputlist):
    if len(inputlist) > 5:
        inputlist.pop(4) #delete from the end: 5th element
        # inputlist.pop(3) #4th
        inputlist.pop(4)  # 4th
        # inputlist.pop(0) #1st
        inputlist.pop(1)  # 1st
        return inputlist #return list
    else:
        raise Exception('List length is smaller than 5') #add exception for too short lists

print(Chapter4(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))