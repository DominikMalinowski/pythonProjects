# Content:
# - keys(), values() and items() for dictionary 
# - get() for dictionary 
# - setdefault() for dictionary 
# - pretty print 



# keys(), values() and items() for dictionary 
dic = {'key1':'value1','key2':'value2','key3':'value3'}
print(dic.keys())
print(dic.values())
print(dic.items())

# get() for dictionary 
dic = {'key1':'value1','key2':'value2','key3':'value3'}
print(dic.get('key2'))

# setdefault() for dictionary 
dic = {'key1':'value1','key2':'value2','key3':'value3'}
dic.setdefault('def_key','def_value')

# pretty print
import pprint
dic = {'key1':'value1','key2':'value2','key3':'value3','def_key':'def_value'}
pprint.pprint(dic, width=1)




