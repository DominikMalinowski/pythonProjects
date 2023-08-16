
def vigenere(text, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    vigenere_text = ''

    for i in range(len(text_int)):
        value = (text_int[i] + key_as_int[i % key_length]) % 26
        vigenere_text += chr(value + 65)
    return vigenere_text
