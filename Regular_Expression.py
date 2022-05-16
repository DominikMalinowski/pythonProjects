##
# expression characters

# \d - number 0-9
# \D - any number other than 0-9
# \w - any letter, number or _ character
# \W - any character other than letter, number or _ character
# \s - space, tabulator or new line character
# \S - any character other than space, tabulator or new line character

##
# expressions symbols

# (?) - zero or one expression for group before
# (*) - zero or more expression for group before
# (+) - one or more expression for group before
# (n) - n-times expression for group before
# (n,) - n-times or more expression for group before
# (n,m) - minimum n-times and maximum m-times expression for group before
# ^text - expression that text must start with word "text"
# text$ - expression that text must end with word "text"
# (.) - any character without new line character
# [abc] - only character from square bracket
# [^abc] - only character other than those from square bracket


##
# import regular expression module
import re
import re

# create regular expression
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# setting search space for expression
mo = phoneNumRegex.search('My phone number is 415-555-4242')

# displaying founded expression
print('Founded phone number ' + mo.group())

##
import re

# grouping regular expressions
phoneNumRegex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My phone number is 415-555-4242')
print('Founded phone number ' + mo.group())
print('Founded phone number ' + mo.group(1))

##
import re

# looking for multiple expressions
heroRegex = re.compile(r'Batman|Tina Faye')
mol = heroRegex.search('Batman i Tina Faye')
mol2 = heroRegex.search('Tina Faye i Batman')
# showing only first founded expression
print(mol.group())
print(mol2.group())

##
import re

# looking for multiple expressions with schema
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile loose his wheel')
print(mo.group())
print(mo.group(1))

##
import re

# looking for expression with optional part
batRegex = re.compile(r'Bat(wo)?man')
mol = batRegex.search('The Adventures of Batman')
print(mol.group())

mol2 = batRegex.search(r'The Adventures of Batwoman')
print(mol2.group())

##
import re

# looking for expression with multiple part
batRegex = re.compile(r'Bat(wo)*man')
mol = batRegex.search('The Adventures of Batman')
print(mol.group())

mol2 = batRegex.search(r'The Adventures of Batwoman')
print(mol2.group())

mol3 = batRegex.search(r'The Adventures of Batwowowowowowowoman')
print(mol3.group())

##
import re

# looking for expression with multiple instance of part
batRegex = re.compile(r'Bat(wo)+man')
mol = batRegex.search(r'The Adventures of Batwoman')
print(mol.group())

mol2 = batRegex.search(r'The Adventures of Batwowowowowowowoman')
print(mol2.group())

mol3 = batRegex.search(r'The Adventures of Batman')
print(mol3 == None)

##
import re

# looking for expression with exact number of repetition
# {3} - exactly three repetition
# {,5} - from zero to max 5 repetition
# {3,} - minimum three repetition
haRegex = re.compile(r'(Ha){3}')
mol = haRegex.search('HaHaHa')
print(mol.groups)

##
import re

text = 'HaHaHaHaHa'

# greedy expressions (maximal number of repetitions)
greedyHaRegex = re.compile(r'(Ha){3,5}')
mol = greedyHaRegex.search(text)
print(mol.group())

# non-greedy expressions (minimal number of repetitions)
nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mol = nonGreedyHaRegex.search(text)
print(mol.group())

##
import re

# displaying all correct expression
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Mobile: 415-555-9999, work: 212-555-0000')
print(mo.group())

mo2 = phoneNumRegex.findall('Mobile: 415-555-9999, work: 212-555-0000')
print(mo2)

##
import re

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipes, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, \
3 hens, 2 doves, 1 partridge'))

##
import re

# creating personal characters class
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop je pokarm dla dzieci. POKARM DLA DZIECI'))

##
import re

# creating personal expelled characters class (space also expelled)
vowelRegex = re.compile(r'[^aeiouAEIOU ]')
print(vowelRegex.findall('RoboCop je pokarm dla dzieci. POKARM DLA DZIECI'))

##
import re

# regular expression begging with exact characters
beginsWithHelloRegex = re.compile(r'^Hello')

print(beginsWithHelloRegex.search('Hello world'))
print(beginsWithHelloRegex.search('I say Hello'))

##
import re

# regular expression ending with exact characters
endWithNumber = re.compile(r'\d+$')

print(endWithNumber.search('Twój numer to 42'))
print(endWithNumber.search('Twój numer to czterdzieści dwa'))

##
import re

# regular expression using '.' as any character other than new line character
atRegex = re.compile(r'.ba')
print(atRegex.findall(' Baba bada baobaby. Baba dba o oba baobaby'))

##
import re

# regular expression for any text
nameRegex = re.compile(r'Name: (.*) Surname: (.*)')
mo = nameRegex.search('Name: Al Surname: Sweigart')
print(mo.group(1))
print(mo.group(2))

##
import re

# regular expression for everything including new line character
noNewLineRegex = re.compile('.*')
print(noNewLineRegex.search('To protect, \nto serve, \nto arrest niggers').group())

newLineRegex = re.compile('.*', re.DOTALL)
print(newLineRegex.search('To protect, \nto serve, \nto arrest niggers').group())

##
import re

# expression ignoring characters size
# re.I can be changed to re.IGNORCASE
robocop = re.compile('Robocop', re.I)

print(robocop.search('Robocop is half man, half machine and half cop').group())
print(robocop.search('ROBOCOP is fighting bad guys').group())

##
import re

# replacing text in regular expression
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('OCENZUROWANO', 'Agent Alice give classified documents to Agent Beatrice'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice inform Agent Beatrice that Agent Eve is double Agent John'))

##
import re

# complicated regular expression
compliRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?           #Area code 
(\s|-|\.)?                   #Delimiter
\d{3}                        #First three digit 
(\s|-|\.)                    #Delimiter 
\d{4}                        #Last four digit 
(\s*(ext|x|ext.)\s*\d{2,5})? #Extension
)''', re.VERBOSE)

##
import re

# giving regular expression multiple arguments
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

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
