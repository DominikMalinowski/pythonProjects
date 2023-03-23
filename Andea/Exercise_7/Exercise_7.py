"""
Using re module, find all e-mail adresses in given string.
Hint: .findall method doesn't work well with groups in regular expressions :)
"""

text_to_search = """
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""
import re

email_reg = re.compile(r'\S+[@]\S+[.]\S+').findall(text_to_search)
print(email_reg)
