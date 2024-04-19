def Chapter6(stringlist):
    stringlist = stringlist.split(";") #divide into list by ; as a separator
    if len(stringlist) > 5:
        stringlist.pop(4) #delete from the end: 5th element
        stringlist.pop(3) #4th
        stringlist.pop(0) #1st
        return stringlist #return list
    else:
        raise Exception('List length is smaller than 5') #add exception for too short lists

try:
    print(Chapter6.Chapter6("Red;Green;White;Black;Pink;Yellow"))
except Exception as error:
    print(error)
try:
    print(Chapter6.Chapter6("Black;Pink;Yellow"))
except Exception as error:
    print(error)