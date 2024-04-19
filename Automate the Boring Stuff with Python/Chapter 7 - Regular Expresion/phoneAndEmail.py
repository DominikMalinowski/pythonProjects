## project for complex regular expressions

import pyperclip
import re

# regular expression for phone number
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?               #Area code
(\s|-|\.)?                      #Delimiter
(\d{3})                         #First 3 number
(\s|-|\.)                       #Delimiter
(\d{4})                         #Last 4 number
(\s*(ext|x|ext.)\s*(\d{2,5}))?  #Extension
)''', re.VERBOSE)

# regular expression for email
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+   #User name
@                   #Delimiter
[a-zA-Z0-9.-]+      #Domens name
(\.[a-zA-Z]{2,4})  # Point and everything else
)''', re.VERBOSE)

# looking for expression in clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy values to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copy to clipboard')
    print('\n'.join(matches))
else:
    print('No phone number or email address has been found')