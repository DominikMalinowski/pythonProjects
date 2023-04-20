
def binary(text):
    binary_text = ' '.join(format(ord(x), 'b') for x in text)
    return binary_text
