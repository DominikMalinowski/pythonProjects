# Content:
# - creating regular expression object 
# - using regular expresion for search 
# - grouping for regular expression

# creating regular expression object 
import re 
numberRegularExpresion = re.compile(r'\d\d\d-\d\d\d-\d\d\d')

# using regular expresion for search 
text = 'My phone number is 123-456-789'
matchObject = numberRegularExpresion.search(text)
print(f'Finded match: \n'+ matchObject.group())

# grouping for regular expression
import re 
numberRegularExpresion_2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
text = 'My phone number is 123-456-789'
matchObject = numberRegularExpresion_2.search(text)
print(f'Finded match: \n'+ matchObject.group(1))
print(f'Finded match: \n'+ matchObject.group(2))

#  