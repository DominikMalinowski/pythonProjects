#
# def is_phone_number(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True
#
# message = 'Zadzwon pod numer 415-555-1011 po przerwie. 415-555-9999 to moje biuro'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if is_phone_number(chunk):
#         print('Znaleziono numer telefonu '+ chunk)
# print('Gotowe')

import re
phoneNumRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Mó numer telefonu to 415-555-4242')
print('Znaleziono numer telefonu '+mo.group())
print(mo.group(1))
mo2 = phoneNumRegex.search('Mó numer telefonu to 555-4242')
print('Znaleziono numer telefonu '+mo2.group())


print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# import re
# heroRegex = re.compile(r'Batman|Tina Faye')
# mol = heroRegex.search('Batman i Tina Faye')
# print(mol.group())
#
# mo2 = heroRegex.search('Tina Faye i Batman')
# print(mo2.group())
#
# batRegex = re.compile(r'Bat(man|mobil|copter|bat)')
# mo = batRegex.search('Batmobil stracił koło')
# print(mo.group())
# print(mo.group(1))
#
# batRegex = re.compile(r'Bat(wo)?man')
# mol = batRegex.search('The Adventures of Batman')
# print(mol.group())
#
# mol2 = batRegex.search(r'The Adventures of Batwoman')
# print(mol2.group())

