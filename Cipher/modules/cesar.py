
def cesar(text, shift): 
    cesar_text = ''

    for i in range(len(text)):
        char = text[i]

        #adding spaces to text 
        if char == ' ':
            cesar_text += ' '
        #encrypt lowercase letters 
        elif (char.isupper()):
            cesar_text += chr((ord(char)+ shift -65) %26 + 65)    
        #encrypt uppercase letters     
        else:
            cesar_text += chr((ord(char) + shift-97) %26 + 97)
    return cesar_text
