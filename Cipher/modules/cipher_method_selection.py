
def cipher_method_selection():
    options = ['Binary','Caesar shift', 'Vigenere Cipher']
    input_message = "Please select you cipher method:\n"
    user_input = ''

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    return user_input
