
print('Put the list with ; as a delimiter')
text=input()
newstext=text.replace(' ','')
lines=newstext.split(';')
lines.remove('')
print(lines)