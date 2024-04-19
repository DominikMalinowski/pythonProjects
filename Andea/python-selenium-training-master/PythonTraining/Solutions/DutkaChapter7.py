import re

text_to_search = """
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""


def getmails(maillist):
    regmail = r'((\w*[-.]*)*@[\w*-.]*([.]\w+))'
    mr = re.finditer(regmail, maillist)
    #mr = re.findall(regmail, maillist)
    mails = [x[0] for x in mr]
    return mails


print('Mails list: ', getmails(text_to_search))


