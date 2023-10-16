# Content:
# - escaping 
# - raw string 
# - multiline text 
# - indeksing for string 
# - in() and not in() for strings 
# - upper(), lower(), isupper() and islower() for string 
# - isX() methods for string 
# - startwith() and endwith() for string
# - join() and split() for string 
# - rjust(), ljust() and center()
# - rjust(), ljust() and center()


# escaping 
print('Below is escaping')
print(f'This is Mr. O\'Hara')

# raw string 
print('Below is raw string')
print(r'This is Mr. Johnson')

# multiline text 
print(
"""
Multiline text 
is possible 
""")

# indeksing for string 
text = 'This is spam'

print(text[3])
print(text[-2])
print(text[3:6])
print(text[3:])
print(text[:6])

# in() and not in() for strings 
text = 'This is spam'
print('This' in text)
print('That' in text)

print('This' not in text)
print('That' not in text)

# upper(), lower(), isupper() and islower() for string 
text = 'This is spam'
print(text.upper())
print(text.lower())

print(text.isupper())
print(text.islower())

# isX() methods for string 
text = 'This is spam'
print(text.isalpha()) # only letter and not empty 
print(text.isalnum()) # only letter and number,and not empty 
print(text.isdecimal()) # only number and not empty 
print(text.isspace()) # only space, tab and not empty 
print(text.istitle()) # only text as Title 

# startwith() and endwith() for string
text = 'This is spam'
print(text.startswith('placeholder1'))
print(text.startswith('This'))

print(text.endswith('placeholder2'))
print(text.endswith('spam'))

# join() and split() for string 
text_join = ' '.join(['Text','has','been','joined'])
print(text_join)

text_split = text_join.split()
print(text_split)

# rjust(), ljust() and center()
text = 'placeholder'
print(text.rjust(20,'*'))
print(text.ljust(20,'*'))
print(text.center(20,'*'))

# rstrip(), lstrip() and strip()
text = '     placeholder     '
print(text.rstrip())
print(text.lstrip())
print(text.strip())