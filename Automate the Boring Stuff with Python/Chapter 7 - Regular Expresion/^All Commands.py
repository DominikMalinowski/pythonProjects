# Content:
# - import regular expression module
# - creating regular expression object 
# - using regular expresion for search 
# - displaying founded expression
# - grouping for regular expression
# - looking for multiple expressions
# - looking for multiple expressions with schema
# - looking for expression with optional part
# - looking for expression with multiple part
# - looking for expression with multiple instance of part
# - looking for expression with exact number of repetition
# - greedy expressions (maximal number of repetitions)
# - non-greedy expressions (minimal number of repetitions)
# - displaying all correct expression
# - creating personal characters class
# - creating personal expelled characters class (space also expelled)
# - regular expression begging with exact characters
# - regular expression ending with exact characters
# - regular expression using '.' as any character other than new line character
# - regular expression for any text
# - regular expression for everything including new line character
# - expression ignoring characters size
# - replacing text in regular expression
# - complicated regular expression
# - giving regular expression multiple arguments
# - regular expression for email


# Expression characters cheatsheet:

# \d - number 0-9
# \D - any number other than 0-9
# \w - any letter, number or _ character
# \W - any character other than letter, number or _ character
# \s - space, tabulator or new line character
# \S - any character other than space, tabulator or new line character


# Expressions symbols cheatsheet:

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


# import regular expression module
import re

# creating regular expression object 

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# using regular expresion for search 
matchObject = phoneNumRegex.search('My phone number is 415-555-4242')

# displaying founded expression
print('Founded phone number ' + matchObject.group())

# grouping regular expressions
phoneNumRegex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('My phone number is 415-555-4242')
print('Founded phone number ' + matchObject.group())
print('Founded phone number ' + matchObject.group(1))

# looking for multiple expressions
import re
heroRegex = re.compile(r'Batman|Tina Faye')
matchObject = heroRegex.search('Batman i Tina Faye')
matchObject2 = heroRegex.search('Tina Faye i Batman')

# showing only first founded expression
print(matchObject.group())

# looking for multiple expressions with schema
import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
matchObject = batRegex.search('Batmobile loose his wheel')
print(matchObject.group())
print(matchObject.group(1))

# looking for expression with optional part
import re
batRegex = re.compile(r'Bat(wo)?man')
matchObjectList = batRegex.search('The Adventures of Batman')
print(matchObjectList.group())

matchObjectList2 = batRegex.search(r'The Adventures of Batwoman')
print(matchObjectList2.group())

# looking for expression with multiple part
import re
batRegex = re.compile(r'Bat(wo)*man')
matchObjectList = batRegex.search('The Adventures of Batman')
print(matchObjectList.group())

matchObjectList2 = batRegex.search(r'The Adventures of Batwoman')
print(matchObjectList2.group())

matchObjectList3 = batRegex.search(r'The Adventures of Batwowowowowowowoman')
print(matchObjectList3.group())

# looking for expression with multiple instance of part
import re
batRegex = re.compile(r'Bat(wo)+man')
matchObjectList = batRegex.search(r'The Adventures of Batwoman')
print(matchObjectList.group())

matchObjectList2 = batRegex.search(r'The Adventures of Batwowowowowowowoman')
print(matchObjectList2.group())

matchObjectList3 = batRegex.search(r'The Adventures of Batman')
print(matchObjectList3 == None)

# looking for expression with exact number of repetition
import re
haRegex = re.compile(r'(Ha){3}')
matchObjectList = haRegex.search('HaHaHa')
print(matchObjectList.groups)

# greedy expressions (maximal number of repetitions)
import re
text = 'HaHaHaHaHa'
greedyHaRegex = re.compile(r'(Ha){3,5}')
matchObjectList = greedyHaRegex.search(text)
print(matchObjectList.group())

# non-greedy expressions (minimal number of repetitions)
nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
matchObjectList = nonGreedyHaRegex.search(text)
print(matchObjectList.group())

# displaying all correct expression
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('Mobile: 415-555-9999, work: 212-555-0000')
print(matchObject.group())

matchObject = phoneNumRegex.findall('Mobile: 415-555-9999, work: 212-555-0000')
print(matchObject)

# creating personal characters class
import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop je pokarm dla dzieci. POKARM DLA DZIECI'))

# creating personal expelled characters class (space also expelled)
import re
vowelRegex = re.compile(r'[^aeiouAEIOU ]')
print(vowelRegex.findall('RoboCop je pokarm dla dzieci. POKARM DLA DZIECI'))

# regular expression begging with exact characters
import re
beginsWithHelloRegex = re.compile(r'^Hello')

print(beginsWithHelloRegex.search('Hello world'))
print(beginsWithHelloRegex.search('I say Hello'))

# regular expression ending with exact characters
import re
endWithNumber = re.compile(r'\d+$')

print(endWithNumber.search('Twój numer to 42'))
print(endWithNumber.search('Twój numer to czterdzieści dwa'))

# regular expression using '.' as any character other than new line character
import re
atRegex = re.compile(r'.ba')
print(atRegex.findall(' Baba bada baobaby. Baba dba o oba baobaby'))

# regular expression for any text
import re
nameRegex = re.compile(r'Name: (.*) Surname: (.*)')
matchObject = nameRegex.search('Name: Al Surname: Sweigart')
print(matchObject.group(1))
print(matchObject.group(2))

# regular expression for everything including new line character
import re
noNewLineRegex = re.compile('.*')
print(noNewLineRegex.search('To protect, \nto serve, \nto arrest niggers').group())

newLineRegex = re.compile('.*', re.DOTALL)
print(newLineRegex.search('To protect, \nto serve, \nto arrest niggers').group())

# expression ignoring characters size
import re
# re.I can be changed to re.IGNORCASE
robocop = re.compile('Robocop', re.I)

print(robocop.search('Robocop is half man, half machine and half cop').group())
print(robocop.search('ROBOCOP is fighting bad guys').group())

# replacing text in regular expression
import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('OCENZUROWANO', 'Agent Alice give classified documents to Agent Beatrice'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice inform Agent Beatrice that Agent Eve is double Agent John'))

# complicated regular expression
import re
compliRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?           #Area code 
(\s|-|\.)?                   #Delimiter
\d{3}                        #First three digit 
(\s|-|\.)                    #Delimiter 
\d{4}                        #Last four digit 
(\s*(ext|x|ext.)\s*\d{2,5})? #Extension
)''', re.VERBOSE)

# giving regular expression multiple arguments
import re
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# regular expression for email
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+   #User name
@                   #Delimiter
[a-zA-Z0-9.-]+      #Domens name
(\.[a-zA-Z]{2,4})  # Point and everything else
)''', re.VERBOSE)
