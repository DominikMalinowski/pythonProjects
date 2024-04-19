"""
Using re module, find all e-mail adresses in given string.
Hint: .findall method doesn't work well with groups in regular expressions :)
"""
import re

text_to_search = """
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""

mailRegex = re.compile(r'''
[A-Za-z\d_.+-]+ #first part 
\@ #symbol 
[A-Za-z\d_+-.]+ #second part 
''',re.VERBOSE)

print(mailRegex.findall(text_to_search))