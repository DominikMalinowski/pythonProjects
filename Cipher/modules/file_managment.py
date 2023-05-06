
def read_file(file):
    open_file = open(file)
    content = open_file.read()
    return content

def save_output_as_file(output_text):
    new_file = open('coded_input_text.txt', 'w')
    new_file.write(output_text)
    new_file.close