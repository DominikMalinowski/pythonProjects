#TODO:
# allow user to provide text or input populated file localization 
# implement the Ceasar cipher 
# implement the Vigenere Cipher


from modules import binary as b
from modules import cipher_method_selection as cms
from modules import inputh_method_selection as ims
from modules.file_managment import read_file as rf
from modules.file_managment import save_output_as_file as soaf

input_selected = ims.input_method_selection()
method_selected = cms.cipher_method_selection()

# make user input method possible 
def provide_text_to_cipher(input_method):
    if input_method == '1':
        text_to_cipher = input()
        print(text_to_cipher)
    elif input_method =='2':
        text_to_cipher = rf('input_file.txt')
    return text_to_cipher

print(f'User select {method_selected}')

def cipher_invoke(input, text_to_cipher):
    if input == '1':
        output = b.binary(text_to_cipher)

    elif input == '2':
        print('placeholder')

    elif input == '3':
        print('placeholder')

    return output

soaf(cipher_invoke(method_selected))

print('Coding has been completed')