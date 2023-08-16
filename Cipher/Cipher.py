
from modules import binary as b
from modules import cesar as c
from modules import vigenere as v
from modules import cipher_method_selection as cms


def cipher_invoke():
    print('Please provide text to cipher')
    text_to_cipher = input()

    method_selected = cms.cipher_method_selection()

    if method_selected == '1':
        output = b.binary(text_to_cipher)

    elif method_selected == '2':
        print('Please provide letters shift to encrypt message')
        shift = input()
        output = c.cesar(text_to_cipher, shift)

    elif method_selected == '3':
        print('Please provide key to encrypt message')
        key = input()
        output = v.vigenere(text_to_cipher, key)

    return output

print(cipher_invoke())