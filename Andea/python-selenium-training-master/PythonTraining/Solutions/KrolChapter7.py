import re  # Regular expression module

# Text where are we looking for email addresses
text_to_search = """
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""

email_address_regex = re.compile(r'([\w+.-]+@[\w+.-]+)') # Email address regular expression

emails = email_address_regex.findall(text_to_search)
for i in range(len(emails)):
        print(emails[i])