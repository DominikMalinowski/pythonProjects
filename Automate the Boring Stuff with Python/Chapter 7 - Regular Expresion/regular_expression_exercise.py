##
import re

num1 = '42'
num2 = '1.234'
num3 = '6.368.745'
num4 = '12.34.567'
num5 = '1234'
numbers = (num1, num2, num3, num4, num5)

numRegex = re.compile(r'(\d{1,3})(\.\d{3})*')
print(numRegex.findall(str(numbers)))

##
import re
data = ('Satoshi Nakamoto, Alicja Nakamoto, Robocop Nakamoto, satoshi Nakamoto, Mr. Nakamoto, Nakamoto, Satoshi nakamoto')

nakamotoRegex = re.compile(r'[A-Z][a-z]*\sNakamoto')
print(nakamotoRegex.findall(data))

##
import re
text = ('Alicja je jablko., Bob glaszcze kota., Karol rzuca pilke., Alicja rzuca jablko., BOB GLASZCZE KOTA., \
RoboCop je jablko., ALICJA RZUCA PILKE., Karol je siodmego kota.')

textRegex = re.compile(r'(Alicja|Bob|Karol)\s(je|glaszcze|rzuca)\s(jablko|kota|pilke)\.$', re.IGNORECASE)
print(textRegex.findall(text))

text2Regex = re.compile(r'(Alicja|Bob|Karol)\s(je|glaszcze|rzuca)\s(jablko|kota|pilke)\.', re.I)
print(text2Regex.findall(text))

##
import re
data = ['shortpw', '8charact', 'onlylower', 'ONLYUPPER', 'NoDigitDigit', 'C0rrectPw']
def passcheck(password):
    print(f'Checking {password}:')
    # minimum of 8 characters
    lenghtRegex = re.compile(r'.{8,}')

    # at least one upper, one lower and one number
    alfnumRegex = re.compile(r'([a-z])([A-Z])(\d)')

    # at least one symbol
    symbRegex = re.compile(r'\W')

    if lenghtRegex.search(password) is None:
        print('Your password is too short - minimal length is 8 characters')
        return False
    if alfnumRegex.search(password) is None:
        print('Your password must contains at least one uppercase letter, one lowercase letter and one number')
        return False
    if symbRegex.search(password) is None:
        print('Your password must contain at least one special character')
        return False

    return True

for pw in data:
    print(passcheck(pw))
passcheck(data)
