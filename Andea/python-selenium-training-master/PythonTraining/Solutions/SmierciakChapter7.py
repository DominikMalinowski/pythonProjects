'''
Using re module, find all e-mail adresses in given string.
Hint: .findall method doesn't work well with groups in regular expressions :)


text_to_search = """
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""
'''
import re

#define function
def Chapter7(str):
#check if string is not empty
    if str != "":
#store result of regular expression into variable x
        x = re.findall(r"(\S+\b@\w..\S+)", str)
        if x is not None:
            return x;
        else:
            return ("no email addresses found")
    elif str == "":
        return ("string is empty")

#test for string from excercise
print(Chapter7("""
Mark Davis MarkDavis@gmail.com
Carl Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl
"""))

#test for different emails
print(Chapter7("""
Mark Davis MarkDavis@gmail.com ksmierciak@andea.com
Carl ksmierciak@andea.com Jugen carl.jugen@university.edu
Black Dynamite black-123-dynamite@very-explosive.pl notam@il jpiaszczak@andea.com.pl
"""))
