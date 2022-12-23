""" Using re module, find all e-mail adresses in given string.
Hint: .findall method doesn't work well with groups in regular expressions :)

text_to_search =
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""

#  import re module with all regex functions

import re

# [] A set of characters
# \w Returns a match where string contains any word characters (from a to Z ,digits  0-9, the underscore character)
# .  Any character (except newline character)
# +	 One or more occurrences

# Regular expression finding e-mails
emailRegex = re.compile(r'[\w\.-]+@[\w\.-]+')

# Search for all e-mail addresses in below text. Change text in """ """" to check if works for another data
match = emailRegex.findall("""text_to_search =
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
""")

# Returns a list containing all matches e-mail addresses from the above text:
if len(match) > 1:
    print('\nYour text contains ' + str(len(match)) + ' e-mail addresses:')
    print(match)
elif len(match) == 1:
    print('\nYour text contains ' + str(len(match)) + ' e-mail address:')
    print(match)
else:
    print('\nYour text  does not contain e-mail any address.')
