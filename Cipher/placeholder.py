#TODO:
# allow user to provide text or input populated file localization 
# find more cipher method 
# implement the Ceasar cipher 
# implement output file creation 


from modules import binary as b
from modules import input_method_selection as ims
from modules.file_managment import read_file as rf

user_input = ims.input_method_selection()

text_to_cipher = rf('input_file2.txt')

print(f'user select {user_input}')

def cipher_invoke(input):
    if input == '1':
        print('placeholder')
    elif input == '2':
        output = b.binary(text_to_cipher)

    return output

print(cipher_invoke(user_input))
