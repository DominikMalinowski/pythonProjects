
def vigenere(text, key):
    vigenere_text = []

    for i in range(len(text)):
        x = (ord(text[i]) +
             ord(key[i])) % 26
        x += ord('A')
        vigenere_text.append(chr(x))
    return("" . join(vigenere_text))
     
vigenere('dupa','zad')
