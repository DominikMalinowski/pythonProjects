import PyPDF2
import os

# Function to read data from file
# parameter: file_path - string containing path to file
# return: content - string containing content from
def readFile(file_path):
    new_file = open(file_path)
    content = new_file.read()
    new_file.close()
    return content

# Function to close pdf file
# parameter: pdf - PDF file object
def closePdf(pdf):
    pdf.close()

# Function to decrypt PDF
# parameter: pdf_path - string containing path to pdf file
# parameter: dictionary - list containig dictionary with words
# return: pdf_reader - PDF reader object
# return: pdf_file - PDF file object
def decryptPdf(pdf_path, dictionary):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for word in dictionary:
        is_decrypted = pdf_reader.decrypt(word)
        if is_decrypted != 0:
            #print("Password is: " + word)
            break
        else:
            continue
    return pdf_reader, pdf_file

# Function to create pdf from alredy existent file
# parameter: pdf_reader - PDF reader object
def createPDF(pdf_reader):
    writer = PyPDF2.PdfFileWriter()
    number_of_pages = int(pdf_reader.getNumPages())
    for j in range(number_of_pages):

        # For even pages modulo 2 is not equal to 0, because first page has index 0
        if j % 2 != 0:
            page = pdf_reader.getPage(j)
            writer.addPage(page)

    output = open('Output.pdf', 'wb')
    writer.write(output)


dictionary_path = '..\\Excercises\\Chapter13dictionary.txt'
pdf_path = '..\\Excercises\\Chapter13pdf.pdf'

# Create list from string containig dictionary from the file
dictionary_list = readFile(dictionary_path).split('\n')

[pdf_reader, pdf_file] = decryptPdf(pdf_path, dictionary_list)

createPDF(pdf_reader)
closePdf(pdf_file)
