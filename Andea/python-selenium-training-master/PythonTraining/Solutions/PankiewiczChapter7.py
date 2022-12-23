# V 1.0 - 15.05.2019

"""
Using re module, find all e-mail adresses in given string.
Hint: .findall method doesn't work well with groups in regular expressions :)
"""

text_to_search = """
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""
#import 're' module, to use its operations
import re

#list with all strings of characters, that have:
    # [\w.-]+   --> look for Any letter, numeric digit, or the underscore character; also '.'; also '-'. This whole group must appears at least one time
    #@+ --> than look for '@', that appear at least one time
match = re.findall(r'([\w.-]+@+[\w.-]+)', text_to_search)

#print list 'match'
print(match)

