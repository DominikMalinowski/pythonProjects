
def method_selection(**arguments):
    options = [arguments]
    input_message = "Please select one of below option:\n"
    user_input = ''

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)

    return user_input


input_methods = ['Provide text to cipher', 'Populate input file']
cipher_methods = ['Binary','Caesar shift', 'Vigenere Cipher']

cipher_method_selection = method_selection(cipher_methods)
input_method_selection = method_selection(input_methods)

