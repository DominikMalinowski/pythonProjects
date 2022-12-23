import re

text_to_search = """
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""

# Regular expression to find email pattern
emailRegex = re.compile(r'''
    [a-zA-Z0-9_.+-]+      # name
    @                     # @ symbol
    [a-zA-Z0-9_.+-]+      # domain
''', re.VERBOSE)

# Find all email addresses in text
email = emailRegex.findall(text_to_search)

print(email)